-- Iniciar transacción
START TRANSACTION;

-- Eliminar el procedimiento almacenado si ya existe
DROP PROCEDURE IF EXISTS UpdatePatientAddresses;

-- Declarar variables
DELIMITER $$
CREATE PROCEDURE UpdatePatientAddresses()
BEGIN
    -- Declarar variables locales
    DECLARE done INT DEFAULT FALSE;
    DECLARE domicilio_id INT;
    DECLARE street_address VARCHAR(255);
    DECLARE street_line_2_address VARCHAR(255);
    DECLARE patient_id INT;

    -- Cursor para recorrer pacientes dentro del rango especificado
    DECLARE cur CURSOR FOR 
        SELECT id
        FROM openemr.patient_data
        WHERE id BETWEEN 477202 AND 500050; -- Limitar el rango de IDs aquí

    -- Manejo de errores
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Abrir cursor
    OPEN cur;

    -- Loop para recorrer pacientes y actualizar direcciones
    paciente_loop: LOOP
        -- Leer el siguiente ID de paciente
        FETCH cur INTO patient_id;

        -- Salir del loop si no hay más pacientes
        IF done THEN
            LEAVE paciente_loop;
        END IF;

        -- Seleccionar un domicilio aleatorio y obtener la dirección y street_line_2
        SELECT CONCAT(TIPOVIAL, ' ', NOMVIAL, ' ', IFNULL(NUMEXT, '')) AS street_address,
               CONCAT(TIPOASEN, ' ', NOMASEN) AS street_line_2_address
        INTO street_address, street_line_2_address
        FROM domicilios_tijuana.domicilios
        WHERE RAND() <= 0.0001 -- Reducir el rango de aleatoriedad para mejorar la eficiencia
        LIMIT 1; -- Limitar la consulta a un solo resultado

        -- Actualizar la dirección y street_line_2 del paciente
        UPDATE openemr.patient_data
        SET
            street = street_address,
            street_line_2 = street_line_2_address
        WHERE id = patient_id;
    END LOOP paciente_loop;

    -- Cerrar cursor
    CLOSE cur;
END$$
DELIMITER ;

-- Ejecutar el procedimiento almacenado
CALL UpdatePatientAddresses();

-- Finalizar la transacción
COMMIT;

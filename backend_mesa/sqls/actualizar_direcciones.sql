-- Iniciar transacción
START TRANSACTION;

-- Eliminar el procedimiento almacenado si ya existe
DROP PROCEDURE IF EXISTS UpdatePatientAddresses;

-- Declarar variables
DELIMITER $$
CREATE PROCEDURE UpdatePatientAddresses()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE street_address VARCHAR(255);
    DECLARE street_line_2_address VARCHAR(255);
    DECLARE patient_id INT;

    -- Cursor para recorrer domicilios_tijuana
    DECLARE cur CURSOR FOR 
        SELECT OBJECTID, CONCAT(TIPOVIAL, ' ', NOMVIAL, ' ', IFNULL(NUMEXT, '')) AS street,
                          CONCAT(TIPOASEN, ' ', NOMASEN, ' ') AS street_line_2_address
        FROM domicilios_tijuana.domicilios;

    -- Manejo de errores
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Abrir cursor
    OPEN cur;

    -- Recorrer todas las filas de domicilios_tijuana dentro del rango especificado
    REPEAT
        -- Leer la siguiente dirección y OBJECTID
        FETCH cur INTO patient_id, street_address, street_line_2_address;

        -- Actualizar los campos en la tabla patient_data solo si hay un paciente correspondiente
        IF NOT done THEN
            UPDATE openemr.patient_data
            SET
                street = street_address,
                street_line_2 = street_line_2_address
            WHERE id = patient_id;
        ELSE
            -- Si no hay más filas, reiniciar el cursor para recorrer desde el principio
            CLOSE cur;
            OPEN cur;
            SET done = FALSE;
        END IF;

    -- Hasta que no haya más filas
    UNTIL done END REPEAT;

    -- Cerrar cursor
    CLOSE cur;
END$$
DELIMITER ;

-- Ejecutar el procedimiento almacenado
CALL UpdatePatientAddresses();

-- Finalizar la transacción
COMMIT;

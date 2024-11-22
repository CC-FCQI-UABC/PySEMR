import React, { useState, useEffect } from 'react';
import './GraphDisplay.css';
import { CSVLink } from "react-csv"; // Importando la librería para descargar CSV
import seasonalPatientCounts from './seasonal_patient_counts.png';

function GraphDisplay({ data }) {
  const [selectedColumns, setSelectedColumns] = useState({
    first_name: false,
    last_name: false,
    city: false,
    state: false,
    email: false,
    phone: false,
    diseases: false,
  });

  const [filteredPatientData, setFilteredPatientData] = useState([]);

  // Actualizar los datos filtrados según las columnas seleccionadas
  useEffect(() => {
    if (data?.patient_data && Array.isArray(data.patient_data)) {
      const updatedData = data.patient_data.map((patient) => {
        const filteredPatient = {};
        if (selectedColumns.first_name) filteredPatient.first_name = patient.name_data?.first_name;
        if (selectedColumns.last_name) filteredPatient.last_name = patient.name_data?.last_name;
        if (selectedColumns.city) filteredPatient.city = patient.address_data?.city;
        if (selectedColumns.state) filteredPatient.state = patient.address_data?.state;
        if (selectedColumns.email) filteredPatient.email = patient.contact_data?.email;
        if (selectedColumns.phone) filteredPatient.phone = patient.contact_data?.phone;
        if (selectedColumns.diseases) filteredPatient.diseases = patient.diseases_contracted?.join(', ');
        // Agregar más campos según sea necesario
        return filteredPatient;
      });
      setFilteredPatientData(updatedData);
    }
  }, [selectedColumns, data?.patient_data]);

  // Manejar el cambio en la selección de columnas
  const handleColumnChange = (event) => {
    const { name, checked } = event.target;
    setSelectedColumns((prev) => ({
      ...prev,
      [name]: checked,
    }));
  };

  return (
    <div className="graph-display">
      <img src={seasonalPatientCounts} alt="Patient Seasonal Data" className="graph-image" />
      <h3>Selecciona las columnas a descargar</h3>
      <div className="checkbox-container">
        <label>
          <input
            type="checkbox"
            name="first_name"
            checked={selectedColumns.first_name}
            onChange={handleColumnChange}
          />
          Nombre
        </label>
        <label>
          <input
            type="checkbox"
            name="last_name"
            checked={selectedColumns.last_name}
            onChange={handleColumnChange}
          />
          Apellido
        </label>
        <label>
          <input
            type="checkbox"
            name="city"
            checked={selectedColumns.city}
            onChange={handleColumnChange}
          />
          Ciudad
        </label>
        <label>
          <input
            type="checkbox"
            name="state"
            checked={selectedColumns.state}
            onChange={handleColumnChange}
          />
          Estado
        </label>
        <label>
          <input
            type="checkbox"
            name="email"
            checked={selectedColumns.email}
            onChange={handleColumnChange}
          />
          Email
        </label>
        <label>
          <input
            type="checkbox"
            name="phone"
            checked={selectedColumns.phone}
            onChange={handleColumnChange}
          />
          Teléfono
        </label>
        <label>
          <input
            type="checkbox"
            name="diseases"
            checked={selectedColumns.diseases}
            onChange={handleColumnChange}
          />
          Enfermedades
        </label>
        {/* Agregar más checkboxes según sea necesario */}
      </div>

      {/* Botón para descargar el archivo CSV */}
      {filteredPatientData.length > 0 && (
        <CSVLink
          data={filteredPatientData}
          filename={"patient_data.csv"}
          className="download-button"
        >
          Descargar datos seleccionados
        </CSVLink>
      )}
    </div>
  );
}

export default GraphDisplay;

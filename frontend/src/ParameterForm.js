import { useState } from "react";
import './ParameterForm.css';

function ParameterForm({setData}) {
  const [PacientesPorDia, setPacientesPorDia] = useState('');
  const [Dias, setDias] = useState('');
  const [param3, setParam3] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showModal, setShowModal] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true); 
    setShowModal(true);
    const pacientesPorDia = parseInt(PacientesPorDia, 10);

    if (isNaN(pacientesPorDia) || pacientesPorDia <= 0) {
      console.error('Por favor, ingresa un número válido de pacientes por día.');
      setLoading(false);
      setShowModal(false);
      return;
    }

    const parameters = {
      pacientes_por_dia: pacientesPorDia,
      dias: parseInt(Dias),
      parameter3: param3,
    };

    try {
      const response = await fetch('http://localhost:5001/run_simulation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(parameters),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Response:', data);
      setResult(data);  
      setData(data);
      setLoading(false);

    } catch (error) {
      console.error('Error al enviar parámetros:', error);
      setLoading(false); 
      setShowModal(false);
    }
  };

  const closeModal = () => {
    setShowModal(false);
    setResult(null); 
  };

  const estaciones = [
    { value: '91', label: 'Invierno' },
    { value: '182', label: 'Primavera' },
    { value: '273', label: 'Verano' },
    { value: '365', label: 'Otoño' },
  ];
  
  return (
    <div className="simulation-container">
      <div className="ParameterForm">
        <h2>Enviar parámetros</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="PacientesPorDia">Pacientes por día:</label>
            <input
              type="number"
              id="PacientesPorDia"
              value={PacientesPorDia}
              onChange={(e) => setPacientesPorDia(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor="Dias">La simulación recorre desde invierno hasta el otoño. Elige hasta que estación.</label>
            <select
              id="Dias"
              value={Dias}
              onChange={(e) => setDias(e.target.value)}
            >
              <option value="" disabled>Selecciona una estación</option>
              {estaciones.map((estacion) => (
                <option key={estacion.value} value={estacion.value}>
                  {estacion.label}
                </option>
              ))}
            </select>
          </div>
          <div>
            <label htmlFor="param3">Parámetro 3:</label>
            <input
              type="text"
              id="param3"
              value={param3}
              onChange={(e) => setParam3(e.target.value)}
            />
          </div>
          <button type="submit">Enviar</button>
        </form>
      </div>

      {showModal && (
        <div className="modal">
          <div className="modal-content">
            {loading ? (
              <div>
                <h3>Simulación en progreso...</h3>
                <p>Por favor, espera mientras procesamos los datos.</p>
              </div>
            ) : result ? (
              <div>
                <h3>Resultados de la Simulación</h3>
                <p>Días simulados: {result.days_simulated}</p>
                <p>Pacientes generados: {result.patients_generated}</p>
                <button onClick={closeModal}>Cerrar</button>
              </div>
            ) : (
              <div>
                <p>Hubo un error con la simulación. Inténtalo de nuevo.</p>
                <button onClick={closeModal}>Cerrar</button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default ParameterForm;

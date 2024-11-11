import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import ParameterForm from "./ParameterForm";
import UserManagementModal from "./UserManagementModal";
import GraphDisplay from "./GraphDisplay";
import './Simulation.css';

function Simulation() {
  const location = useLocation();
  const username = location.state?.username;
  const [userType, setUserType] = useState(null); // Guardamos el tipo de usuario aquí
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    fetch(`http://localhost:5000/user_type/${username}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Error al obtener el tipo de usuario');
        }
        return response.json(); // If the response is valid, parse it as JSON
      })
      .then((data) => {
        setUserType(data.user_type); // Set the user_type state
      })
      .catch((error) => {
        console.error('Error fetching user type:', error);
      });
  }, [username]);

  const handleOpenModal = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  return (
    <div className="simulation-container">
      <div className="parameter-graph-container">
      {userType && (userType !== "Alumno") && (
  <div className="button">
    <h3>Opciones</h3>
    <button onClick={handleOpenModal}>
      <p>Gestión de Usuarios</p>
    </button>
  </div>
)}

{userType && (userType !== "Profesor") && (
  <>
    <ParameterForm />
    <GraphDisplay />
  </>
)}

      </div>

      {isModalOpen && <UserManagementModal onClose={handleCloseModal} />}
    </div>
  );
}

export default Simulation;

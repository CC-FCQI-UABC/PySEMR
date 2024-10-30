import React, { useState } from "react";
import { useLocation } from "react-router-dom";
import ParameterForm from "./ParameterForm";
import UserManagementModal from "./UserManagementModal";
import './Simulation.css';

function Simulation() {
  const location = useLocation();
  const username = location.state?.username;
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleOpenModal = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  return (
    <div className="simulation-container">
      {username === "usuario1" && (
        <div className="button">
          <button onClick={handleOpenModal}>
            <p>Gestión de Usuarios</p>
          </button>
        </div>
      )}
      <ParameterForm />
      {isModalOpen && (
        <UserManagementModal onClose={handleCloseModal} />
      )}
    </div>
  );
}

export default Simulation;

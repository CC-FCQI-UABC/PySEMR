import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import ParameterForm from "./ParameterForm";
import UserManagementModal from "./UserManagementModal";
import GraphDisplay from "./GraphDisplay";
import io from "socket.io-client";  // Import socket.io-client
import './Simulation.css';

const socket = io("http://localhost:5002");  // Connect to the Flask WebSocket server

function Simulation() {
  const location = useLocation();
  const username = location.state?.username;
  const [userType, setUserType] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [data, setData] = useState([]);  // State to store seasonal data

  useEffect(() => {
    fetch(`http://localhost:5000/user_type/${username}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Error al obtener el tipo de usuario');
        }
        return response.json();
      })
      .then((data) => {
        setUserType(data.user_type);
      })
      .catch((error) => {
        console.error('Error fetching user type:', error);
      });

    // Listen for updates from the backend via WebSocket
    socket.on("update", (newData) => {
      setData(newData.season_counts);  // Update the state with the new data
    });

    return () => {
      socket.off("update");  // Cleanup the WebSocket listener on unmount
    };
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
            <ParameterForm setData={setData} />
            <GraphDisplay data={data} />
          </>
        )}
      </div>

      {isModalOpen && <UserManagementModal onClose={handleCloseModal} />}
    </div>
  );
}

export default Simulation;

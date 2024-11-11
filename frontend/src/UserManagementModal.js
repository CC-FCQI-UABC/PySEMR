import React, { useState, useEffect } from "react";
import './UserManagementModal.css'; // Estilos del modal

function UserManagementModal({ onClose }) {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({ username: "", password: "", user_type: "" });
  const [editingUser, setEditingUser] = useState(null);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await fetch("http://localhost:5000/users");
      const data = await response.json();
      setUsers(data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewUser((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (editingUser) {
      // Logic for updating an existing user can be added here
    } else {
      await createUser();
    }
  };

  const createUser = async () => {
    try {
      const response = await fetch("http://localhost:5000/users", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newUser),
      });

      if (response.ok) {
        fetchUsers(); // Refresh user list after creation
        setNewUser({ username: "", password: "", user_type: "" }); // Clear input fields
      } else {
        console.error("Failed to create user");
      }
    } catch (error) {
      console.error("Error creating user:", error);
    }
  };

  const handleDelete = async (userId) => {
    if (window.confirm("¿Estás seguro de que quieres eliminar este usuario?")) {
      try {
        const response = await fetch(`http://localhost:5000/users/${userId}`, {
          method: "DELETE",
        });
        if (response.ok) {
          fetchUsers(); // Refresh user list after deletion
        } else {
          console.error("Failed to delete user");
        }
      } catch (error) {
        console.error("Error deleting user:", error);
      }
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>Gestión de Usuarios</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="username"
            placeholder="Nombre de usuario"
            value={newUser.username}
            onChange={handleInputChange}
            required
          />
          <input
            type="text"
            name="password"
            placeholder="Contraseña"
            value={newUser.password}
            onChange={handleInputChange}
            required
          />
          <select
            name="user_type"
            value={newUser.user_type}
            onChange={handleInputChange}
            required
          >
            <option value="" disabled>Selecciona el tipo de usuario</option>
            <option value="Alumno">Alumno</option>
            <option value="Profesor">Profesor</option>
          </select>
          <button type="submit">{editingUser ? "Actualizar Usuario" : "Crear Usuario"}</button>
        </form>
        <div className="user-list-container">
        <h3>Lista de Usuarios</h3>
        <table>
  <thead>
    <tr>
      <th>Username</th>
      <th>User Type</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {users.map((user) => (
      <tr key={user.id} >
        <td >{user.username}</td>
        <td >{user.user_type}</td>
        <td>
          <button onClick={() => handleDelete(user.username)}>Eliminar</button>
        </td>
      </tr>
    ))}
  </tbody>
</table>

        </div>
        <button onClick={onClose}>Cerrar</button>
      </div>
    </div>
  );
}

export default UserManagementModal;

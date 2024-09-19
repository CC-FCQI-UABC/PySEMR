import { useState } from "react";
import './App.css';

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
      const data = await response.json();
      if (response.ok) {
        setIsLoggedIn(true); // Iniciar sesión correctamente
        setErrorMessage(""); // Limpiar el error
      } else {
        setErrorMessage(data.message); // Mostrar el error si no es ok
      }
    } catch (error) {
      setErrorMessage("Error al conectarse con el servidor.");
    }
  };

  return (
    <div className="App">
      {!isLoggedIn ? (
        <form onSubmit={handleSubmit}>
          <h2>Iniciar sesión</h2>
          <div>
            <label>Usuario:</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div>
            <label>Contraseña:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button type="submit">Login</button>
          {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
        </form>
      ) : (
        <h2>¡Bienvenido!</h2>
      )}
    </div>
  );
}

export default App;

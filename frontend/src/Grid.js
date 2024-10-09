import { useState, useEffect } from "react";
import './Grid.css';

function Grid() {
  const [grid, setGrid] = useState(createInitialGrid());

  // Función para crear la grilla inicial con pacientes sanos
  function createInitialGrid() {
    const rows = 10;
    const cols = 10;
    const initialGrid = [];
    for (let i = 0; i < rows; i++) {
      const row = [];
      for (let j = 0; j < cols; j++) {
        row.push({ infected: false });
      }
      initialGrid.push(row);
    }
    return initialGrid;
  }

  // Simulación de la infección
  useEffect(() => {
    const interval = setInterval(() => {
      setGrid((prevGrid) => {
        const newGrid = prevGrid.map((row) =>
          row.map((cell) =>
            cell.infected ? cell : Math.random() < 0.1 ? { infected: true } : cell
          )
        );
        return newGrid;
      });
    }, 1000); // Infectar cada segundo
    return () => clearInterval(interval); // Limpiar intervalo cuando el componente se desmonte
  }, []);

  return (
    <div className="Grid">
      <h2>Simulación de infección de pacientes</h2>
      <table>
        <tbody>
          {grid.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, colIndex) => (
                <td
                  key={colIndex}
                  style={{
                    width: "30px",
                    height: "30px",
                    backgroundColor: cell.infected ? "red" : "green",
                    border: "1px solid black",
                  }}
                ></td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Grid;

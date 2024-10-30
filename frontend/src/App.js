import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Login";
import Simulation from "./Simulation"; // Corrected import
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/simulation" element={<Simulation />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

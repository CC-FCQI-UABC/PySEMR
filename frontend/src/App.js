import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Login";
import Grid from "./Grid";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/grid" element={<Grid />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

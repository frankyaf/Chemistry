

/*
import logo from './logo.svg';
import './App.css';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
*/
import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [elementos, setElementos] = useState([]);

  useEffect(() => {
    axios.get("/api/elementos/") // relativo para que funcione en producción
      .then(res => setElementos(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Tabla Periódica</h1>
      <ul>
        {elementos.map(e => (
          <li key={e.atomic_number}>
            {e.atomic_number} - {e.symbol} ({e.name})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

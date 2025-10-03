import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import { Card } from './pages/Card';
import { Navigation } from './components/Navigation';
import { Board } from './components/Board';

function App(){
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/Card" element={<Card/>} />
        <Route path="/Game" element={<Card/>} />
      </Routes>
      <div className="flex h-screen items-center justify-center bg-gray-900">
        <h1 className="text-white text-4xl font-bold">¡Hola con Tailwind!</h1>
      </div>
      <Board />
    </BrowserRouter>
    
  )
}

export default App
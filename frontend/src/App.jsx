import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Card } from "./pages/Card";
import { Navigation } from './components/Navigation';

function App(){
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/Card" element={<Card/>} />
        <Route path="/Game" element={<Card/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
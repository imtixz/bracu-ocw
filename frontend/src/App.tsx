import { Routes, Route } from "react-router";
import Home from "./pages/Home";
import Details from "./pages/Details";

function App() {

  return (
    <Routes>
      <Route path="/" element={<Home />}/>
      <Route path="/details" element={<Details />}/>
    </Routes>
  )
}

export default App

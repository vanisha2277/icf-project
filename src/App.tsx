import { Routes, Route } from "react-router-dom";

import LandingPage from "./components/LandingPage/LandingPage";
import Preferences from "./components/Preferences/preferences";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/preferences" element={<Preferences />} />
    </Routes>
  );
}

export default App;

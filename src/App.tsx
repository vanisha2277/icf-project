import { Routes, Route } from "react-router-dom";

import LandingPage from "./components/LandingPage/LandingPage";
import Preferences from "./components/Preferences/preferences";
import ReadingMode from "./components/ReadingMode/ReadingMode";
import Vocabulary from "./components/Vocabulary/vocabulary";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/preferences" element={<Preferences />} />
      <Route path="/reading-mode" element={<ReadingMode />} />
      <Route path="/vocabulary" element={<Vocabulary />} />
    </Routes>
  );
}

export default App;
import { Routes, Route } from "react-router-dom";

import LandingPage from "./components/LandingPage/LandingPage";
import Preferences from "./components/Preferences/preferences";
import ReadingMode from "./components/ReadingMode/ReadingMode";
import Vocabulary from "./components/Vocabulary/vocabulary";
import Math from "./components/Math/math";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/preferences" element={<Preferences />} />
      <Route path="/reading-mode" element={<ReadingMode />} />
      <Route path="/vocabulary" element={<Vocabulary />} />
      <Route path = "/math-mode" element ={<Math/>}/>
    </Routes>
  );
}

export default App;
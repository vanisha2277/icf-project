import { Routes, Route } from "react-router-dom";

import LandingPage from "./components/LandingPage/LandingPage";
import Preferences from "./components/Preferences/preferences";
import ReadingMode from "./components/ReadingMode/ReadingMode";
import Vocabulary from "./components/Vocabulary/vocabulary";
import Math from "./components/Math/math";
import KeyIdeas from "./components/Key-Ideas/key_ideas";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/preferences" element={<Preferences />} />
      <Route path="/reading-mode" element={<ReadingMode />} />
      <Route path="/vocabulary" element={<Vocabulary />} />
      <Route path = "/math-mode" element ={<Math/>}/>
      <Route path = "/key_ideas" element = {<KeyIdeas/>}/>
    </Routes>
  );
}

export default App;
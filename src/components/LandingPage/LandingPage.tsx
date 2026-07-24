import { useNavigate } from "react-router-dom";
import "./LandingPage.css";


function LandingPage() {
    const navigate = useNavigate();
  return (
    <main className="landing-page">

      <section className="hero">

        <div className="logo-circle">
          🌱
        </div> 

        <h1>Welcome</h1>  

        <h2>
          Learn in the way that works best for you.
        </h2>

        <p className="description">
          Reading support that adapts educational content
          to your learning needs through accessible,
          personalized learning tools.
        </p>

        <button 
        className="primary-button"
        onClick = { () => navigate("/preferences")}
       >
          Get Started
        </button>

      </section>

      <section className="features">

        <div className="feature-card">
          <span>📖</span>
          <h3>Make Reading Easier</h3>
          <p>
            Simplify educational text while preserving meaning.
          </p>
        </div>

        <div className="feature-card">
          <span>💬</span>
          <h3>Explain Difficult Words</h3>
          <p>
            Receive simple explanations for unfamiliar vocabulary.
          </p>
        </div>

        <div className="feature-card">
          <span>✨</span>
          <h3>Highlight Key Ideas</h3>
          <p>
            Quickly identify the most important concepts.
          </p>
        </div>

        <div className="feature-card">
          <span>➗</span>
          <h3>Math Support</h3>
          <p>
            Break down equations into easy-to-follow steps.
          </p>
        </div>

      </section>

    </main>
  );
}

export default LandingPage;

import "./LandingPage.css";

function LandingPage() {
  return (
    <main className="landing-page">
      <div className="hero">
        <h1>AdaptEd</h1>
        <p className="tagline">
          Personalized learning for every student.
        </p>

        <p className="description">
          Make educational content more accessible by simplifying text,
          explaining difficult vocabulary, and adapting information to your
          learning needs.
        </p>

        <button className="start-button">
          Get Started
        </button>
      </div>

      <section className="features">
        <div className="feature-card">
          <h3>📖 Simplify</h3>
          <p>Rewrite complex educational text into clear, readable language.</p>
        </div>

        <div className="feature-card">
          <h3>📝 Explain</h3>
          <p>Define difficult vocabulary with simple, student-friendly explanations.</p>
        </div>

        <div className="feature-card">
          <h3>⭐ Summarize</h3>
          <p>Highlight the key ideas so students can focus on what matters most.</p>
        </div>

        <div className="feature-card">
          <h3>♿ Accessibility</h3>
          <p>Adapt content to support different learning styles and accessibility needs.</p>
        </div>
      </section>
    </main>
  );
}

export default LandingPage;

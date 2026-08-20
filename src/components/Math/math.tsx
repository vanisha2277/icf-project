import { useNavigate } from "react-router-dom";
import "./Math.css";

function MathMode() {
  const navigate = useNavigate();

  return (
    <main className="math-page">
      <header className="math-header">
        <div>
          <p className="eyebrow">Math Support</p>
          <h1>Let's break this problem down.</h1>
        </div>

        <button
          className="secondary-button"
          onClick={() => navigate("/preferences")}
        >
          Back to Preferences
        </button>
      </header>

      <section className="math-layout">

        <article className="problem-card">
          <p className="subject">Algebra</p>

          <h2>Solve for x</h2>

          <div className="problem">
            3x + 6 = 18
          </div>

          <p className="instruction">
            Work through each step to find the value of x.
          </p>
        </article>

        <aside className="steps-card">
          <p className="eyebrow">Step-by-Step</p>

          <h2>Let's solve it together.</h2>

          <div className="math-step">
            <span className="step-number">1</span>

            <div>
              <h3>Subtract 6 from both sides</h3>
              <p>
                We want to get the number 6 away from x.
              </p>

              <div className="equation">
                3x + 6 - 6 = 18 - 6
              </div>
            </div>
          </div>

          <div className="math-step">
            <span className="step-number">2</span>

            <div>
              <h3>Simplify</h3>
              <p>
                The two 6s on the left cancel each other out.
              </p>

              <div className="equation">
                3x = 12
              </div>
            </div>
          </div>

          <div className="math-step">
            <span className="step-number">3</span>

            <div>
              <h3>Divide by 3</h3>
              <p>
                Divide both sides by 3 to find x.
              </p>

              <div className="equation">
                x = 4
              </div>
            </div>
          </div>

          <div className="answer">
            <span>✓</span>
            <div>
              <strong>Answer</strong>
              <p>x = 4</p>
            </div>
          </div>
        </aside>

      </section>
    </main>
  );
}

export default MathMode;
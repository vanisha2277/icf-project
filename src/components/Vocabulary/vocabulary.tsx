import { useNavigate } from "react-router-dom";
import "./vocabulary.css";

function Vocabulary() {
  const navigate = useNavigate();

  return (
    <main className="vocabulary-page">
      <header className="vocabulary-header">
        <div>
          <p className="eyebrow">Vocabulary Support</p>
          <h1>Let's make difficult words easier to understand.</h1>
        </div>

        <button
          className="secondary-button"
          onClick={() => navigate("/preferences")}
        >
          Back to Preferences
        </button>
      </header>

      <section className="vocabulary-layout">

        <article className="vocabulary-content">
          <p className="subject">Biology</p>

          <h2>Understanding Photosynthesis</h2>

          <p>
            Photosynthesis is a biochemical process used by plants,
            algae, and some bacteria to convert light energy into
            chemical energy.
          </p>

          <p>
            During photosynthesis, plants absorb light energy using
            pigments such as chlorophyll. They use this energy to
            transform carbon dioxide and water into glucose.
          </p>

          <p>
            Oxygen is produced as a byproduct of this process and
            is released into the atmosphere.
          </p>
        </article>

        <aside className="word-explanation">
          <p className="eyebrow">Word Helper</p>

          <h2>Select a word</h2>

          <p>
            Select a difficult word from the reading to see
            an easy-to-understand explanation.
          </p>

          <div className="word-placeholder">
            <span>💡</span>
            <p>
              Your explanation will appear here.
            </p>
          </div>
        </aside>

      </section>
    </main>
  );
}

export default Vocabulary;
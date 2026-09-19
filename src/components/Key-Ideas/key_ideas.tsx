import { useNavigate} from "react-router-dom";
import "./key_ideas.css";

function KeyIdeas() {
  const navigate = useNavigate();

  return (
    <div className="key-ideas-page">
      <header className="key-ideas-header">
        <div>
          <p className="key-ideas-eyebrow">KEY IDEAS</p>
          <h1>Let's focus on what's important.</h1>
          <p className="key-ideas-subtitle">
            Identify the most important information without losing the context.
          </p>
        </div>

        <button
          className="back-button"
          onClick={() => navigate("/preferences")}
        >
          ← Back to Preferences
        </button>
      </header>

      <main className="key-ideas-content">
        {/* Original Content */}
        <section className="original-card">
          <div className="card-heading">
            <div>
              <p className="card-label">ORIGINAL CONTENT</p>
              <h2>Understanding Photosynthesis</h2>
            </div>
          </div>

          <div className="article-text">
            <p>
              Photosynthesis is the process that plants use to make their own
              food. Plants use energy from sunlight to convert carbon dioxide
              and water into glucose, a type of sugar that provides energy.
            </p>

            <p>
              Chlorophyll, the green pigment found in plant cells, absorbs
              sunlight and helps provide the energy needed for photosynthesis.
              Most chlorophyll is found inside structures called chloroplasts.
            </p>

            <p>
              During photosynthesis, plants take in carbon dioxide from the air
              and water from the soil. These materials are used to produce
              glucose. Oxygen is released as a byproduct and enters the
              atmosphere.
            </p>

            <p>
              Photosynthesis is important because it provides plants with
              energy and produces oxygen that many organisms need to survive.
            </p>
          </div>
        </section>

        {/* Key Ideas */}
        <section className="key-ideas-card">
          <div className="card-heading">
            <div>
              <p className="card-label">KEY IDEAS</p>
              <h2>What should I remember?</h2>
            </div>

            <span className="sparkle">✨</span>
          </div>

          <div className="ideas-list">
            <div className="idea">
              <div className="idea-number">1</div>

              <div className="idea-content">
                <h3>Plants make their own food.</h3>
                <p>
                  Photosynthesis allows plants to use sunlight to create
                  glucose, which provides energy.
                </p>
              </div>
            </div>

            <div className="idea">
              <div className="idea-number">2</div>

              <div className="idea-content">
                <h3>Sunlight provides the energy.</h3>
                <p>
                  Chlorophyll absorbs sunlight and helps power the process of
                  photosynthesis.
                </p>
              </div>
            </div>

            <div className="idea">
              <div className="idea-number">3</div>

              <div className="idea-content">
                <h3>Plants use carbon dioxide and water.</h3>
                <p>
                  These materials are combined during photosynthesis to produce
                  glucose.
                </p>
              </div>
            </div>

            <div className="idea">
              <div className="idea-number">4</div>

              <div className="idea-content">
                <h3>Oxygen is released.</h3>
                <p>
                  Oxygen is produced as a byproduct of photosynthesis and is
                  released into the atmosphere.
                </p>
              </div>
            </div>
          </div>

          <button className="context-button">
            Show Context
          </button>
        </section>
      </main>
    </div>
  );
}

export default KeyIdeas;
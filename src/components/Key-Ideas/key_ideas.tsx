import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./key_ideas.css";

type Idea = {
  id: number;
  title: string;
  explanation: string;
  paragraph: number;
};

const ideas: Idea[] = [
  {
    id: 1,
    title: "Plants make their own food.",
    explanation:
      "Photosynthesis allows plants to use sunlight to create glucose, which provides energy.",
    paragraph: 1,
  },
  {
    id: 2,
    title: "Sunlight provides the energy.",
    explanation:
      "Chlorophyll absorbs sunlight and helps power the process of photosynthesis.",
    paragraph: 2,
  },
  {
    id: 3,
    title: "Plants use carbon dioxide and water.",
    explanation:
      "These materials are combined during photosynthesis to produce glucose.",
    paragraph: 3,
  },
  {
    id: 4,
    title: "Oxygen is released.",
    explanation:
      "Oxygen is produced as a byproduct of photosynthesis and is released into the atmosphere.",
    paragraph: 3,
  },
];

function KeyIdeas() {
  const navigate = useNavigate();

  const [selectedIdea, setSelectedIdea] = useState<number | null>(null);
  const [showContext, setShowContext] = useState(false);

  const handleIdeaClick = (ideaId: number) => {
    setSelectedIdea((current) =>
      current === ideaId ? null : ideaId
    );
  };

  const getParagraphClass = (paragraphNumber: number) => {
    if (selectedIdea === null) {
      return "";
    }

    const selected = ideas.find(
      (idea) => idea.id === selectedIdea
    );

    if (selected?.paragraph === paragraphNumber) {
      return "highlighted-paragraph";
    }

    return "dimmed-paragraph";
  };

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
          Exit Key Ideas
        </button>
      </header>

      <main className="key-ideas-content">
        {/* ORIGINAL CONTENT */}
        <section className="original-card">
          <div className="card-heading">
            <div>
              <p className="card-label">ORIGINAL CONTENT</p>

              <h2>Understanding Photosynthesis</h2>
            </div>
          </div>

          <div className="article-text">
            <p className={getParagraphClass(1)}>
              Photosynthesis is the process that plants use to make their own
              food. Plants use energy from sunlight to convert carbon dioxide
              and water into glucose, a type of sugar that provides energy.
            </p>

            <p className={getParagraphClass(2)}>
              Chlorophyll, the green pigment found in plant cells, absorbs
              sunlight and helps provide the energy needed for photosynthesis.
              Most chlorophyll is found inside structures called chloroplasts.
            </p>

            <p className={getParagraphClass(3)}>
              During photosynthesis, plants take in carbon dioxide from the air
              and water from the soil. These materials are used to produce
              glucose. Oxygen is released as a byproduct and enters the
              atmosphere.
            </p>

            <p className={getParagraphClass(4)}>
              Photosynthesis is important because it provides plants with
              energy and produces oxygen that many organisms need to survive.
            </p>
          </div>

          {selectedIdea !== null && (
            <div className="selected-message">
              <strong>
                Idea {selectedIdea} is highlighted in the original content.
              </strong>

              <button
                type="button"
                onClick={() => setSelectedIdea(null)}
              >
                Clear highlight
              </button>
            </div>
          )}
        </section>

        {/* KEY IDEAS */}
        <section className="key-ideas-card">
          <div className="card-heading">
            <div>
              <p className="card-label">KEY IDEAS</p>

              <h2>What should I remember?</h2>
            </div>

            <span className="sparkle">✨</span>
          </div>

          <p className="instruction-text">
            Select an idea to see where it appears in the original content.
          </p>

          <div className="ideas-list">
            {ideas.map((idea) => (
              <button
                key={idea.id}
                type="button"
                className={`idea ${
                  selectedIdea === idea.id
                    ? "selected-idea"
                    : ""
                }`}
                onClick={() => handleIdeaClick(idea.id)}
                aria-pressed={selectedIdea === idea.id}
              >
                <div className="idea-number">
                  {idea.id}
                </div>

                <div className="idea-content">
                  <h3>{idea.title}</h3>

                  <p>{idea.explanation}</p>

                  {selectedIdea === idea.id && (
                    <span className="idea-status">
                      ✓ Showing related context
                    </span>
                  )}
                </div>
              </button>
            ))}
          </div>

          {/* SHOW CONTEXT */}
          <button
            type="button"
            className="context-button"
            onClick={() =>
              setShowContext((current) => !current)
            }
            aria-expanded={showContext}
          >
            {showContext ? "Hide Context" : "Show Context"}
          </button>

          {showContext && (
            <div className="context-box">
              <h3>Why this helps</h3>

              <p>
                Key Ideas brings the most important information forward
                while keeping the original material available for reference.
              </p>

              <p>
                This can help reduce cognitive load and make dense educational
                content easier to process.
              </p>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default KeyIdeas;
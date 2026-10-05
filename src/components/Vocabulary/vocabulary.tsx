import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./vocabulary.css";

type VocabularyWord = {
  word: string;
  definition: string;
  example: string;
};

const vocabularyWords: VocabularyWord[] = [
  {
    word: "biochemical",
    definition:
      "A process that happens inside a living organism using chemical reactions.",
    example:
      "Photosynthesis is biochemical because it uses chemical reactions inside plant cells.",
  },
  {
    word: "pigments",
    definition:
      "Natural substances that give something its color and can absorb certain types of light.",
    example:
      "Chlorophyll is a pigment that gives plants their green color.",
  },
  {
    word: "chlorophyll",
    definition:
      "A green pigment in plants that absorbs light energy for photosynthesis.",
    example:
      "Chlorophyll helps a plant capture energy from sunlight.",
  },
  {
    word: "byproduct",
    definition:
      "A substance that is produced as a result of another process.",
    example:
      "Oxygen is a byproduct of photosynthesis.",
  },
];

function Vocabulary() {
  const navigate = useNavigate();

  const [selectedWord, setSelectedWord] =
    useState<VocabularyWord | null>(null);

  const handleWordClick = (word: VocabularyWord) => {
    setSelectedWord((current) =>
      current?.word === word.word ? null : word
    );
  };

  return (
    <main className="vocabulary-page">
      <header className="vocabulary-header">
        <div>
          <p className="eyebrow">Vocabulary Support</p>

          <h1>
            Let's make difficult words easier to understand.
          </h1>

          <p className="vocabulary-subtitle">
            Select a word from the reading to see a simpler explanation.
          </p>
        </div>

        <button
          className="back-button"
          onClick={() => navigate("/preferences")}
        >
          Exit Vocab
        </button>
      </header>

      <section className="vocabulary-layout">

        {/* READING CONTENT */}
        <article className="vocabulary-content">
          <p className="subject">Biology</p>

          <h2>Understanding Photosynthesis</h2>

          <p>
            Photosynthesis is a{" "}
            <button
              className={`vocab-word ${
                selectedWord?.word === "biochemical"
                  ? "selected-word"
                  : ""
              }`}
              onClick={() =>
                handleWordClick(vocabularyWords[0])
              }
            >
              biochemical
            </button>{" "}
            process used by plants, algae, and some bacteria to
            convert light energy into chemical energy.
          </p>

          <p>
            During photosynthesis, plants absorb light energy
            using{" "}
            <button
              className={`vocab-word ${
                selectedWord?.word === "pigments"
                  ? "selected-word"
                  : ""
              }`}
              onClick={() =>
                handleWordClick(vocabularyWords[1])
              }
            >
              pigments
            </button>{" "}
            such as{" "}
            <button
              className={`vocab-word ${
                selectedWord?.word === "chlorophyll"
                  ? "selected-word"
                  : ""
              }`}
              onClick={() =>
                handleWordClick(vocabularyWords[2])
              }
            >
              chlorophyll
            </button>
            . They use this energy to transform carbon dioxide
            and water into glucose.
          </p>

          <p>
            Oxygen is produced as a{" "}
            <button
              className={`vocab-word ${
                selectedWord?.word === "byproduct"
                  ? "selected-word"
                  : ""
              }`}
              onClick={() =>
                handleWordClick(vocabularyWords[3])
              }
            >
              byproduct
            </button>{" "}
            of this process and is released into the atmosphere.
          </p>

          <p className="reading-hint">
            💡 Click any highlighted word to learn what it means.
          </p>
        </article>


        {/* WORD EXPLANATION */}
        <aside className="word-explanation">
          <p className="eyebrow">Word Helper</p>

          {!selectedWord ? (
            <>
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
            </>
          ) : (
            <>
              <p className="selected-word-label">
                SELECTED WORD
              </p>

              <h2>{selectedWord.word}</h2>

              <div className="definition-box">
                <h3>In simple terms</h3>

                <p>
                  {selectedWord.definition}
                </p>
              </div>

              <div className="example-box">
                <h3>Example</h3>

                <p>
                  {selectedWord.example}
                </p>
              </div>

              <button
                className="clear-word-button"
                onClick={() => setSelectedWord(null)}
              >
                Choose another word
              </button>
            </>
          )}
        </aside>

      </section>
    </main>
  );
}

export default Vocabulary;
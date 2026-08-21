// ICF 2026 AI disclosure: built with AI assistance.
import "./ReadingMode.css";
import { useNavigate } from "react-router-dom";
import { useEffect, useRef, useState } from "react";
import {
  transformText,
  type TransformChunk,
  type WordTiming,
} from "../../services/api";

const DEFAULT_TEXT = `Photosynthesis is a biochemical process used by plants,
algae, and some bacteria to convert light energy into
chemical energy. This process allows organisms to create
the energy they need to survive and grow.

During photosynthesis, plants absorb light energy using
pigments such as chlorophyll. They use this energy to
transform carbon dioxide and water into glucose, a type
of sugar that stores chemical energy.

Oxygen is produced as a byproduct of this process and is
released into the atmosphere. Photosynthesis is therefore
important not only for plants, but also for many other
organisms that depend on oxygen and plants for survival.`;

// Escapes everything, then selectively restores only the <b>/</b> tags the
// backend's bionic transform inserts, so user-supplied text can never smuggle
// in arbitrary HTML through dangerouslySetInnerHTML.
function sanitizeBionicHtml(html: string): string {
  const div = document.createElement("div");
  div.textContent = html;
  return div.innerHTML.replace(/&lt;b&gt;/g, "<b>").replace(/&lt;\/b&gt;/g, "</b>");
}

interface FlatWord {
  key: string;
  word: string;
  startMs: number;
  endMs: number;
}

function flattenTimings(chunks: TransformChunk[]): FlatWord[] {
  const flat: FlatWord[] = [];
  let offsetMs = 0;

  chunks.forEach((chunk, chunkIndex) => {
    const timings: WordTiming[] = chunk.word_timings ?? [];
    let chunkMaxEnd = 0;

    timings.forEach((timing, wordIndex) => {
      flat.push({
        key: `${chunkIndex}-${wordIndex}`,
        word: timing.word,
        startMs: offsetMs + timing.start_ms,
        endMs: offsetMs + timing.end_ms,
      });
      chunkMaxEnd = Math.max(chunkMaxEnd, timing.end_ms);
    });

    offsetMs += chunkMaxEnd + 200;
  });

  return flat;
}

function ReadingMode() {
  const navigate = useNavigate();

  const [text, setText] = useState(DEFAULT_TEXT);
  const [bionic, setBionic] = useState(false);
  const [chunking, setChunking] = useState(false);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [chunks, setChunks] = useState<TransformChunk[] | null>(null);

  const [speaking, setSpeaking] = useState(false);
  const [activeWordKey, setActiveWordKey] = useState<string | null>(null);
  const timeoutIdsRef = useRef<number[]>([]);

  const stopSpeaking = () => {
    window.speechSynthesis.cancel();
    timeoutIdsRef.current.forEach((id) => window.clearTimeout(id));
    timeoutIdsRef.current = [];
    setSpeaking(false);
    setActiveWordKey(null);
  };

  useEffect(() => stopSpeaking, []);

  const handleApply = async () => {
    stopSpeaking();
    setLoading(true);
    setError(null);
    try {
      const result = await transformText(text, {
        bionic,
        chunking,
        tts_sync: false,
      });
      setChunks(result.chunks);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  const handleReadAloud = async () => {
    if (speaking) {
      stopSpeaking();
      return;
    }

    setLoading(true);
    setError(null);
    try {
      const result = await transformText(text, {
        bionic,
        chunking,
        tts_sync: true,
      });
      setChunks(result.chunks);

      const spokenText = result.chunks.map((c) => c.text).join(" ");
      const flatWords = flattenTimings(result.chunks);

      const utterance = new SpeechSynthesisUtterance(spokenText);
      utterance.onend = stopSpeaking;
      utterance.onerror = stopSpeaking;

      timeoutIdsRef.current = flatWords.map((w) =>
        window.setTimeout(() => setActiveWordKey(w.key), w.startMs),
      );
      const lastWord = flatWords[flatWords.length - 1];
      if (lastWord) {
        timeoutIdsRef.current.push(
          window.setTimeout(() => setActiveWordKey(null), lastWord.endMs),
        );
      }

      setSpeaking(true);
      window.speechSynthesis.speak(utterance);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  const renderChunk = (chunk: TransformChunk, chunkIndex: number) => {
    if (chunk.word_timings && chunk.word_timings.length > 0) {
      return (
        <p key={chunkIndex}>
          {chunk.word_timings.map((timing, wordIndex) => {
            const key = `${chunkIndex}-${wordIndex}`;
            return (
              <span
                key={key}
                className={key === activeWordKey ? "read-word active" : "read-word"}
              >
                {timing.word}{" "}
              </span>
            );
          })}
        </p>
      );
    }

    if (chunk.bionic_html) {
      return (
        <p
          key={chunkIndex}
          dangerouslySetInnerHTML={{ __html: sanitizeBionicHtml(chunk.bionic_html) }}
        />
      );
    }

    return <p key={chunkIndex}>{chunk.text}</p>;
  };

  return (
    <main className="reading-page">
      <header className="reading-header">
        <div>
          <p className="eyebrow">Reading Mode</p>
          <h1>Let's make this easier to read.</h1>
        </div>

        <button
          className="secondary-button"
          onClick={() => {
            stopSpeaking();
            navigate("/preferences");
          }}
        >
          Exit Reading Mode
        </button>
      </header>

      <section className="reading-layout">
        <aside className="reading-controls">
          <h2>Reading Settings</h2>

          <label className="setting">
            <input type="checkbox" />
            <span>Large Text</span>
          </label>

          <label className="setting">
            <input type="checkbox" />
            <span>Increased Spacing</span>
          </label>

          <label className="setting">
            <input
              type="checkbox"
              checked={bionic}
              onChange={(e) => setBionic(e.target.checked)}
            />
            <span>Bionic Reading</span>
          </label>

          <label className="setting">
            <input
              type="checkbox"
              checked={chunking}
              onChange={(e) => setChunking(e.target.checked)}
            />
            <span>Reading Overlay</span>
          </label>

          <textarea
            className="reading-textarea"
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows={8}
          />

          <button className="listen-button" onClick={handleApply} disabled={loading}>
            {loading && !speaking ? "Applying…" : "Apply Settings"}
          </button>

          <button className="listen-button" onClick={handleReadAloud} disabled={loading}>
            {speaking ? "⏸ Stop" : "🔊 Read Aloud"}
          </button>
        </aside>

        <article className="reading-content">
          <p className="subject">Biology</p>
          <h2>Understanding Photosynthesis</h2>

          {error && <p className="read-error">{error}</p>}

          {chunks
            ? chunks.map((chunk, i) => renderChunk(chunk, i))
            : text.split(/\n\s*\n/).map((para, i) => <p key={i}>{para}</p>)}
        </article>
      </section>
    </main>
  );
}

export default ReadingMode;

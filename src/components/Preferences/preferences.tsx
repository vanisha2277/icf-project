import { useNavigate } from "react-router-dom";
import "./Preferences.css";

const options = [
  {
    icon: "📖",
    title: "Make Reading Easier",
    description:
      "Simplify complex sentences while keeping the original meaning.",
    path: "/reading-mode",
  },
  {
    icon: "💬",
    title: "Explain Difficult Words",
    description:
      "Get simple definitions for unfamiliar vocabulary.",
  },
  {
    icon: "✨",
    title: "Highlight Key Ideas",
    description:
      "Focus on the most important information.",
  },
  {
    icon: "🔊",
    title: "Listen Along",
    description:
      "Hear text read aloud with reading support.",
  },
  {
    icon: "➗",
    title: "Step-by-Step Math",
    description:
      "Break down problems into smaller steps.",
  },
];

function Preferences() {
  const navigate = useNavigate();

  return (
    <main className="preferences-page">
      <section className="preferences-header">
        <h1>How do you learn best?</h1>

        <p>
          Choose what helps you understand information more easily.
        </p>
      </section>

      <section className="preference-grid">
        {options.map((option) => (
          <div
            className="preference-card"
            key={option.title}
            onClick={() => {
              if (option.path) {
                navigate(option.path);
              }
            }}
            role={option.path ? "button" : undefined}
            tabIndex={option.path ? 0 : undefined}
          >
            <span>{option.icon}</span>

            <h2>{option.title}</h2>

            <p>{option.description}</p>
          </div>
        ))}
      </section>
    </main>
  );
}

export default Preferences;
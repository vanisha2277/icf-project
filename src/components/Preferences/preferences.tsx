import "./Preferences.css";

const options = [
  {
    icon: "📖",
    title: "Make Reading Easier",
    description:
      "Simplify complex sentences while keeping the original meaning."
  },
  {
    icon: "💬",
    title: "Explain Difficult Words",
    description:
      "Get simple definitions for unfamiliar vocabulary."
  },
  {
    icon: "✨",
    title: "Highlight Key Ideas",
    description:
      "Focus on the most important information."
  },
  {
    icon: "➗",
    title: "Step-by-Step Math",
    description:
      "Break down problems into smaller steps."
  }
];

function Preferences() {
  return (
    <main className="preferences-page">

      <section className="preferences-header">
        <h1>How do you learn best?</h1>

        <p>
          Choose what helps you understand information
          more easily.
        </p>
      </section>


      <section className="preference-grid">

        {options.map((option) => (
          <div className="preference-card" key={option.title}>

            <span>
              {option.icon}
            </span>

            <h2>
              {option.title}
            </h2>

            <p>
              {option.description}
            </p>

          </div>
        ))}

      </section>


      <button className="primary-button">
        Continue
      </button>

    </main>
  );
}

export default Preferences;
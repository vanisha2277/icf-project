import "./ReadingMode.css";

function ReadingMode() {
  return (
    <main className="reading-page">
      <header className="reading-header">
        <div>
          <p className="eyebrow">Reading Mode</p>
          <h1>Let's make this easier to read.</h1>
        </div>

        <button className="secondary-button">
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
            <input type="checkbox" />
            <span>Bionic Reading</span>
          </label>

          <label className="setting">
            <input type="checkbox" />
            <span>Reading Overlay</span>
          </label>

          <button className="listen-button">
            🔊 Read Aloud
          </button>
        </aside>

        <article className="reading-content">
          <p className="subject">Biology</p>

          <h2>Understanding Photosynthesis</h2>

          <p>
            Photosynthesis is a biochemical process used by plants,
            algae, and some bacteria to convert light energy into
            chemical energy. This process allows organisms to create
            the energy they need to survive and grow.
          </p>

          <p>
            During photosynthesis, plants absorb light energy using
            pigments such as chlorophyll. They use this energy to
            transform carbon dioxide and water into glucose, a type
            of sugar that stores chemical energy.
          </p>

          <p>
            Oxygen is produced as a byproduct of this process and is
            released into the atmosphere. Photosynthesis is therefore
            important not only for plants, but also for many other
            organisms that depend on oxygen and plants for survival.
          </p>
        </article>

      </section>
    </main>
  );
}

export default ReadingMode;
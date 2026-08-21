# ICF 2026 — Accessibility Reading Tool

AI disclosure: parts of this project were built with AI assistance.

## Problem & target users

Reading support for students who benefit from bionic reading, chunked text, and
synced text-to-speech (e.g. dyslexia, ADHD, or other processing differences).

## What's fully working end-to-end right now

- **Backend** (`backend/`): a real, tested FastAPI service. `POST /transform`
  takes `{ text, options: { bionic, chunking, tts_sync } }` and returns
  `{ chunks: [{ text, bionic_html, word_timings }] }`. Bionic bolding and
  sentence-based chunking are deterministic; TTS word timings fall back to a
  synthetic generator when no AI provider is configured. 12/12 backend tests
  pass (see Testing below).
- **Reading Mode** (`/reading-mode`) is wired to the real backend:
  - A textarea (pre-filled with a sample paragraph) lets you paste/edit text.
  - **Bionic Reading** and **Reading Overlay** checkboxes map to the backend's
    `bionic` and `chunking` options respectively. **Large Text** and
    **Increased Spacing** are still visual-only placeholders — no logic is
    wired to them yet.
  - **Apply Settings** sends the current text + options to `POST /transform`
    and renders the real returned chunks (sanitized bionic HTML, or plain
    chunked text) in place of the original hardcoded paragraph.
  - **Read Aloud** requests `tts_sync: true`, then uses the browser's
    `speechSynthesis` API to read the text aloud while highlighting the
    currently-spoken word using the backend's `word_timings`.
  - Loading and error states are inline text within the existing layout (no
    new modals/toasts). If the backend isn't running, you'll see a clear
    "Could not reach the backend..." message instead of a crash or blank page.

## What's stubbed / not yet connected

- **Math mode** (`/math-mode`) is still a fully static mockup (one hardcoded
  algebra problem). The backend has **no math transformation logic at all**,
  so this was intentionally left untouched rather than inventing new backend
  behavior. Wiring it is a separate task once a math endpoint exists.
- **Vocabulary** (`/vocabulary`) is still a static mockup — no word-lookup
  logic or backend endpoint exists for it.
- **Preferences** (`/preferences`) is a navigation menu to the other pages,
  not a settings form — there's no shared/global preferences state. Each
  page's options (currently just Reading Mode's) are local to that page.
- **Chrome extension packaging is incomplete.** There is no `manifest.json`
  and `@crxjs/vite-plugin` (already a devDependency) is not wired into
  `vite.config.ts`. There's also no content-script code to extract text from
  a web page — `src/background/extension` is an empty placeholder. Today this
  runs as a plain web app via `npm run dev`, not a loadable unpacked
  extension. Building the actual extension shell is future work.
- **Dev-only CORS opening:** `backend/main.py` originally only allowed
  `chrome-extension://*` origins (correct for a shipped extension, but it
  blocks a plain browser tab talking to the backend). `http://localhost:5173`
  / `127.0.0.1:5173` were added to the allowed origins specifically so the
  current web-app version can be tested against the real backend during
  development. Revisit this once the extension is actually packaged.

## Run instructions

You need both the backend and frontend running together.

### 1. Backend (FastAPI)

```bash
cd backend
python -m venv venv        # if not already created
source venv/bin/activate
pip install -r requirements.txt
cd ..
uvicorn backend.main:app --reload --port 8000
```

Verify it's up: `curl http://localhost:8000/health` → `{"status":"ok"}`

### 2. Frontend (Vite dev server)

```bash
npm install
npm run dev
```

Open the printed URL (typically `http://localhost:5173`) and navigate to
**Preferences → Make Reading Easier** (or go directly to `/reading-mode`).

### 3. Try it

1. Edit the text in the textarea (or leave the sample paragraph).
2. Toggle **Bionic Reading** and/or **Reading Overlay**.
3. Click **Apply Settings** to see the real transformed output.
4. Click **🔊 Read Aloud** to hear it spoken with word-by-word highlighting.
5. Stop the backend and click **Apply Settings** again to see the graceful
   error state.

Note: this validates the app as a normal web page, not as a loaded Chrome
extension — see the packaging gap above.

## Testing

```bash
# Backend unit tests (run from repo root; PYTHONPATH is required on this
# pytest version so `backend` resolves as a package)
source backend/venv/bin/activate
PYTHONPATH=. pytest backend/tests

# Frontend build + lint
npm run build
npm run lint
```

## Limitations / next steps

- Math mode and Vocabulary need their own backend endpoints before they can
  be wired up.
- No shared preferences state across pages yet — Preferences doesn't hold
  reusable bionic/chunking/tts settings today.
- No Chrome extension manifest, content-script injection, or `chrome.storage`
  usage yet — this is a prerequisite for testing as an actual browser
  extension rather than a local web app.
- "Large Text" and "Increased Spacing" checkboxes in Reading Mode are
  unwired placeholders.

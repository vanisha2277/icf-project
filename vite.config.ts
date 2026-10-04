// ICF 2026 AI disclosure: built with AI assistance.
import { crx } from '@crxjs/vite-plugin'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'
import manifest from './manifest.json' with { type: 'json' }

export default defineConfig({
  plugins: [
    react(),
    crx({ manifest }),
  ],
})

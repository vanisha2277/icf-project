// ICF 2026 AI disclosure: built with AI assistance.
// Typed client for the backend's POST /transform endpoint.

export const API_BASE_URL = "http://localhost:8000";

export interface TransformOptions {
  bionic: boolean;
  chunking: boolean;
  tts_sync: boolean;
}

export interface WordTiming {
  word: string;
  start_ms: number;
  end_ms: number;
}

export interface TransformChunk {
  text: string;
  bionic_html: string | null;
  word_timings: WordTiming[] | null;
}

export interface TransformResponse {
  chunks: TransformChunk[];
}

export async function transformText(
  text: string,
  options: TransformOptions,
): Promise<TransformResponse> {
  let response: Response;
  try {
    response = await fetch(`${API_BASE_URL}/transform`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, options }),
    });
  } catch {
    throw new Error(
      `Could not reach the backend at ${API_BASE_URL}. Is it running?`,
    );
  }

  if (!response.ok) {
    throw new Error(`Backend returned an error (status ${response.status}).`);
  }

  return response.json() as Promise<TransformResponse>;
}

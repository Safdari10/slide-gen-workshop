// frontend/src/hooks/useSlideGenerator.ts
import { useState } from "react";
import type { SlideRequest } from "../types/api";

export function useSlideGenerator() {
  const [status, setStatus] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  async function generate(req: SlideRequest): Promise<void> {
    setLoading(true);
    setStatus("Generating...");
    try {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(req),
      });
      const raw = await res.text();
      const data = raw ? JSON.parse(raw) : null;
      if (!res.ok) {
        setStatus(data?.message || `Error ${res.status}`);
        return;
      }
      setStatus(data?.message || "Done!");
    } catch {
      setStatus("Cannot reach backend. Is FastAPI running?");
    } finally {
      setLoading(false);
    }
  }

  return { status, loading, generate };
}

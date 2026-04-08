// frontend/src/hooks/useManim.ts  ← CREATE
import { useState } from "react";

export function useManim() {
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");

  async function renderScene(sceneClass: string = "TitleSlide"): Promise<void> {
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`/api/render?scene_class=${sceneClass}`, {
        method: "POST",
      });
      if (!res.ok) {
        const t = await res.text();
        setError(`Render failed: ${res.status} — ${t}`);
        return;
      }
      const blob: Blob = await res.blob();
      const url: string = URL.createObjectURL(blob);
      setVideoUrl(url);
    } catch {
      setError("Cannot reach backend.");
    } finally {
      setLoading(false);
    }
  }

  return { videoUrl, loading, error, renderScene };
}

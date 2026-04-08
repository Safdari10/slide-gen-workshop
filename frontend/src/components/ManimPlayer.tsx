// frontend/src/components/ManimPlayer.tsx  ← CREATE
interface Props {
  videoUrl: string | null;
  loading: boolean;
  error: string;
  onRender: () => void;
}

export function ManimPlayer({ videoUrl, loading, error, onRender }: Props) {
  return (
    <div style={{ marginTop: 24 }}>
      <button onClick={onRender} disabled={loading} style={{ padding: "8px 20px", fontSize: 15 }}>
        {loading ? "Rendering..." : "▶ Render Animation"}
      </button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {videoUrl && (
        <video
          src={videoUrl}
          controls
          autoPlay
          style={{ width: "100%", marginTop: 12, borderRadius: 8 }}
        />
      )}
    </div>
  );
}

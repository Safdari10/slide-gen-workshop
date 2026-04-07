// frontend/src/components/GenerateButton.tsx  ← CREATE
interface Props {
  onClick: () => void;
  loading: boolean;
}
export function GenerateButton({ onClick, loading }: Props) {
  return (
    <button
      onClick={onClick}
      disabled={loading}
      style={{ marginTop: 12, padding: "10px 24px", fontSize: 16 }}>
      {loading ? "Generating..." : "Generate Slides"}
    </button>
  );
}

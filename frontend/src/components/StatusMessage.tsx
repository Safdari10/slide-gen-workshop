// frontend/src/components/StatusMessage.tsx  ← CREATE
interface Props {
  message: string;
}
export function StatusMessage({ message }: Props) {
  return <p style={{ color: "#555" }}>{message}</p>;
}

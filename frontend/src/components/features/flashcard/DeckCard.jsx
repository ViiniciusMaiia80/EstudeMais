import { Button } from "../../ui";

function DeckCard({ nome, flashcardsCount }) {
  return (
    <div className="border border-[#eeeeee] rounded overflow-hidden">
      <div className="h-1.5 bg-brand" />
      <div className="p-4">
        <h3 className="font-semibold text-brand">{nome}</h3>
        <p className="text-sm text-muted mt-1">{flashcardsCount} flashcards criados</p>
        <Button variant="link" className="mt-3">
          Estudar agora &gt;
        </Button>
      </div>
    </div>
  );
}

export default DeckCard;

import { FileText } from "lucide-react";
import { Button } from "../../ui";

function QuestionListItem({ titulo, materiaNome }) {
  return (
    <div className="flex items-center justify-between border border-[#eeeeee] rounded p-4">
      <div className="flex items-center gap-3">
        <span className="w-9 h-9 rounded bg-brand text-white flex items-center justify-center shrink-0">
          <FileText size={18} />
        </span>
        <div>
          <p className="font-medium text-brand text-sm">{titulo}</p>
          <p className="text-xs text-muted">{materiaNome}</p>
        </div>
      </div>
      <Button variant="primary" className="text-sm py-1.5">
        Responder
      </Button>
    </div>
  );
}

export default QuestionListItem;

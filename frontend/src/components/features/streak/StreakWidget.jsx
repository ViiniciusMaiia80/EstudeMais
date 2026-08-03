import { Flame, MoreVertical } from "lucide-react";
import { IconButton } from "../../ui";

function StreakWidget() {
  return (
    <div className="flex items-center justify-between border border-[#eeeeee] rounded p-4">
      <div className="flex items-center gap-2">
        <Flame size={20} className="text-amber-500" />
        <span className="text-sm font-medium text-brand">Comece uma sequência</span>
      </div>
      <IconButton icon={MoreVertical} label="Mais opções" />
    </div>
  );
}

export default StreakWidget;

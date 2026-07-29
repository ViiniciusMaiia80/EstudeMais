import { Settings, HelpCircle } from "lucide-react";
import { SearchInput, IconButton, Button } from "../../ui";

function Topbar() {
  return (
    <header className="w-full h-20 bg-white border-b border-[#eeeeee] flex items-center gap-6 px-6">
      <SearchInput />
      <div className="flex items-center gap-1">
        <IconButton icon={Settings} label="Configurações" />
        <IconButton icon={HelpCircle} label="Ajuda" />
      </div>
      <Button variant="primary">Criar Flashcard</Button>
    </header>
  );
}

export default Topbar;

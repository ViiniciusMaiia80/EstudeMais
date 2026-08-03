import { NavLink } from "react-router-dom";
import { Home, FileText, ClipboardList, BarChart3 } from "lucide-react";
import { Logo } from "../../ui";

const itemClasses =
  "flex items-center gap-3 px-4 py-2.5 rounded text-base font-medium text-white transition duration-200 ease-in-out";

function Sidebar() {
  return (
    <nav className="w-56 shrink-0 bg-brand py-6 px-3 flex flex-col items-center gap-6">
      <Logo className="h-12" />

      <div className="w-full flex flex-col gap-1">
        <NavLink
          to="/inicio"
          className={({ isActive }) =>
            `${itemClasses} ${isActive ? "bg-amber-400 !text-brand" : "hover:bg-white/10"}`
          }
        >
          <Home size={18} />
          Início
        </NavLink>

        <span className={`${itemClasses} cursor-default opacity-70`}>
          <FileText size={18} />
          Flashcards
        </span>

        <span className={`${itemClasses} cursor-default opacity-70`}>
          <ClipboardList size={18} />
          Questões
        </span>

        <span className={`${itemClasses} cursor-default opacity-70`}>
          <BarChart3 size={18} />
          Dashboard
        </span>
      </div>
    </nav>
  );
}

export default Sidebar;

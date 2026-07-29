import { Search } from "lucide-react";

function SearchInput({ placeholder = "Search", className = "", ...props }) {
  return (
    <div className={`relative flex-1 ${className}`}>
      <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-muted" size={18} />
      <input
        type="search"
        placeholder={placeholder}
        className="w-full h-10 border border-[#d7d7d7] rounded pl-10 pr-3 text-sm bg-white text-[#333333] placeholder:text-[#9a9a9a] focus:outline-none focus:border-brand"
        {...props}
      />
    </div>
  );
}

export default SearchInput;

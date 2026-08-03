function FormField({ label, type = "text", options, className = "", ...props }) {
  const controlClasses =
    "w-full h-[42px] border border-[#d7d7d7] rounded px-3 text-sm bg-white text-[#333333] placeholder:text-[#9a9a9a] focus:outline-none focus:border-brand";

  return (
    <div className={`text-left mb-4 ${className}`}>
      <label className="block text-[13px] text-muted mb-1.5">{label}</label>
      {type === "select" ? (
        <select className={controlClasses} {...props}>
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      ) : (
        <input type={type} className={controlClasses} {...props} />
      )}
    </div>
  );
}

export default FormField;

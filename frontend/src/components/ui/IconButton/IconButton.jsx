function IconButton({ icon: Icon, label, size = 18, className = "", ...props }) {
  return (
    <button
      type="button"
      aria-label={label}
      className={`inline-flex items-center justify-center w-9 h-9 rounded text-brand bg-transparent border-none cursor-pointer hover:opacity-70 transition duration-200 ease-in-out ${className}`}
      {...props}
    >
      <Icon size={size} />
    </button>
  );
}

export default IconButton;

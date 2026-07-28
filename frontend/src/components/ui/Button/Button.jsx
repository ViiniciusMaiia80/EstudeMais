function Button({
  variant = "primary",
  fullWidth = false,
  type = "button",
  className = "",
  children,
  ...props
}) {
  const base =
    "inline-flex items-center justify-center rounded transition duration-200 ease-in-out cursor-pointer border";

  const variants = {
    primary: "bg-brand text-white border-brand font-medium hover:opacity-95",
    outline: "bg-white text-brand border-brand font-medium hover:opacity-85",
    ghost:
      "bg-transparent text-brand border-transparent font-normal text-sm whitespace-nowrap hover:opacity-85",
    link: "bg-transparent text-link border-transparent font-normal text-[13px] p-0",
  };

  const sizing = fullWidth ? "w-full h-[42px]" : "px-[18px] py-2";

  return (
    <button
      type={type}
      className={`${base} ${variants[variant]} ${sizing} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
}

export default Button;

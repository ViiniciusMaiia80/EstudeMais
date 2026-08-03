import Logo from "../../ui/Logo/Logo";

function AuthLayout({ title, children }) {
  return (
    <div className="min-h-screen bg-white flex flex-col justify-center items-center p-6">
      <div className="mb-10">
        <Logo className="h-12" />
      </div>

      <div className="w-full max-w-[420px] max-[900px]:max-w-[360px] text-center">
        {title && (
          <h1 className="text-[58px] leading-[1.1] text-brand font-bold mb-[34px] max-[900px]:text-[42px]">
            {title}
          </h1>
        )}
        {children}
      </div>
    </div>
  );
}

export default AuthLayout;

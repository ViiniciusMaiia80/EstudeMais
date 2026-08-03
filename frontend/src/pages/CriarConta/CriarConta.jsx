import { useNavigate } from "react-router-dom";
import { AuthLayout } from "../../components/layout";
import { Button } from "../../components/ui";

function CriarConta() {
  const navigate = useNavigate();

  return (
    <AuthLayout title="Crie sua conta">
      <Button variant="primary" fullWidth onClick={() => navigate("/cadastro")}>
        Continue com o e-mail
      </Button>

      <div className="my-4 text-[#7a7a7a] text-sm font-normal relative text-center before:content-[''] before:absolute before:top-1/2 before:left-0 before:w-[42%] before:h-px before:bg-[#dddddd] after:content-[''] after:absolute after:top-1/2 after:right-0 after:w-[42%] after:h-px after:bg-[#dddddd]">
        ou
      </div>

      <Button variant="link" onClick={() => navigate("/login")}>
        Já tem uma conta?
      </Button>
    </AuthLayout>
  );
}

export default CriarConta;

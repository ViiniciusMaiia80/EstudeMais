import { useNavigate } from "react-router-dom";
import AuthLayout from "../../components/layout/AuthLayout/AuthLayout";
import FormField from "../../components/ui/FormField/FormField";
import Button from "../../components/ui/Button/Button";

function Login() {
  const navigate = useNavigate();

  return (
    <AuthLayout title="Faça Login">
      <FormField label="E-mail" type="email" placeholder="seu@email.com" />
      <FormField label="Senha" type="password" placeholder="Sua senha" />

      <div className="mt-3">
        <Button variant="primary" fullWidth onClick={() => navigate("/")}>
          Entrar
        </Button>
      </div>

      <div className="w-full flex justify-between mt-7 max-[900px]:flex-col max-[900px]:items-center max-[900px]:gap-3.5">
        <Button variant="link" onClick={() => navigate("/criar-conta")}>
          Criar uma conta?
        </Button>
        <Button variant="link">Esqueceu a senha?</Button>
      </div>
    </AuthLayout>
  );
}

export default Login;

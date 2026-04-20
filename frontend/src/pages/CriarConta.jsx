import { useNavigate } from "react-router-dom";
import logo from "../assets/logo-estudemais.svg";

function CriarConta() {
  const navigate = useNavigate();

  return (
    <div className="auth-page">
      <div className="auth-logo">
        <img src={logo} alt="EstudeMais" />
      </div>

      <div className="auth-card">
        <h1>Crie sua conta</h1>

        <button
          type="button"
          className="auth-button"
          onClick={() => navigate("/cadastro")}
        >
          Continue com o e-mail
        </button>

        <div className="auth-divider">ou</div>

        <button
          type="button"
          className="auth-link"
          onClick={() => navigate("/login")}
        >
          Já tem uma conta?
        </button>
      </div>
    </div>
  );
}

export default CriarConta;
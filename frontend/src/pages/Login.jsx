import { useNavigate } from "react-router-dom";
import logo from "../assets/logo-estudemais.svg";

function Login() {
  const navigate = useNavigate();

  return (
    <div className="auth-page">
      <div className="auth-logo">
        <img src={logo} alt="EstudeMais" />
      </div>

      <div className="auth-card">
        <h1>Faça Login</h1>

        <div className="form-group">
          <label>E-mail</label>
          <input
            className="form-input"
            type="email"
            placeholder="seu@email.com"
          />
        </div>

        <div className="form-group">
          <label>Senha</label>
          <input
            className="form-input"
            type="password"
            placeholder="Sua senha"
          />
        </div>

        <div className="auth-actions">
          <button
            type="button"
            className="auth-button"
            onClick={() => navigate("/")}
          >
            Entrar
          </button>
        </div>

        <div className="auth-links-row">
          <button
            type="button"
            className="auth-link"
            onClick={() => navigate("/criar-conta")}
          >
            Criar uma conta?
          </button>

          <button type="button" className="auth-link">
            Esqueceu a senha?
          </button>
        </div>
      </div>
    </div>
  );
}

export default Login;
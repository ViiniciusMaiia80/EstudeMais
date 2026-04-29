import { useState } from "react";
import { useNavigate } from "react-router-dom";
import logo from "../assets/logo-estudemais.svg";

function Cadastro() {
  const navigate = useNavigate();

  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [perfil, setPerfil] = useState("");

  const validar = () => {
    if (!nome) {
      alert("Nome é obrigatório");
      return false;
    }

    if (!email.includes("@")) {
      alert("Email inválido");
      return false;
    }

    if (senha.length < 6) {
      alert("Senha deve ter no mínimo 6 caracteres");
      return false;
    }

    if (!perfil) {
      alert("Selecione um perfil");
      return false;
    }

    return true;
  };

  const handleCadastro = () => {
    if (!validar()) return;

    fetch("http://127.0.0.1:8000/usuario/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nome,
        email,
        senha,
        tipo_usuario: perfil,
      }),
    })
      .then(async (res) => {
        const data = await res.json();

        if (!res.ok) {
          alert("Erro do backend: " + JSON.stringify(data));
          throw new Error("Erro ao cadastrar");
        }

        return data;
      })
      .then(() => {
        alert("Cadastro realizado com sucesso!");
        navigate("/login");
      })
      .catch((err) => {
        console.error(err);
      });
  };

  return (
    <div className="auth-page">
      <div className="auth-logo">
        <img src={logo} alt="EstudeMais" />
      </div>

      <div className="auth-card">
        <h1>Crie sua conta</h1>

        <div className="form-group">
          <label>Nome completo</label>
          <input
            className="form-input"
            type="text"
            placeholder="Digite seu nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>E-mail</label>
          <input
            className="form-input"
            type="email"
            placeholder="seu@email.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Senha</label>
          <input
            className="form-input"
            type="password"
            placeholder="Mínimo 6 caracteres"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Sou</label>
          <select
            className="form-select"
            value={perfil}
            onChange={(e) => setPerfil(e.target.value)}
          >
            <option value="">Selecione uma opção</option>
            <option value="aluno">Aluno</option>
            <option value="professor">Professor</option>
          </select>
        </div>

        <div className="auth-actions">
          <button type="button" className="auth-button" onClick={handleCadastro}>
            Cadastrar
          </button>
        </div>
      </div>
    </div>
  );
}

export default Cadastro;
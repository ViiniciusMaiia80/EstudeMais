import { useState } from "react";

function Cadastro() {

  // 🔹 Estados
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [perfil, setPerfil] = useState("");

  // 🔹 Validação dos campos
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

  // 🔹 Envio para o backend
  const handleCadastro = () => {

    // primeiro valida
    if (!validar()) return;

    // depois envia para o Django
    fetch("http://127.0.0.1:8000/usuario/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nome: nome,
        email: email,
        senha: senha,
        perfil: perfil
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("Cadastro realizado:", data);
        alert("Cadastro realizado com sucesso!");
      })
      .catch((err) => {
        console.error("Erro:", err);
        alert("Erro ao cadastrar");
      });
  };

  // 🔹 Interface
  return (
    <div>
      <h1>Crie sua conta</h1>

      <input
        type="text"
        placeholder="Nome completo"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />

      <br /><br />

      <input
        type="email"
        placeholder="E-mail"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <br /><br />

      <input
        type="password"
        placeholder="Senha"
        value={senha}
        onChange={(e) => setSenha(e.target.value)}
      />

      <br /><br />

      <select
        value={perfil}
        onChange={(e) => setPerfil(e.target.value)}
      >
        <option value="">Selecione um perfil</option>
        <option value="aluno">Aluno</option>
        <option value="professor">Professor</option>
      </select>

      <br /><br />

      <button onClick={handleCadastro}>
        Cadastrar
      </button>

    </div>
  );
}

export default Cadastro;
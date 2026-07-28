import { useState } from "react";
import { useNavigate } from "react-router-dom";
import AuthLayout from "../../components/layout/AuthLayout/AuthLayout";
import FormField from "../../components/ui/FormField/FormField";
import Button from "../../components/ui/Button/Button";

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
    <AuthLayout title="Crie sua conta">
      <FormField
        label="Nome completo"
        type="text"
        placeholder="Digite seu nome"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />

      <FormField
        label="E-mail"
        type="email"
        placeholder="seu@email.com"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <FormField
        label="Senha"
        type="password"
        placeholder="Mínimo 6 caracteres"
        value={senha}
        onChange={(e) => setSenha(e.target.value)}
      />

      <FormField
        label="Sou"
        type="select"
        value={perfil}
        onChange={(e) => setPerfil(e.target.value)}
        options={[
          { value: "", label: "Selecione uma opção" },
          { value: "aluno", label: "Aluno" },
          { value: "professor", label: "Professor" },
        ]}
      />

      <div className="mt-3">
        <Button variant="primary" fullWidth onClick={handleCadastro}>
          Cadastrar
        </Button>
      </div>
    </AuthLayout>
  );
}

export default Cadastro;

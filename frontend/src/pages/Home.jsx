import { useNavigate } from "react-router-dom";
import logo from "../assets/logo-estudemais.svg";
import heroImage from "../assets/img-home.png";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="page-container">
      <header className="home-header">
        <div className="home-logo">
          <img src={logo} alt="EstudeMais" />
        </div>

        <nav className="home-nav">
          <button type="button">Criar Flashcard</button>
          <button type="button">Como Funciona</button>

          <button
            type="button"
            className="btn-outline"
            onClick={() => navigate("/login")}
          >
            Entrar
          </button>

          <button
            type="button"
            className="btn-primary"
            onClick={() => navigate("/criar-conta")}
          >
            Criar Conta
          </button>
        </nav>
      </header>

      <section className="home-hero">
        <div className="home-text">
          <h1>
            Use <span className="home-highlight">Flashcards</span>
            <br />
            para revisões e
            <br />
            acesse <span className="home-highlight">questões</span>
            <br />
            disponibilizadas
            <br />
            por seu professor!
          </h1>
        </div>

        <div className="home-image">
          <img src={heroImage} alt="Ilustração da página inicial" />
        </div>
      </section>
    </div>
  );
}

export default Home;
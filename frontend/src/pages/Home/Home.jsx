import { useNavigate } from "react-router-dom";
import { Logo, Button } from "../../components/ui";
import heroImage from "../../assets/img-home.png";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-white">
      <header className="w-full h-[88px] bg-white border-b border-[#eeeeee] flex items-center justify-between px-12 max-[900px]:h-auto max-[900px]:min-h-[88px] max-[900px]:flex-wrap max-[900px]:justify-center max-[900px]:px-5 max-[900px]:py-4 max-[900px]:gap-4">
        <Logo />

        <nav className="flex items-center gap-6 flex-wrap max-[900px]:justify-center max-[900px]:gap-3">
          <Button variant="ghost">Criar Flashcard</Button>
          <Button variant="ghost">Como Funciona</Button>
          <Button variant="outline" onClick={() => navigate("/login")}>
            Entrar
          </Button>
          <Button variant="primary" onClick={() => navigate("/criar-conta")}>
            Criar Conta
          </Button>
        </nav>
      </header>

      <section className="w-full flex items-center justify-between gap-4 px-12 py-[70px] max-[900px]:flex-col max-[900px]:text-center max-[900px]:px-5 max-[900px]:py-12 max-[900px]:gap-8">
        <div className="flex-1 text-left max-[900px]:text-center">
          <h1 className="text-[64px] leading-[1.1] font-bold text-brand max-w-[620px] max-[900px]:text-[42px] max-[900px]:max-w-full">
            Use{" "}
            <span className="bg-[linear-gradient(transparent_55%,#ffe9a8_55%)] px-0.5">
              Flashcards
            </span>
            <br />
            para revisões e
            <br />
            acesse{" "}
            <span className="bg-[linear-gradient(transparent_55%,#ffe9a8_55%)] px-0.5">
              questões
            </span>
            <br />
            disponibilizadas
            <br />
            por seu professor!
          </h1>
        </div>

        <div className="flex-1 flex justify-end max-[900px]:justify-center">
          <img
            src={heroImage}
            alt="Ilustração da página inicial"
            className="max-w-[520px] w-full h-auto block"
          />
        </div>
      </section>
    </div>
  );
}

export default Home;

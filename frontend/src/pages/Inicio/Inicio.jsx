import { AppShell } from "../../components/layout";
import { DeckCard, QuestionListItem, StreakWidget } from "../../components/features";
import materias from "../../mocks/materias";
import questoes from "../../mocks/questoes";
import usuario from "../../mocks/usuario";

function Inicio() {
  return (
    <AppShell>
      <h1 className="text-2xl font-bold text-brand">Olá, {usuario.nome}</h1>
      <p className="text-sm text-muted mt-1">Aqui está o que temos para hoje nos seus estudos</p>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
        <section>
          <div className="flex items-center justify-between mb-3">
            <h2 className="font-semibold text-brand">Flashcards</h2>
            <button type="button" className="text-link text-sm bg-transparent border-none p-0 cursor-pointer">
              Ver todos &gt;
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {materias.map((materia) => (
              <DeckCard key={materia.id} nome={materia.nome} flashcardsCount={materia.flashcardsCount} />
            ))}

            <div className="border border-dashed border-[#d7d7d7] rounded flex items-center justify-center text-muted text-sm min-h-[120px]">
              + Novo Flashcard
            </div>
          </div>

          <div className="mt-4">
            <StreakWidget />
          </div>
        </section>

        <section>
          <div className="flex items-center justify-between mb-3">
            <h2 className="font-semibold text-brand">Questões</h2>
            <button type="button" className="text-link text-sm bg-transparent border-none p-0 cursor-pointer">
              Ver todos &gt;
            </button>
          </div>

          <div className="flex flex-col gap-3">
            {questoes.map((questao) => (
              <QuestionListItem key={questao.id} titulo={questao.titulo} materiaNome={questao.materiaNome} />
            ))}
          </div>
        </section>
      </div>
    </AppShell>
  );
}

export default Inicio;

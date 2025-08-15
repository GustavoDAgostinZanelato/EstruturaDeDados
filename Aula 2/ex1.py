
class LIVRO:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def exibirDetalhes(self):
        print(f"Livro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Disponível: {'Sim' if self.disponivel else 'Não'}")


class USUARIO:
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []

    def emprestarLivros(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livrosEmprestados.append(livro)
            print(f"{self.nome} alugou o livro: {livro.titulo}")
        else:
            print(f"O livro '{livro.titulo}' não está disponível.")

    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados:
            livro.disponivel = True
            self.livrosEmprestados.remove(livro)
            print(f"{self.nome} devolveu o livro: {livro.titulo}")
        else:
            print(f"{self.nome} não possui o livro '{livro.titulo}'.")

class BIBLIOTECA:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)
        print(f"Livro {livro.titulo} adicionado a biblioteca {self.nome}")
    
    def exibirLivrosDisponiveis(self):
        print(f"\n Livros disponíveis na biblioteca {self.nome}")
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        if disponiveis:
            for livro in disponiveis:
                livro.exibirDetalhes()
        else:
            print("Nenhum livro disponível no momento")


if __name__ == "__main__":
    biblioteca = BIBLIOTECA("Biblioteca Municipal")
    
    livro1 = LIVRO("O Hobbit", "J.R.R. Tolkien")
    livro2 = LIVRO("Dom Casmurro", "Machado de Assis")
    livro3 = LIVRO("Harry Potter", "J.K. Rowling")
    livro4 = LIVRO("O Senhor dos Anéis", "J.R.R. Tolkien")

    biblioteca.livros.append(livro1)
    biblioteca.livros.append(livro2)
    biblioteca.livros.append(livro3)
    biblioteca.livros.append(livro4)

    usuario1 = USUARIO("Alice")
    usuario2 = USUARIO("Bruno")

    biblioteca.exibirLivrosDisponiveis()

    usuario1.emprestarLivros(livro1)
    usuario2.emprestarLivros(livro1)  # Tenta pegar livro já emprestado
    usuario2.emprestarLivros(livro2)

    biblioteca.exibirLivrosDisponiveis()

    # Devolução de livros
    usuario1.devolverLivro(livro1)
    usuario2.devolverLivro(livro2)

    # Exibir livros após devolução
    biblioteca.exibirLivrosDisponiveis()
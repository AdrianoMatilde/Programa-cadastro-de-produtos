# Programa de cadastro de produtos incluindo funcionalidades gerando um arquivo em CSV para persistência de dados.
import csv
import sqlite3

# Classe para representar os produtos
class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

# Classe para gerenciamento

class GerenciadorProdutos:
    def __init__(self):
        self.conexao = sqlite3.connect('produtos.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS produtos (codigo TEXT, nome TEXT, preco REAL, quantidade INTEGER)')
        self.conexao.commit()

    def adicionar_produto(self, codigo, nome, preco, quantidade):
        produto = Produto(codigo, nome, preco, quantidade)
        self.cursor.execute('INSERT INTO produtos (codigo, nome, preco, quantidade) VALUES (?, ?, ?, ?)',
                            (produto.codigo, produto.nome, produto.preco, produto.quantidade))
        self.conexao.commit()

    def buscar_produto(self, codigo):
        self.cursor.execute('SELECT codigo, nome, preco, quantidade FROM produtos WHERE codigo = ?', (codigo,))
        produto = self.cursor.fetchone()
        if produto:
            return Produto(produto[0], produto[1], produto[2], produto[3])
        else:
            return None

    def excluir_produto(self, codigo):
        self.cursor.execute('DELETE FROM produtos WHERE codigo = ?', (codigo,))
        if self.cursor.rowcount > 0:
            print(f"Produto de código {codigo} excluído com sucesso!")
        else:
            print(f"Produto de código {codigo} não encontrado.")
        self.conexao.commit()

    def listar_produtos(self):
        print("Lista de Produtos:")
        self.cursor.execute('SELECT codigo, nome, preco, quantidade FROM produtos')
        produtos = self.cursor.fetchall()
        for produto in produtos:
            print(f"Código: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]:.2f} | Quantidade: {produto[3]}")

    def salvar_produtos(self):
        with open('produtos.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Código", "Nome", "Preço", "Quantidade"])
            self.cursor.execute('SELECT codigo, nome, preco, quantidade FROM produtos')
            produtos = self.cursor.fetchall()
            for produto in produtos:
                writer.writerow([produto[0], produto[1], produto[2], produto[3]])

    def __del__(self):
        self.conexao.close()

# Função para exibir o menu de opções
def exibir_menu():
    print("===== MENU =====")
    print("1 - Adicionar Produto")
    print("2 - Buscar Produto")
    print("3 - Excluir Produto")
    print("4 - Listar Produtos")
    print("5 - Salvar Produtos")
    print("6 - Sair do Programa")


# Função principal do programa
def main():
    gerenciador = GerenciadorProdutos()
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            gerenciador.adicionar_produto(codigo, nome, preco, quantidade)
            print("Produto adicionado com sucesso!")

        elif opcao == "2":
            codigo = input("Digite o código do produto: ")
            produto = gerenciador.buscar_produto(codigo)
            if produto:
                print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R${produto.preco:.2f} | Quantidade: {produto.quantidade}")
            else:
                print(f"Produto de código {codigo} não encontrado.")

        elif opcao == "3":
            codigo = input("Digite o código do produto a ser excluído: ")
            gerenciador.excluir_produto(codigo)

        elif opcao == "4":
            gerenciador.listar_produtos()

        elif opcao == "5":
            gerenciador.salvar_produtos()
            print("Produtos salvos no arquivo produtos.csv. Encerrando o programa...")
            break

        elif opcao == "6":
            print("Encerrando o programa...")

if __name__ == "__main__":
    main()

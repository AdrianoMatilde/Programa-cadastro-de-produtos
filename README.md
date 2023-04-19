# Programa-cadastro-de-produtos

---

Esse é um programa de cadastro de produtos em Python que utiliza um banco de dados SQLite para persistência de dados e também inclui uma funcionalidade para gerar um arquivo CSV com os dados dos produtos cadastrados.

O programa começa com a definição da classe Produto, que possui os atributos código, nome, preço e quantidade, e em seguida define a classe GerenciadorProdutos, que é responsável por gerenciar os produtos, incluindo as operações de adicionar, buscar, excluir e listar produtos, além de salvar os dados em um arquivo CSV.

A classe GerenciadorProdutos possui um construtor que cria uma conexão com o banco de dados SQLite, cria a tabela "produtos" se ela não existir e, ao final de cada operação, realiza um commit para salvar as alterações no banco de dados.

As funções adicionar_produto, buscar_produto e excluir_produto utilizam comandos SQL para manipular os dados no banco de dados, enquanto a função listar_produtos utiliza um comando SQL para buscar todos os produtos e, em seguida, itera sobre os resultados e imprime os dados dos produtos na tela.

A função salvar_produtos utiliza a biblioteca csv do Python para criar um arquivo CSV e escrever os dados dos produtos nele. A função del é responsável por fechar a conexão com o banco de dados quando o objeto GerenciadorProdutos é destruído.

A função main é a função principal do programa, que cria um objeto GerenciadorProdutos e executa um loop infinito que exibe um menu de opções para o usuário e executa as operações de acordo com a opção selecionada. Quando o usuário seleciona a opção "Salvar Produtos", os produtos são salvos no arquivo CSV e o programa é encerrado.

Em resumo, este é um programa simples e funcional para gerenciamento de produtos que utiliza um banco de dados SQLite para persistência de dados e também inclui uma funcionalidade para salvar os dados em um arquivo CSV.

---

Espero que tenha gostado!

Se tiver mais alguma ideia não deixe de contribuir.

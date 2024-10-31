# Gerenciador de Estoque Python

Um aplicativo Python com interface gráfica para gerenciar um estoque, conectando-se a um banco de dados SQL Server.

## Funcionalidades
* **Cadastro de produtos:** Adicione novos produtos ao estoque, incluindo nome, data de validade, lote e quantidade.
* **Gerenciamento de estoque:** Atualize a quantidade de produtos em estoque e consulte informações sobre produtos específicos.
* **Exclusão de produtos:** Remova produtos do estoque.

## Pré-requisitos
**Python:** Versão 3.x (recomenda-se 3.6 ou superior)
**Bibliotecas:**
  * `tkinter`: Biblioteca padrão do Python para criar interfaces gráficas.
  * `pyodbc`: Biblioteca para conectar a bancos de dados ODBC, como SQL Server.
  **Banco de dados:** SQL Server com a tabela "Insumos" criada com os campos "nome_produto", "data_validade", "lote" e "quantidade".
 

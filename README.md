🪙 Agenciamento de Clientes para Negociação de Bitcoin
<p align="center"> <img src="https://img.shields.io/badge/versão-1.0-blue.svg" alt="Versão"> <img src="https://img.shields.io/badge/status-em%20desenvolvimento-green.svg" alt="Status"> <img src="https://img.shields.io/badge/licença-MIT-yellow.svg" alt="Licença"> </p>
<br>📚 Descrição</br>
Este projeto de software foi desenvolvido para uma empresa especializada no agenciamento de clientes potenciais para compra, venda e negociação de bitcoins. O sistema oferece funcionalidades de cadastro de usuários, armazenamento seguro de dados em MySQL e fornece cotações de Bitcoin em tempo real, permitindo transações eficientes e seguras.
<br>🌟 Funcionalidades</br>
Cadastro de Usuários: Criação de contas com informações básicas (nome, e-mail, telefone)
Armazenamento Seguro: Dados de usuários protegidos no banco de dados MySQL
Cotação em Tempo Real: Integração com API externa para cotações atualizadas de Bitcoin
Interface RESTful: API de fácil integração com outras plataformas e aplicativos
<br>🚀 Tecnologias Utilizadas</br>
<table> <tr> <th>Tecnologia</th> <th>Descrição</th> </tr> <tr> <td>Python 3.x</td> <td>Linguagem principal de desenvolvimento</td> </tr> <tr> <td>Flask</td> <td>Framework para criação da API</td> </tr> <tr> <td>MySQL</td> <td>Banco de dados para armazenamento de usuários</td> </tr> <tr> <td>Requests</td> <td>Biblioteca para integração com API de cotação</td> </tr> <tr> <td>Docker (opcional)</td> <td>Contêinerização do projeto</td> </tr> <tr> <td>Git</td> <td>Versionamento de código</td> </tr> </table>
🔧 Como Executar o Projeto
Pré-requisitos
Python 3.x instalado
MySQL configurado
Docker (opcional para contêinerização)
Passos para Inicialização
Clone o Repositório:
bash
git clone https://github.com/thiagoaparsilva/Agenciamento-Bitcoin.git
cd Agenciamento-Bitcoin

Instale as Dependências:
bash
pip install -r requirements.txt

Configure o Banco de Dados:
Crie um arquivo .env com as seguintes informações:
text
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
MYSQL_DATABASE=agenciamento_bitcoin

Inicie o Servidor:
<br>bash</br>
python app.py

Acesse a API: Visite http://localhost:5000
<br>⚡ Exemplos de Uso</br>
Cadastrar Novo Usuário
bash
curl -X POST http://localhost:5000/api/register -d '{"username": "joao", "email": "joao@email.com", "phone": "123456789"}'

Consultar Valor Atual do Bitcoin
bash
curl http://localhost:5000/api/bitcoin_price

<br>🔬 Testes</br>
Execute os testes com o seguinte comando:
bash
pytest

<br>🤝 Como Contribuir</br>
Faça um fork do repositório
Crie uma nova branch: git checkout -b minha-nova-feature
Faça suas alterações e commit: git commit -am 'Adiciona nova feature'
Push para a branch: git push origin minha-nova-feature
Abra um Pull Request
<br>📄 Licença</br>
Este projeto está licenciado sob a Licença MIT. <p align="center"> <a href="link_para_documentacao"> <img src="https://img.shields.io/badge/Documentação-Ver%20Mais-blue?style=for-the-badge" alt="Documentação"> </a> </p>

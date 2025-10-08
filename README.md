# Agrotech Vendas

## 🌾 Visão geral

O **Agrotech Vendas** é uma aplicação em Python criada como parte de um projeto acadêmico da FIAP com foco no **agronegócio brasileiro**.  
Seu principal objetivo é auxiliar **produtores rurais e pequenos comerciantes agrícolas** no controle das vendas realizadas, permitindo uma visão clara do que foi vendido, quando, para quem e por qual valor.

Essa solução contribui diretamente para o fortalecimento da **gestão comercial** dos produtores, facilitando o acesso à informação e a tomada de decisão — mesmo em contextos com pouca familiaridade com tecnologia ou ausência de conexão com sistemas sofisticados.

---

## 🌱 Problema resolvido

Pequenos e médios produtores do agronegócio frequentemente enfrentam desafios para **organizar suas vendas de forma estruturada**.  
Muitos ainda fazem registros manuais, o que gera risco de perda de dados, erros de cálculo e falta de visibilidade sobre a saúde financeira da propriedade.

O sistema **Agrotech Vendas** atua nesse ponto, oferecendo uma interface simples no terminal para registrar, consultar e salvar vendas com consistência, permitindo uma gestão melhor da produção escoada.

---

## 🧩 Setor do agronegócio atendido

Esta solução atua principalmente nos seguintes setores do agro:

- **Distribuição e consumo**: ao controlar e registrar as vendas realizadas, o sistema contribui para o rastreamento e melhoria na logística de saída da produção.  
- **Serviços de apoio**: oferece suporte digital simples e acessível para a gestão de vendas, sem depender de sistemas complexos.

---

## ⚙️ Funcionalidades

- Registro de novas vendas (produto, cliente, quantidade, valor)  
- Consulta de vendas anteriores  
- Salvamento e leitura de dados em arquivos `.txt` e `.json`  
- Conexão com banco de dados Oracle para armazenar e consultar registros  
- Validação de entrada de dados para evitar erros  
- Estrutura de código organizada com subalgoritmos (funções reutilizáveis)

---

## 💡 Tecnologias utilizadas

| Tecnologia     | Uso principal                                |
|----------------|-----------------------------------------------|
| Python 3.x     | Lógica do sistema e manipulação de dados      |
| `.txt`         | Armazenamento de relatórios                   |
| `.json`        | Salvamento e recuperação de dados estruturados|
| Oracle DB      | Persistência dos dados em banco relacional    |

---

## 📂 Estrutura de pastas

agrotech_vendas/
├── main.py # Arquivo principal da aplicação
├── funcoes.py # Subalgoritmos (cadastrar, consultar etc.)
├── conexao_oracle.py # Módulo de conexão com Oracle DB
├── dados/
│ ├── vendas.json # Armazenamento estruturado de dados
│ └── relatorio.txt # Exportação de relatório em texto
└── README.md # Este arquivo


## 🧪 Como executar o projeto

1. **Clone o repositório:**

git clone https://github.com/Julia-carvalho96/agrotech_vendas.git
Navegue até a pasta:


cd agrotech_vendas
Crie e ative o ambiente virtual (opcional, mas recomendado):


python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
Instale as dependências (se houver):

pip install -r requirements.txt
Execute o sistema:

python main.py
🧠 Aprendizados aplicados
Este projeto foi construído com base nos seguintes conceitos aprendidos nos capítulos 3 a 6 da disciplina de Python:

Subalgoritmos: uso de funções com passagem de parâmetros

Estruturas de dados: listas, tuplas e dicionários para armazenar e manipular informações

Manipulação de arquivos: leitura e escrita em .txt e .json

Conexão com banco de dados Oracle: integração para armazenamento e consulta de informações

👩‍🌾 Futuras melhorias
Interface gráfica simples (Tkinter ou versão web)

Cadastro de clientes e produtos

Exportação em PDF ou Excel

Dashboard com relatórios de vendas

👥 Integrantes do grupo
Julia Duarte de Carvalho – RM 567816

📜 Licença
Este projeto é parte de uma atividade acadêmica e não possui licença de uso comercial.

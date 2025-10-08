# agrotech_vendas

## 🌾 Visão geral do projeto

O **agrotech_vendas** é um sistema simples, funcional e baseado em terminal para **registro e análise de vendas agrícolas**. Foi desenvolvido em Python como parte do projeto da disciplina da FIAP, com foco em **facilitar a gestão de vendas de pequenos produtores rurais**.

O sistema permite:
- Registrar vendas com data, produto, quantidade, preço e total;
- Listar todas as vendas feitas;
- Ver um resumo por produto (número de vendas e total acumulado);
- Gerar um relatório `.txt` com os totais por produto.

---

## 🧑‍🌾 Área do agronegócio atendida

Esta solução atua no setor de **distribuição e consumo**, ao permitir que pequenos produtores tenham **visibilidade sobre suas vendas** e desempenho financeiro. Ela substitui o controle manual (papel ou planilha) por um sistema digital acessível e fácil de usar.

---

## 🧠 Tecnologias utilizadas

O projeto utiliza os principais recursos aprendidos nos capítulos 3 a 6 da disciplina de Python, incluindo:

- ✅ Subalgoritmos com funções;
- ✅ Estruturas de dados (listas, dicionários);
- ✅ Manipulação de arquivos (`.json` e `.txt`);
- ✅ Uso de condicionais, laços e tratamento de exceções;
- ✅ Interface de menu no terminal (sem interface gráfica).

> O sistema é 100% utilizável via linha de comando e pensado para rodar em qualquer ambiente com Python 3 instalado.

---

## 📁 Estrutura do projeto

agrotech_vendas/
├── dados/
│ ├── vendas.json # Base de dados com as vendas registradas
│ └── relatorio.txt # Relatório com totais por produto (gerado pelo sistema)
│
├── main.py # Arquivo principal com o código do sistema
├── README.md # Documentação do projeto


---

## 📌 Funcionalidades

| Funcionalidade                | Descrição |
|------------------------------|-----------|
| Registrar nova venda         | Solicita nome do produto, quantidade e preço unitário. Calcula o total e salva no arquivo `vendas.json`. |
| Listar vendas registradas    | Mostra todas as vendas registradas até o momento, com data, produto e valor. |
| Mostrar totais por produto   | Exibe o total de vendas e o valor acumulado por produto. |
| Gerar relatório `.txt`       | Cria um relatório formatado e salva no arquivo `relatorio.txt`. |

---

## 🧪 Validações aplicadas

- Tratamento de erros ao abrir arquivos inexistentes ou corrompidos;
- Prevenção de divisão por zero;
- Verificação se há vendas antes de exibir ou gerar relatórios;
- Conversão segura de entradas para números (`float()`).

---

## 📝 Como executar o projeto

1. Clone o repositório ou baixe os arquivos.
2. Garanta que a pasta `dados/` existe (ou crie manualmente).
3. Execute o programa com:
```bash
python main.py


4. Siga o menu exibido no terminal:
  1) Registrar nova venda
  2) Listar vendas
  3) Mostrar totais por produto
  4) Gerar relatório .txt
  0) Sair

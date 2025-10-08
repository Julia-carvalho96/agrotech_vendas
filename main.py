import json
from datetime import date

# caminho do arquivo onde as vendas vão ser salvas
CAMINHO_VENDAS = "dados/vendas.json"


def registrar_venda():
    print("\n=== Registrar nova venda ===")

    produto = input("Nome do produto: ")
    quantidade = float(input("Quantidade vendida (kg ou sacas): "))
    preco_unitario = float(input("Preço unitário (R$): "))

    total = quantidade * preco_unitario
    data_hoje = date.today().isoformat()

    nova_venda = {
        "produto": produto,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "total": total,
        "data": data_hoje
    }

    try:
        with open(CAMINHO_VENDAS, "r", encoding="utf-8") as f:
            vendas = json.load(f)
    except json.JSONDecodeError:
        vendas = []

    vendas.append(nova_venda)

    with open(CAMINHO_VENDAS, "w", encoding="utf-8") as f:
        json.dump(vendas, f, indent=2, ensure_ascii=False)

    print(f"\n✅ venda registrada com sucesso! total = R$ {total:.2f}")


def listar_vendas():
    print("\n=== Vendas registradas ===")
    try:
        with open(CAMINHO_VENDAS, "r", encoding="utf-8") as f:
            vendas = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Nenhuma venda registrada ainda.")
        return

    if not vendas:
        print("Nenhuma venda registrada ainda.")
        return

    for i, venda in enumerate(vendas, start=1):
        print(f"{i:02d}) {venda['data']} | {venda['produto']} | qtd: {venda['quantidade']} | R$: {venda['preco_unitario']} | total: R$ {venda['total']}")


def mostrar_totais():
    print("\n=== Totais por produto ===")
    try:
        with open(CAMINHO_VENDAS, "r", encoding="utf-8") as f:
            vendas = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Nenhuma venda registrada.")
        return

    if not vendas:
        print("Nenhuma venda registrada.")
        return

    totais = {}
    for venda in vendas:
        produto = venda["produto"]
        total = venda["total"]

        if produto not in totais:
            totais[produto] = {"total": 0, "qtd_vendas": 0}

        totais[produto]["total"] += total
        totais[produto]["qtd_vendas"] += 1

    total_geral = 0
    for produto, info in totais.items():
        print(f"- {produto:<8} | vendas: {info['qtd_vendas']:>2} | total: R$ {info['total']:.2f}")
        total_geral += info["total"]

    print("-" * 40)
    print(f"TOTAL GERAL: R$ {total_geral:.2f}")


def gerar_relatorio():
    print("\n=== Gerando relatório ===")
    try:
        with open(CAMINHO_VENDAS, "r", encoding="utf-8") as f:
            vendas = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Nenhuma venda registrada.")
        return

    if not vendas:
        print("Nenhuma venda registrada.")
        return

    totais = {}
    for venda in vendas:
        produto = venda["produto"]
        total = venda["total"]

        if produto not in totais:
            totais[produto] = {"total": 0, "qtd_vendas": 0}

        totais[produto]["total"] += total
        totais[produto]["qtd_vendas"] += 1

    total_geral = 0
    linhas = []
    linhas.append("Relatório de vendas\n")
    linhas.append("-" * 40)

    for produto, info in totais.items():
        linha = f"{produto:<8} | vendas: {info['qtd_vendas']:>2} | total: R$ {info['total']:.2f}"
        linhas.append(linha)
        total_geral += info["total"]

    linhas.append("-" * 40)
    linhas.append(f"TOTAL GERAL: R$ {total_geral:.2f}")
    linhas.append("")

    with open("dados/relatorio.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print("✅ Relatório salvo em 'dados/relatorio.txt'")


# ======== MENU PRINCIPAL ========

while True:
    print("\n=== MENU ===")
    print("1) Registrar nova venda")
    print("2) Listar vendas")
    print("3) Mostrar totais por produto")
    print("4) Gerar relatório .txt")
    print("0) Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_venda()
    elif opcao == "2":
        listar_vendas()
    elif opcao == "3":
        mostrar_totais()
    elif opcao == "4":
        gerar_relatorio()
    elif opcao == "0":
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")

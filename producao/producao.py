import tkinter as tk
from tkinter import ttk
from pathlib import Path

ARQUIVO = Path(__file__).parent.parent / "estoque" / "estoque_atualizado.txt"


def carregar_dados():
    dados = {}
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha or ":" not in linha:
                    continue
                chave, valor = linha.split(":", 1)
                dados[chave.strip()] = valor.strip()
    except FileNotFoundError:
        dados["erro"] = f"Arquivo '{ARQUIVO}' não encontrado. Gere o estoque no módulo C."
    return dados


def parse_float_valor(valor_str: str) -> float:
    v = valor_str.replace("R$", "").replace(" ", "").replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return 0.0


def main():
    dados = carregar_dados()

    root = tk.Tk()
    root.title("Módulo Produção")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="both", expand=True)

    if "erro" in dados:
        ttk.Label(frame, text=dados["erro"], foreground="red").pack()
        root.mainloop()
        return

    materia = dados.get("Nome da matéria prima", dados.get("Nome da mat�ria prima", ""))
    quantidade = int(dados.get("Quantidade de matéria prima", dados.get("Quantidade de mat�ria prima", "0")) or "0")
    preco_unit = parse_float_valor(dados.get("Valor unitário", "0"))
    valor_total = parse_float_valor(dados.get("Valor total da nota fiscal", "0"))

    ttk.Label(frame, text="Controle de Produção", font=("Arial", 14, "bold")).pack(pady=(0, 10))

    ttk.Label(frame, text=f"Matéria-prima: {materia}").pack(anchor="w")
    ttk.Label(frame, text=f"Quantidade em estoque: {quantidade} unidades").pack(anchor="w")
    ttk.Label(frame, text=f"Preço unitário de compra: R$ {preco_unit:.2f}").pack(anchor="w")
    ttk.Label(frame, text=f"Custo total do lote: R$ {valor_total:.2f}").pack(anchor="w")

    ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=10)

    ttk.Label(frame, text="Dados gerais da entrada", font=("Arial", 11, "bold")).pack(anchor="w")

    campos = [
        "Número de entrada",
        "Número da nota fiscal",
        "Nome do fornecedor",
        "CNPJ do fornecedor",
    ]
    for campo in campos:
        ttk.Label(frame, text=f"{campo}: {dados.get(campo, '')}").pack(anchor="w")

    root.mainloop()


if __name__ == "__main__":
    main()

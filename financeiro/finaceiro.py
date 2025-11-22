import tkinter as tk
from tkinter import ttk
from pathlib import Path

ARQUIVO = Path(__file__).parent.parent / "estoque" / "estoque_atualizado.txt"


def carregar_dados():
    dados = {}
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                if ":" not in linha:
                    continue
                chave, valor = linha.split(":", 1)
                dados[chave.strip()] = valor.strip()
    except FileNotFoundError:
        dados["erro"] = f"Arquivo '{ARQUIVO}' não encontrado. Gere o estoque no módulo C."
    return dados


def main():
    dados = carregar_dados()

    root = tk.Tk()
    root.title("Módulo Financeiro")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="both", expand=True)

    if "erro" in dados:
        ttk.Label(frame, text=dados["erro"]).pack()
        root.mainloop()
        return

    valor_total = float(dados.get("Valor total da nota fiscal", "0").replace(",", "."))
    qtd_parcelas = int(dados.get("Quantidade de parcelas", "1"))
    valor_parcela = valor_total / qtd_parcelas if qtd_parcelas > 0 else 0

    ttk.Label(frame, text="Resumo Financeiro", font=("Arial", 14, "bold")).pack(pady=(0, 10))

    ttk.Label(frame, text=f"Valor total da nota fiscal: R$ {valor_total:.2f}").pack(anchor="w")
    ttk.Label(frame, text=f"Quantidade de parcelas: {qtd_parcelas}").pack(anchor="w")
    ttk.Label(frame, text=f"Valor de cada parcela: R$ {valor_parcela:.2f}").pack(anchor="w")

    ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=10)

    ttk.Label(frame, text="Dados brutos do arquivo:", font=("Arial", 10, "bold")).pack(anchor="w")

    for chave, valor in dados.items():
        if chave == "erro":
            continue
        ttk.Label(frame, text=f"{chave}: {valor}").pack(anchor="w")

    root.mainloop()


if __name__ == "__main__":
    main()

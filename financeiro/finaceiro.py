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
    # remove "R$" e espaços, troca vírgula por ponto
    v = valor_str.replace("R$", "").replace(" ", "").replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return 0.0


def main():
    dados = carregar_dados()

    root = tk.Tk()
    root.title("Módulo Financeiro")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="both", expand=True)

    if "erro" in dados:
        ttk.Label(frame, text=dados["erro"], foreground="red").pack()
        root.mainloop()
        return

    valor_total_nf = parse_float_valor(dados.get("Valor total da nota fiscal", "0"))
    qtd_parcelas = int(dados.get("Quantidade de parcelas", "1") or "1")
    valor_parcela = valor_total_nf / qtd_parcelas if qtd_parcelas > 0 else 0.0

    ttk.Label(frame, text="Resumo Financeiro", font=("Arial", 14, "bold")).pack(pady=(0, 10))

    ttk.Label(frame, text=f"Valor total da nota fiscal: R$ {valor_total_nf:.2f}").pack(anchor="w")
    ttk.Label(frame, text=f"Quantidade de parcelas: {qtd_parcelas}").pack(anchor="w")
    ttk.Label(frame, text=f"Valor de cada parcela: R$ {valor_parcela:.2f}").pack(anchor="w")

    ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=10)

    ttk.Label(frame, text="Detalhamento das parcelas", font=("Arial", 11, "bold")).pack(anchor="w")

    cols = ("Parcela", "Vencimento", "Valor")
    tree = ttk.Treeview(frame, columns=cols, show="headings", height=8)
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, anchor="center", width=150)
    tree.pack(fill="both", expand=True)

    # Linhas "PARCELA X: Vencimento ... | Valor R$Y"
    for chave, valor in dados.items():
        if not chave.startswith("PARCELA "):
            continue
        # valor = "Vencimento dd/mm/aaaa | Valor R$xx"
        parte_venc, _, parte_valor = valor.partition("|")
        vencimento = parte_venc.replace("Vencimento", "").strip()
        valor_num = parte_valor.replace("Valor", "").strip()
        tree.insert("", "end", values=(chave, vencimento, valor_num))

    root.mainloop()


if __name__ == "__main__":
    main()

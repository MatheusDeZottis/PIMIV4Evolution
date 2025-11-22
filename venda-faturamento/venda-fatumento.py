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
    root.title("Módulo Venda / Faturamento")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="both", expand=True)

    if "erro" in dados:
        ttk.Label(frame, text=dados["erro"]).pack()
        root.mainloop()
        return

    quantidade = int(dados.get("Quantidade de matéria prima", dados.get("Quantidade de mat�ria prima", "0")))
    preco_unit_custo = float(dados.get("Valor unitário da matéria prima", dados.get("Valor unit�rio da mat�ria prima", "0")).replace(",", "."))
    # Markup simples de 30% para venda
    preco_unit_venda = preco_unit_custo * 1.30
    receita_total = preco_unit_venda * quantidade
    custo_total = preco_unit_custo * quantidade
    lucro = receita_total - custo_total

    ttk.Label(frame, text="Simulação de Venda / Faturamento", font=("Arial", 14, "bold")).pack(pady=(0, 10))

    ttk.Label(frame, text=f"Quantidade disponível para venda: {quantidade}").pack(anchor="w")
    ttk.Label(frame, text=f"Preço de custo (unitário): R$ {preco_unit_custo:.2f}").pack(anchor="w")
    ttk

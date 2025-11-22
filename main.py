import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent


def run_estoque():
    candidatos = [
        BASE_DIR / "estoque" / "ModuloEstoque",
        BASE_DIR / "estoque" / "ModuloEstoque.exe",
    ]
    exe = next((p for p in candidatos if p.exists()), None)

    if not exe:
        print("\n[ERRO] Executável do módulo ESTOQUE não encontrado.")
        print("       Compile o C dentro da pasta estoque:")
        print("       gcc ModuloEstoque.c -o ModuloEstoque\n")
        return

    print(f"\n[INFO] Executando módulo ESTOQUE: {exe}\n")
    subprocess.call([str(exe)])


def run_script(rel_path: str, nome: str):
    script = BASE_DIR / rel_path
    if not script.exists():
        print(f"\n[ERRO] Script {rel_path} não encontrado.\n")
        return

    print(f"\n[INFO] Abrindo módulo {nome}: {script}\n")
    subprocess.call([sys.executable, str(script)])


def main():
    while True:
        print("\n========== PIM-IV EVOLUTION ==========")
        print("1 - Módulo de Estoque (C)")
        print("2 - Módulo Financeiro (Python)")
        print("3 - Módulo Produção (Python)")
        print("4 - Módulo Venda / Faturamento (Python)")
        print("0 - Sair")
        opcao = input("Selecione uma opção: ").strip()

        if opcao == "1":
            run_estoque()
        elif opcao == "2":
            run_script("financeiro/finaceiro.py", "FINANCEIRO")
        elif opcao == "3":
            run_script("producao/producao.py", "PRODUÇÃO")
        elif opcao == "4":
            run_script("venda-faturamento/venda-fatutamento.py", "VENDA / FATURAMENTO")
        elif opcao == "0":
            print("\nEncerrando sistema...\n")
            break
        else:
            print("\n[ERRO] Opção inválida.\n")


if __name__ == "__main__":
    main()

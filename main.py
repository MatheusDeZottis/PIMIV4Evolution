import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent


def run_estoque():
    # tenta achar o executável do módulo C
    candidatos = [
        BASE_DIR / "estoque" / "ModuloEstoque",
        BASE_DIR / "estoque" / "ModuloEstoque.exe",
    ]
    exe = next((p for p in candidatos if p.exists()), None)

    if not exe:
        print("\n[ERRO] Executável do módulo ESTOQUE não encontrado.")
        print("       Compile o C, ex.: gcc \"Modulo Estoque.c\" -o ModuloEstoque\n")
        return

    print(f"\n[INFO] Executando módulo ESTOQUE: {exe}\n")
    subprocess.call([str(exe)])


def run_financeiro():
    script = BASE_DIR / "financeiro" / "finaceiro.py"
    if not script.exists():
        print("\n[ERRO] Script financeiro/finaceiro.py não encontrado.\n")
        return

    print(f"\n[INFO] Abrindo módulo FINANCEIRO: {script}\n")
    subprocess.call([sys.executable, str(script)])


def run_producao():
    script = BASE_DIR / "producao" / "producao.py"
    if not script.exists():
        print("\n[ERRO] Script producao/producao.py não encontrado.\n")
        return

    print(f"\n[INFO] Abrindo módulo PRODUÇÃO: {script}\n")
    subprocess.call([sys.executable, str(script)])


def run_venda_faturamento():
    script = BASE_DIR / "venda-faturamento" / "venda-fatutamento.py"
    if not script.exists():
        print("\n[ERRO] Script venda-faturamento/venda-fatutamento.py não encontrado.\n")
        return

    print(f"\n[INFO] Abrindo módulo VENDA / FATURAMENTO: {script}\n")
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
            run_financeiro()
        elif opcao == "3":
            run_producao()
        elif opcao == "4":
            run_venda_faturamento()
        elif opcao == "0":
            print("\nEncerrando sistema...\n")
            break
        else:
            print("\n[ERRO] Opção inválida.\n")


if __name__ == "__main__":
    main()
#include <stdio.h>
#include <locale.h>
#include <time.h>
#include <stdlib.h>

// Estrutura para armazenar os dados de UMA parcela
typedef struct {
    struct tm vencimento; // Data de vencimento (usa tm_mday, tm_mon, tm_year)
    float valor;          // Valor individual da parcela
} Parcela;

// Estrutura principal para armazenar todos os dados da entrada de mercadoria
typedef struct {
    int numeroentrada;
    char numeronotafiscal[20];
    char materiaprima[50];
    int quantidademp;
    float precounitario;
    float valortotalnf;

    char cnpjfornecedor[20]; 
    char nomefornecedor[100]; 
    
    int quantidadeparcela;
    Parcela *parcelas; 
} EntradaMercadoria;

void limpar_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main()
{
    setlocale(LC_ALL, "portuguese");
    
    EntradaMercadoria entrada;

    printf("Digite o número de entrada de mercadoria: ");
    scanf("%d", &entrada.numeroentrada);
    limpar_buffer();

    printf("Digite o número da nota fiscal: ");
    scanf("%[^\n]", entrada.numeronotafiscal); 
    limpar_buffer();

    printf("Digite o nome do fornecedor: ");
    scanf("%[^\n]", entrada.nomefornecedor);
    limpar_buffer();

    printf("Digite o CNPJ do fornecedor: ");
    scanf("%s", entrada.cnpjfornecedor);
    limpar_buffer();

    printf("Digite o nome da matéria prima: ");
    scanf("%[^\n]", entrada.materiaprima);
    limpar_buffer();

    printf("Digite a quantidade de matéria prima: ");
    scanf("%d", &entrada.quantidademp);
    limpar_buffer();

    printf("Qual valor unitário de cada produto? ");
    scanf("%f", &entrada.precounitario);
    limpar_buffer();

    entrada.valortotalnf = entrada.quantidademp * entrada.precounitario;
    printf("\nO valor total da nota fiscal é: R$%.2f\n", entrada.valortotalnf);

    printf("Em quantos pagamentos essa compra foi parcelada? ");
    scanf("%d", &entrada.quantidadeparcela);
    limpar_buffer();
    
    entrada.parcelas = (Parcela *)malloc(entrada.quantidadeparcela * sizeof(Parcela));
    if (entrada.parcelas == NULL) {
        printf("\nErro: Falha ao alocar memória para as parcelas.\n");
        return 1;
    }

    float valorparcela = entrada.valortotalnf / entrada.quantidadeparcela;

    printf("\n--- Registro de Parcelas ---\n");
    for (int i = 0; i < entrada.quantidadeparcela; i++)
    {
        printf("Digite a data de vencimento da parcela %d (DD/MM/AAAA): ", i + 1);
        scanf("%d/%d/%d", 
            &entrada.parcelas[i].vencimento.tm_mday, 
            &entrada.parcelas[i].vencimento.tm_mon, 
            &entrada.parcelas[i].vencimento.tm_year);
        limpar_buffer();

        entrada.parcelas[i].vencimento.tm_mon  -= 1; 
        entrada.parcelas[i].vencimento.tm_year -= 1900; 
        
        entrada.parcelas[i].valor = valorparcela;

        printf("Parcela %d registrada: Vencimento %02d/%02d/%04d, Valor R$%.2f\n", 
            i + 1, 
            entrada.parcelas[i].vencimento.tm_mday, 
            entrada.parcelas[i].vencimento.tm_mon + 1, 
            entrada.parcelas[i].vencimento.tm_year + 1900,
            entrada.parcelas[i].valor);
    }

    FILE *arquivo = fopen("estoque_atualizado.txt", "w");
    if (arquivo != NULL)
    {
        fprintf(arquivo, "--- ENTRADA DE MERCADORIA %d ---\n", entrada.numeroentrada);
        fprintf(arquivo, "Número de entrada: %d\n", entrada.numeroentrada);
        fprintf(arquivo, "Número da nota fiscal: %s\n", entrada.numeronotafiscal);
        fprintf(arquivo, "Nome do fornecedor: %s\n", entrada.nomefornecedor);
        fprintf(arquivo, "CNPJ do fornecedor: %s\n", entrada.cnpjfornecedor);
        fprintf(arquivo, "Nome da matéria prima: %s\n", entrada.materiaprima);
        fprintf(arquivo, "Quantidade de matéria prima: %d\n", entrada.quantidademp);
        fprintf(arquivo, "Valor unitário: R$%.2f\n", entrada.precounitario);
        fprintf(arquivo, "Valor total da nota fiscal: R$%.2f\n", entrada.valortotalnf);
        fprintf(arquivo, "Quantidade de parcelas: %d\n", entrada.quantidadeparcela);
        fprintf(arquivo, "\n--- DETALHES DAS PARCELAS ---\n");
        
        for (int i = 0; i < entrada.quantidadeparcela; i++)
        {
            fprintf(arquivo,
                "PARCELA %d: Vencimento %02d/%02d/%04d | Valor R$%.2f\n", 
                i + 1,
                entrada.parcelas[i].vencimento.tm_mday,
                entrada.parcelas[i].vencimento.tm_mon + 1,
                entrada.parcelas[i].vencimento.tm_year + 1900,
                entrada.parcelas[i].valor);
        }

        fclose(arquivo);
        printf("\nArquivo estoque_atualizado.txt gerado com sucesso com todos os detalhes das parcelas!\n");
    }
    else
    {
        printf("\nErro ao abrir o arquivo de estoque atualizado!\n");
    }
    
    free(entrada.parcelas);
    return 0;
}

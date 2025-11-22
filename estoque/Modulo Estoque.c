#include <stdio.h>
#include <locale.h>
#include <time.h>

int numeroentrada; //Número de entrada de mercadoria em estoque
char numeronotafiscal; //Número da nota fiscal
char materiaprima[50]; //Nome da matéria prima
int quantidademp; //Quantidade de matéria prima
float precounitario; //Preço unitário da matéria prima
float valortotalnf; //Valor total da nota fiscal
int quantidadeparcela; //Quantidade de parcelas para pagamento
struct tm vencimentoparcela; //Data de vencimento da parcela
int cnpjfornecedor; //CNPJ do fornecedor
char nomefornecedor[100]; //Nome do fornecedor

int main()
{
    setlocale(LC_ALL, "portuguese");

 //Coleta de dados da entrada de mercadoria

    printf ("Digite o número de entrada de mercadoria: ");
    scanf ("%d", &numeroentrada);
    printf ("Digite o número da nota fiscal: ");
    scanf ("%s", &numeronotafiscal);
    printf ("Digite o nome do fornecedor: ");
    scanf ("%s", nomefornecedor);
    printf ("Digite o CNPJ do fornecedor: ");
    scanf ("%d", &cnpjfornecedor);
    printf ("Digite o nome da matéria prima: ");
    scanf ("%s", materiaprima);
    printf ("Digite a quantidade de matéria prima: ");
    scanf ("%d", &quantidademp);
    printf ("Qual valor unitario de cada produto? ");
    scanf ("%f", &precounitario);
    valortotalnf = quantidademp * precounitario;
    printf ("O valor total da nota fiscal é: %.2f\n", valortotalnf);
    printf ("Em quantos pagamentos essa compra foi parcelada? ");
    scanf ("%d", &quantidadeparcela);
    for (int i = 1; i <= quantidadeparcela; i++)
    {
        printf ("Digite a data de vencimento da parcela %d: ", i);
        scanf ("%d/%d/%d", &vencimentoparcela.tm_mday, &vencimentoparcela.tm_mon, &vencimentoparcela.tm_year);
        float valorparcela = valortotalnf / quantidadeparcela;
        
     //Exibição das datas de vencimento e valores das parcelas

        printf ("A parcela %d vence em %02d/%02d/%04d e o valor é: %.2f\n", i, vencimentoparcela.tm_mday, vencimentoparcela.tm_mon, vencimentoparcela.tm_year, valorparcela);
    }

    //Gerando arquivo com estoque atualizado
    FILE *arquivo = fopen ("estoque_atualizado.txt", "w");
    if (arquivo != NULL) //Verifica se o arquivo foi aberto corretamente
    {
        fprintf (arquivo, "Número de entrada de mercadoria: %d\n", numeroentrada);
        fprintf (arquivo, "Número da nota fiscal: %s\n", numeronotafiscal);
        fprintf (arquivo, "Nome do fornecedor: %s\n", nomefornecedor);
        fprintf (arquivo, "CNPJ do fornecedor: %d\n", cnpjfornecedor);
        fprintf (arquivo, "Nome da matéria prima: %s\n", materiaprima);
        fprintf (arquivo, "Quantidade de matéria prima: %d\n", quantidademp);
        fprintf (arquivo, "Valor unitário da matéria prima: %.2f\n", precounitario);
        fprintf (arquivo, "Valor total da nota fiscal: %.2f\n", valortotalnf);
        fprintf (arquivo, "Quantidade de parcelas: %d\n", quantidadeparcela);
        fclose (arquivo);
        printf ("Arquivo de estoque atualizado gerado com sucesso!\n");
    }
    else
    {
        printf ("Erro ao abrir o arquivo de estoque atualizado!\n");
    }
 
 return 0;
} 
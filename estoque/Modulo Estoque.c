#include <stdio.h>
#include <locale.h>
#include <time.h>

int numeroentrada; //N�mero de entrada de mercadoria em estoque
char numeronotafiscal[50]; //N�mero da nota fiscal  <<< AJUSTADO PARA STRING
char materiaprima[50]; //Nome da mat�ria prima
int quantidademp; //Quantidade de mat�ria prima
float precounitario; //Pre�o unit�rio da mat�ria prima
float valortotalnf; //Valor total da nota fiscal
int quantidadeparcela; //Quantidade de parcelas para pagamento
struct tm vencimentoparcela; //Data de vencimento da parcela
long long cnpjfornecedor;
char nomefornecedor[100]; //Nome do fornecedor

int main()
{
    setlocale(LC_ALL, "portuguese");

    //Coleta de dados da entrada de mercadoria

    printf ("Digite o n�mero de entrada de mercadoria: ");
    scanf ("%d", &numeroentrada);

    printf ("Digite o n�mero da nota fiscal: ");
    scanf ("%49s", numeronotafiscal); // <<< AJUSTE: LENDO STRING CORRETA

    printf ("Digite o nome do fornecedor: ");
    scanf ("%99s", nomefornecedor);

    printf ("Digite o CNPJ do fornecedor: ");
    scanf ("%lld", &cnpjfornecedor); // <<< AJUSTE: LENDO COMO long long

    printf ("Digite o nome da mat�ria prima: ");
    scanf ("%49s", materiaprima);

    printf ("Digite a quantidade de mat�ria prima: ");
    scanf ("%d", &quantidademp);

    printf ("Qual valor unitario de cada produto? ");
    scanf ("%f", &precounitario);

    valortotalnf = quantidademp * precounitario;
    printf ("O valor total da nota fiscal �: %.2f\n", valortotalnf);

    printf ("Em quantos pagamentos essa compra foi parcelada? ");
    scanf ("%d", &quantidadeparcela);
    for (int i = 1; i <= quantidadeparcela; i++)
    {
        printf ("Digite a data de vencimento da parcela %d: ", i);
        scanf ("%d/%d/%d", &vencimentoparcela.tm_mday, &vencimentoparcela.tm_mon, &vencimentoparcela.tm_year);
        float valorparcela = valortotalnf / quantidadeparcela;
        printf ("A parcela %d vence em %02d/%02d/%04d e o valor �: %.2f\n",
                i,
                vencimentoparcela.tm_mday,
                vencimentoparcela.tm_mon,
                vencimentoparcela.tm_year,
                valorparcela);
    }

    FILE *arquivo = fopen ("estoque_atualizado.txt", "w");
    if (arquivo != NULL) //Verifica se o arquivo foi aberto corretamente
    {
        fprintf (arquivo, "N�mero de entrada de mercadoria: %d\n", numeroentrada);
        fprintf (arquivo, "N�mero da nota fiscal: %s\n", numeronotafiscal);
        fprintf (arquivo, "Nome do fornecedor: %s\n", nomefornecedor);
        fprintf (arquivo, "CNPJ do fornecedor: %lld\n", cnpjfornecedor);
        fprintf (arquivo, "Nome da mat�ria prima: %s\n", materiaprima);
        fprintf (arquivo, "Quantidade de mat�ria prima: %d\n", quantidademp);
        fprintf (arquivo, "Valor unit�rio da mat�ria prima: %.2f\n", precounitario);
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

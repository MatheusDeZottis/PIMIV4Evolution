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

    printf ("Digite o número de entrada de mercadoria: ");
    scanf ("%d", &numeroentrada);
    printf ("Digite o número da nota fiscal: ");
    scanf ("%s", &numeronotafiscal);
    printf ("Digite o nome da matéria prima: ");
    scanf ("%s", materiaprima);
    printf ("Digite a quantidade de matéria prima: ");
    scanf ("%d", &quantidademp);
    return 0;
}
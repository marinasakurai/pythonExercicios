#Arquivo Control
from Model import somarInicioFim #Conecta a classe model e control
from Model import tabuada
from Model import inicioFim
from Model import impares
from Model import somar10Numeros
from Model import somar0Numero
from Model import calcularMedia
from Model import ehPar
from Model import fatorial
import this
this.opcao = -1 #Declarando a variável
this.num   = -1 #Acionar o while
this.i     = 0#contador
this.negativo = 0
def exercicio01():
    inicio = int(input("Informe o início: "))
    fim    = int(input("Informe o fim: "))
    print(somarInicioFim(inicio,fim))
def exercicio02():
    num = int(input("Informe o número que deseja multiplicar: "))
    fim = int(input("Informe até onde deve ser multiplicado: "))
    print(tabuada(num,fim))
def exercicio03():
    inicio = int(input("Informe o valor inicial: "))
    fim    = int(input("Informe o valor final: "))
    print(inicioFim(inicio, fim))
def exercicio04():
    inicio = int(input("Informe o início: "))
    fim    = int(input("Informe o final: "))
    print(impares(inicio, fim))

def exercicio05():
    for i in range(0,10,1):
        num = int(input("informe {}° número:". format(i+1)))
        soma = somar10Numeros(num)
    print("a soma dos números digitados é: {}".format(soma))

def exercicio06():

    while(this.num != 0):
        this.num = int(input("Informe um número: "))
        soma = somar0Numero(this.num)
    print("a soma dos números digitados é: {}".format(soma))

def exercicio07():

    while(this.num != 0):
        this.num = int(input("Informe um número: "))
        if ehPar(this.num) == True:
            soma = somar10Numeros(this.num)
            this.i += 1 #contar qtos numeros foram digitados
    print("A media dos números digitados é: {}".format(calcularMedia(soma,this.i)))

def exercicio08():
    while(this.num != 0):
        this.num = int(input("Informe um número"))
        #primeira digitação do usuário
        if this.num != 0:
            if this.i == 0:
                maior = this.num
                menor = this.num
            this.i += 1
            #A partir da seunda volta
            if this.num > maior:
                maior = this.num
            if this.num < menor:
                menor = this.num
    print ("O maior número digitado é: {} \ne o menor número digitado é: {}".format(maior,menor))


def exercicio09():
    for i in range(20):
        this.num = int(input("informe um valor: "))
        #a soma dos números positivos
        if this.num >= 0:
            soma = somar10Numeros(this.num)
        #quantidade de valores negativos
        else:
            this.negativo += 1
    print(f"Há {this.negativo} números negativos\nA soma dos positivos é {soma}")

def exercicio10():
    num = int(input("Informe um número: "))
    print(fatorial(num))

def exercicio11():
    quantidade = int(input("Informe a quantidade de jogadores: "))
    for i in range(0, quantidade, 1):
        altura = float(input(f"{i + 1} altura: "))
        #validação
        while (altura <= 0):
              if altura <= 0:
                 print("erro! informe uma altura positiva!")
              altura = float(input(f"{i + 1} altura: "))
        soma = somar10Numeros(altura)
    print (f"A media de altura desse time é {calcularMedia(soma,quantidade)}")


def exercicio12():
    for i in range(0,16,1):
        nota = float(input(f"{i+1} nota: "))
        while(nota < 0 or nota > 10):
            print("Erro! Informe uma nota entre 0 e 10")
        cand = input(f"{i+1} candidata")
        if i == 0:
            maior = nota
        if nota > maior:
            maior = nota
            venc = cand
    print(f"A vencedora é: {venc}, sua nota foi {maior}")

def menu():
    print("\nEscolha uma das opções abaixo: \n" +
          "0. Sair\n" +
          "1. Exercício 01\n" +
          "2. Exercício 02\n" +
          "3. Exercício 03\n" +
          "4. Exercício 04\n" +
          "5. Exercício 05\n" +
          "6. Exercício 06\n" +
          "7. Exercício 07\n" +
          "8. Exercício 08\n" +
          "9. Exercício 09\n" +
          "10. Exercício 10\n" +
          "11. Exercício 11\n" +
          "12. Exercício 12\n")
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu() #Chamar o menu
        if this.opcao == 0:
            print("Obrigado!")
        elif this.opcao == 1:
            exercicio01()
        elif this.opcao == 2:
            exercicio02()
        elif this.opcao == 3:
            exercicio03()
        elif this.opcao == 4:
            exercicio04()
        elif this.opcao == 5:
            exercicio05()
        elif this.opcao == 6:
            exercicio06()
        elif this.opcao == 7:
            exercicio07()
        elif this.opcao == 8:
            exercicio08()
        elif this.opcao == 9:
            exercicio09()
        elif this.opcao == 10:
            exercicio10()
        elif this.opcao == 11:
            exercicio11()
        elif this.opcao == 12:
            exercicio11()
        else:
            print("Erro! Escolha uma opção válida!")








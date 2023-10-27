#Arquivo Model
import this
this.soma = 0
this.num  = 0

#1.Faça um algoritmo que calcule a soma dos números inteiros de 1 a 100.
# while = Utilizo quando eu não sei quantas vezes vou repetir
# for   = Quando eu sei quantas repetições acontecerão
def somarInicioFim(inicio, fim):
    soma = 0 #Instanciei a variável
    for i in range(inicio,fim+1,1):
        soma += i
    return soma

#2. Construa um programa que exiba a tabuada de 1 até N.
def tabuada(num, fim):
    multiplicacao = "" #Instanciando uma variável do tipo texto
    for i in range(1,fim+1, 1):
        multiplicacao += "{} * {} = {}\n".format(num, i, num * i)
    return multiplicacao

#3. Faça um algoritmo que escreva na tela os números
# de um número inicial a um número final. Os números inicial
# e final devem ser informados pelo usuário;
def inicioFim(inicio, fim):
    mostrar = ""
    for i in range(inicio, fim+1, 1):
        mostrar += "{} ".format(i)
    return mostrar

#4. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200;
def impares(inicio, fim):
    impar = ""
    for i in range(inicio, fim+1, 1):
        if i % 2 != 0:
            impar += "{}\n".format(i)
    return impar

#5. escrever um algoritimo que leia 10 números inteiros e, ao final, apresenta a soma de todos os números lidos;

def somar10Numeros(num):
    this.soma += num
    return this.soma

#6. Faça o mesmo que antes, porém, ao invés de ler 10 números,
#o programa deverá ler e somar o números até qe o valor digitados seja zero

def somar0Numero(num):
    this.soma += num
    return this.soma

#7. Escreva 1 algorismo que calcule a média dos números digitados pelo usuário, se eles forem pares.
#Termine a leitura se o usuário digitar zero (0)

def calcularMedia(soma, qtde):
    return soma/qtde

def ehPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

#8Escreva 1 algoritimo que leia valores inteiros e
# encontre o maior e o menor deles. Termine a leitura se p usuário digitar zero(0)


#9 escreva um algoritmo que leia 20 valores inteiros e ao final exiba:
#A- a soma dos números positivos;
#B - a quantidade de valores negativos

#10 Escreva um programa que lido um numero, calcule e informe o seu fatorial.
#ex. 5! = 5*4*3*2*1 = 120

def fatorial(num):
    aux = num
    fat = 1
    while (num > 1):
        fat = fat * num
        num -= 1
    return f"0 fatorial de {aux} é {fat}"

#11 Escreva um programa que leia um valor correspondente ao número de jogadores de um time de volei
#o programa deverá ler uma altura para cada um dos jogadores e, ao final informar a altura media do time

#12 Em um concurso de miss, os jurados precisam digitar o nome das 16 candidatas e suas respectivas notas
#(0 a 10). Crie um programa que leia estas informações e que ao final do programa,
#apresente apenas o nome e a nota da vencedora






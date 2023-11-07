#Exercícios  em Python 
#Calcule a media de um número desconhecido de pessoas
n_pessoas = int(input("Digite o número de pessoas: "))
soma = 0
for _i in range (n_pessoas):
  idade = int(input("Qual a idade da pessoas?"))
  soma += idade
media = int(soma/n_pessoas)
print("A média das idade é", media," anos.")

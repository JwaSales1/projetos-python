#tipo Float

#Tipo real, decimal

#casas decimais

#obs: O separados de casas decimais na programacao e o ponto e nao a vírgula

#Errado
Valor = 1, 44
print (type(valor))
#Errado do ponto de vista do float, mas gera uma dupla

#certo
valor = 1.44
print(valor)
print(type(valor))
#é Possivel no ponto de vista do Float
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Podermos converter um float para um int
#OBS: Ao converter valores float para inteiros, perdemos precisão
resultado = int(valor)
print(res)
print(type(res))

#Números complexos
Variavel = 5j
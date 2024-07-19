#Exemplo
def saudacao(nome):
    print(f"Olá,{nome}!")

print("\n Chamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")

#funcao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado
print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado da função quadrado:", resultado_quadrado)

#Funcao com multiplos parametros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\n chamando a função soma : ")
numero1= 20
numero2= 50
resultado_soma = soma(numero1,numero2)
print("A soma do numero %s e o numero %s é %s" %(numero1,numero2,resultado_soma))
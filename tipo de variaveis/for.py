print("For ultilizando lista")
lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)

print("For ultilizando tupla")
tupla =(1,2,3,4,5)
for elemento in tupla:
    print(tupla)

print("For ultilizando dicionario - chaves")

pessoa ={"nome": "Jorge","Idade": 23 , "Cidade":"Brasilia"}
for chave in pessoa.keys():
    print(chave)
print("For ultilizando dicionario - valor")
for valor in pessoa.values():
    print(valor)
    
    print("\nFor ultilizando dicionario - itens")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
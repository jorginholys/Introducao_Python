#CRIANDO UM DICICÍONARIO DE EXEMPLO
pessoa = {"nome":"Jorge", "idade": 30 , "cidade": "São Paulo"}
print("Meu dicionário de exemplo:",pessoa)

#Acessando Valores por chave 
print("Nome:", pessoa["nome"])
print("Nome:", pessoa["idade"])
pessoa["sobrenome"] = "Luis"
print("Nome:", pessoa["cidade"])
print("sobrenome:", pessoa["sobrenome"])

print("Meu dicionário de exemplo:",pessoa)

#Removendo um par chave-valor
del pessoa["sobrenome"]

print("Meu dicionário de exemplo:",pessoa)

#Métodos keys(), values(), itens()
chaves = list(pessoa.keys())
print("Chaves do dicionário" , chaves)
print("Primeira chave:" , chaves[0])

#método values
valores = list(pessoa.values())
print("valores do dicionário" , valores)
print("Primeiro valor do dicionario :" , valores[0])

#método items

itens = list(pessoa.items())
print("Pares chave-valor do dicionário" , itens)
print("Primeira chave-valor: %s = %s " %(itens[0][0], itens [0][1]))




#if, elif e else

#exemplo de "if" 

idade = 18
print("Exemplo de comando if")
if idade >=18:
    print("voce é maior de idade")
elif idade >= 12 :
    print("Você é adolescente")
else: 
    print("Você é menor de idade.")

mensagem = "Pode tirar carteira de motorista" if idade >= 18 else "Você não pode tirar carteira de motorista"
print(mensagem)
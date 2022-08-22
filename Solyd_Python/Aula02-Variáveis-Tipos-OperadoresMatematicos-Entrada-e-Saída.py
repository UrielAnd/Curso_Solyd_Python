print("primeiro print")
print("segundo print\nterceiro print")

nome = "Uriel"
sobrenome = "Andrade"
idade = 20
altura = 1.76

print(nome,sobrenome)
print(idade,altura)

tipo = type(nome)

print(type(nome))
print(type(idade))
print(type(altura))
print(type(tipo))

print("teste "+nome +" "+str(idade)) #str(variável) *Converte variável em str(string)

pergunta = input("Digite uma pergunta: ")
print(pergunta)

resposta = input("Digite a resposta da pergunta: ")  #Input captura os dados do teclado
print(resposta)

print(type(pergunta))
print(type(resposta))
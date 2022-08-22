lista = ["Samuel", "Silvânia"]  #A lista é mutavel e variável CHAMADO -> (LIST)
tupla = ("Charles", "Uriel")  #A tupla em python não é mutavel igual a lista | Ela sempre terá o mesmo números de itens dentro , más se pode variar o conteúdo que ja se tem nela apenas substituindo ela toda.  CHAMADO -> (TUPLE)
dicionario = {"nome": "Guilherme", "idade": 27}  #É proposto com uma chave e valor, muito parecido com arquivo json.Ele é mutável e variádo  CHAMADO -> (DICT)      |Útil para buscas|   
             # Chave     Valor  |  Chave   Valor
             # Isso é um item so|Isso é outro item
conjunto = {"Gui","Jão"}   #No conjunto não se pode ter itens repetidos e pode ser mutavel e variádo. Também ele não é ordenado como os indices 0,1,...   CHAMADO -> (SET)      

#Pode se usar o for em qualquer tipo de coleção ^^

print(tupla)
print(tupla[0])

#Pode se usar o not(não está dentro) ao invés do in(está dentro) nesse tipo de if e no for que percorre uma coleção
if "Charles" in tupla:  #Acontece se Chales estiver dentro da tupla **Serve para todas as coleções mas para dicionario se aplica diferente, colocando .values no nome do dicionario antes**
    print("TEM")

print(dicionario)

print(dicionario["nome"])  #Ao inves de passar o índice se passa a chave, revelendo o conteúdo

if "Guilherme" in dicionario.values():  #Exemplo dicionario buscando conteúdo .values(valor)  .keys(Chaves  **O for também é assim**
        print("TEM GUI")

dicionario["nome"] = "igor"     #Troca o valor da chave nome do dicionario

dicionario["cpf"] = "359723457834"  #Adiciona no dicionario quando não se tem a chave

print(dicionario["nome"])
print(dicionario["cpf"])
#O Dicionário é mais rapido que a lista

print(conjunto)

conjunto.add("Gabriel") #É adicionado porque não existe
conjunto.add("henrique")
conjunto.add("Gui")     #Não é adicionado porque já exixte

print(conjunto)
#O conjunto é mais rapido que a lista

conjunto.remove("Gui")
print(conjunto)

#INICIALIZAR VAZIO
#lista = []
#tupla = ()
#dicionario = {}
#conjunto = {}
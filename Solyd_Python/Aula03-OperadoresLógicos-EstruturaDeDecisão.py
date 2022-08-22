from traceback import print_tb


verdade = True
falso = False

print(type(falso),type(verdade))
print(falso)

if verdade == True:
    print("ISSO É VERDADE")
if falso == False:
    print("ISSO É MENTIRA")

if falso == False and verdade == True:  #Operadores logicos são pelos nomes (and, or, not) e não simbolos
    print("TESTE\tTESTE")   #\t é tab

if verdade == False:
    print("VERD")
elif falso == False:    #elif == else if em python
    print("FALS")
else:
    print("Nenh")        

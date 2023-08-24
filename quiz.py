print("Seja muito bem vindo!")
answer_user = input("Quer começar? ")
if answer_user != "s":
    quit()
score = 0


print("Quando começou a primeira guerra mundial?\n a) 1910 \n b) 1947 \n c) 1914")
answer_1 = input("Resposta: ")

if answer_1 == "c":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")



print("Qual é a civilização mais antiga do mundo? \n (a) Suméria \n (b) Mesoamericana \n (c) Egípcia")
answer_2 = input("Resposta: ")

if answer_2 == "a":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")




print("Em que ano John F. Kennedy foi assassinado? \n a) 1970 \n b) 1963 \n c) 1962 ")
answer_3 = input("Resposta: ")

if answer_3 == "b":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")



print(f"Quiz acabou...: {score}/3")
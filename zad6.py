with open("zadanie6.txt","w") as f:
    lista=[]
    for i in range(10):
        lista.append(input("wpisz liczbe "))
        print(lista)
    print("Finalowa lista wpisanych liczb zostala dodana do pliku")
    f.write(str(lista) + "\n")

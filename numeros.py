def patito(numero):
    for i in range(numero, 0, -1):
        print(str(i).zfill(len(str(numero))))

patito(1000)




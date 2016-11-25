def interpretar_comandos():
    comando = ''
    while (comando != 'salir'):
        comando = input("=>")
        if ("imprimir" in comando):
            result = comando.split("'")
            result = result[1]
            print(result)
        if ("para" in comando):
            result = comando.split(" ")
            print(result)
            #for i in result[2]


print(interpretar_comandos())
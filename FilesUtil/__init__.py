def criar_txt(name, cont):
    with open(f'{name}.txt','a') as arquivo:
        arquivo.write(str(cont))

def mod_txt(arquivo, cont):
    arquivo = open(f"{arquivo}.txt", "a")
    arquivo.write('\n')
    arquivo.write(str(cont))
    arquivo.close()
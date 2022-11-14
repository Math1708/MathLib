def fat(num):
    nums = []
    result = 1
    num_list = -1
    var = int

    while True:
        if num > 1:
            nums.append(num)
            num = num - 1
        if num <= 1:
            break

    for n in nums:
        result = result * n
    return result

def nums_primos(m):
    import os
    import time

    num = 0
    numeros_primos = []
    inicio = time.time()


    def cmd(command):
        os.system(command)

    cmd('cls')
    for c in range(2, m):
        if c != 2 and c != 3 and c != 5 and c != 7:
            if (c % 2) != 0 and (c % 3) != 0 and (c % 5) != 0 and (c % 7) != 0:
                num = num + 1
                p = (c / m) * 100
                print(f"[\033[42;1;33m{c}\033[m] - Encontrando números primos...        {p:.1f}")
                numeros_primos.append(c)
            else:
                p = (c / m) * 100
                print(f"[{c}] -  Encontrando números primos...        {p:.1f}")
                pass   

        if c == 2 or c == 5 or c == 7 or c == 3:
            p = (c / m) * 100
            print(f"[\033[42;1;33m{c}\033[m] -  Encontrando números primos...        {p:.1f}")
            num = num + 1
            numeros_primos.append(c)
        if c == 1:
            p = (c / m) * 100
            print(f"[{c}] -  Encontrando números primos...        {p:.1f}")
            pass

    fim = time.time()
    delta = (fim - inicio) / 60
    pps = num / delta

    cmd('cls')

    print(f"{num} números primos encontrados.")
    print(f"Tempo de execução: {delta:.1f} minutos")
    print(f"A média de números primos encontrados por minuto foi de {pps:.2f} ")

    with open(f'numeros_primos{num}.txt','w') as arquivo:
        for valor in numeros_primos:
            arquivo.write(str(valor) + '\n')
    arquivo.close(

    )

def nums_primos_time(m):
    import os
    import time

    c = 0

    loop = 100

    num = 0
    numeros_primos = []
    inicio = time.time()

    def cmd(command):
        os.system(command)

    cmd('cls')
    while True:
        c = c + 1
        if c != 2 and c != 3 and c != 5 and c != 7:
            if (c % 2) != 0 and (c % 3) != 0 and (c % 5) != 0 and (c % 7) != 0:
                num = num + 1
                p = (c / m) * 100
                print(f"[\033[42;1;33m{c}\033[m] - Encontrando números primos...        {p:.1f}")
                numeros_primos.append(c)
                if ((time.time() - inicio)/60) >= m:
                    break
                else:
                    pass
            else:
                p = (c / m) * 100
                print(f"[{c}] -  Encontrando números primos...        {p:.1f}")
                if ((time.time() - inicio)/60) >= m:
                    break
                else:
                    pass   

        if c == 2 or c == 5 or c == 7 or c == 3:
            p = (c / m) * 100
            print(f"[\033[42;1;33m{c}\033[m] -  Encontrando números primos...        {p:.1f}")
            num = num + 1
            numeros_primos.append(c)
            if ((time.time() - inicio)/60) >= m:
                break
            else:
                pass
        if c == 1:
            p = (c / m) * 100
            print(f"[{c}] -  Encontrando números primos...        {p:.1f}")
            if ((time.time() - inicio)/60) >= m:
                break
            else:
                loop = loop + 1
            pass

    fim = time.time()
    delta = (fim - inicio) / 60
    pps = num / delta

    cmd('cls')

    print(f"{num} números primos encontrados.")
    print(f"Tempo de execução: {delta:.1f} minutos")
    print(f"A média de números primos encontrados por minuto foi de {pps:.2f} ")

    with open(f'numeros_primos.txt','w') as arquivo:
        for valor in numeros_primos:
            arquivo.write(str(valor) + '\n')
    arquivo.close()
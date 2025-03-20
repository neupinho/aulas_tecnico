

print("----------Olá, Bem vindo a escada de marmore XD---------")
nome = input("me chamo zezinha, digite seu nome: ")
idade = int(input("digite sua idade em números: "))

if idade < 18:
    print(f'Desculpa {nome}, tu tem idade pra entrar aqui não, da meia volta')

if idade >= 18:
    print("cuidado onde você anda")
    print("temos alguns comandos,diga 'cansei' para sair da escada de marmore")

    while True:
        comandos = input()
        suspeita = False
        acertei = False
        if "cansei" in comandos:
            print("aula de Laura agora ne")
            break
        if "aloo" in comandos:
            print("barulhos altos de beijo*")
            if suspeita == False:
                suspeita = True
        if "achei voce safadinha" in comandos:
            print("meu deus, essa fernanda e fernando")
            if suspeita == False:
                suspeita = True
                acertei = True
        if "leticia" and "leo" in comandos:
            print("MEU DEUS LETICIA TU NAO ERA SAPATAO????")
            acertei = True
        if "meu deus nao acredito" in comandos:
            print("acho que achei algo interessante")
            suspeita = True
        if "lixo" in comandos:
            print("lixo ta la na sala")
            if suspeita == True:
                suspeita = False
        if "marta" in comandos:
            print("que saudades de tia marta")
        if "camisinha" in comandos:
            print("KKKKKKKK que horror fizeram atos aqui, sem noção")
            
        if "fone" in comandos:
            print("ACHEI MEU FONE ROUBADO")

        if suspeita and acertei == True:
            print("eu confirmei minhas suspeitas")
            print("muito bom o dia de hoje, descobri varias coisas")
            break
            suspeita = False
            acertei = False

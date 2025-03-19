

print("----------Olá, Bem vindo a escada de marmore XD---------")
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
        suspeita = True
    if "achei voce safadinha" in comandos:
        print("meu deus, essa fernanda e fernando")
        acertei = True
    if "leticia" and "leo" in comandos:
        print("MEU DEUS LETICIA TU NAO ERA SAPATAO????")
    if "meu deus nao acredito" in comandos:
        print("miguel e felipe se pegando omgg")
    if "raquel" and "gabriel" in comandos:
        print("KKKKK supera esses 2 visse")
    if "boquinha" and "neto" in comandos:
        print("é só amizade, abestalhado")
    if "camisinha" in comandos:
        print("KKKKKKKK que horror fizeram atos aqui, sem noção")
    if "fone" in comandos:
        print("OMGGG ACHEI")

    if suspeita and acertei == True:
        print("meu deus eu confirmei minhas suspeitas")
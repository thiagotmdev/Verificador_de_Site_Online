import requests

print("Bem vindo ao Verificador de sites 1.0! \nInsira as URLs dos sites que deseja verificar o status. (Separados por vírgula)\n")


def add_url():
    url = input("Digite uma URL: ")
    url_lower = url.lower()
    url_split = url_lower.split(", ")
    url_split > []
    return verifica_site(url_split)


def verifica_site(list):
    for l in list:
        if "." in l:
            try:
                url = l
                url_p = l.replace(url, "http://" + l)
                r_url = requests.get(url_p)
                code = r_url.status_code
                if code == 200:
                    print(url_p, "Site Online")
                elif code != 200:
                    print(url_p, "Site não encontrado")
            except:
                print(url, "Site Offline")
        else:
            print(l, "Site Inválido")

    o = input("Deseja fazer mais uma verificação? s (SIM) ou n (NÂO): ")
    return options(o.lower())


def options(option):
    if option == "s":
        return add_url()
    elif option == "n":
        return print("Aplicação encerrada")
    elif option != "s" or "n":
        return print(options(input("Digite um valor válido: ")))


add_url()

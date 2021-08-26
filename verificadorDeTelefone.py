# encontrar informações básicas de um número de telefone
import phonenumbers
from phonenumbers import geocoder


def indentify(numero):
    phone = phonenumbers.parse(numero)
    print(f"O telefone informado é da cidade + estado: {geocoder.description_for_number(phone, 'pt')}")



if __name__ == '__main__':
    try:
        telefone = input('Informe o número no formato +55... \n')
        if len(telefone) <= 14:
            indentify(telefone)
        else:
            print('Formato incorreto')
    except ValueError:
        pass

import requests
import json

def get_cotacao(destino = 'BRL'):

    url = 'https://api.exchangerate-api.com/v4/latest/' + destino

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        return data['rates']

    else:
        print('Erro ao obter cotações: ', response.status_code)
        return None

def converter_cotacao(origem = 'USD', destino = 'BRL', valor = 1):
    rates = get_cotacao(destino)
    return round(valor / rates[origem], 2)

def menu():
    print()
    print('1 - Converter Dólar em Real')
    print('2 - Converter Euro em Real')
    print('3 - Converter Libras em Real')
    print('4 - Outra cotação')
    print('0 - Sair')
    print()

#menu()
    
opcao = 1
while opcao != 0:
     menu()
     opcao = int(input('Escolha uma opção: '))

     destino = 'BRL'
     valor = int(input('Digite o valor: '))

     match opcao:
         case 1: origem = 'USD'

         case 2: origem = 'EUR'

         case 3: origem = 'GBP'

         case 4:
             origem = input('Digite a origem: ') 
             destino = input('Digite o destino: ')
        
     if opcao:        
        print()
        print('**********************************************************')
        print(f'{origem} para {destino}: ' , converter_cotacao(origem, destino, valor))
        print('**********************************************************')
        print()
             







#print(converter_cotacao())
#print(get_cotacao())








#rates = get_cotacao()  
#print('USD:', 1 / rates['USD'])
#print('EUR:', 1 / rates['EUR'])
#print('GBP:', 1 / rates['GBP'])        
 
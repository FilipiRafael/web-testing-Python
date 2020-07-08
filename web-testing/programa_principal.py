# Importando a biblioteca urllib.request
# Esta biblioteca que trará a capacidade para o nosso programa de requisitar a conexão de uma URL na web

import urllib.request

def testar_website(site):

    try:
        site = urllib.request.urlopen(site)

        # Aqui você pode colocar qualquer URL, caso o site obtenha SSL, poderá apenas alterar o "http://" para "https://".
        # Impressindível colocar o prefixo http.

    except urllib.error.URLError:

        print("Erro na conexão com a internet ou a URL não foi encontrada")

        # Irá imprimir esta mensagem caso a conexão não consiga ser estabelecida ou a URL informada não seja encontrada

    else:

        # Por fim, com tudo sendo executado corretamente, esta mensagem será impressa

        print("Conexão estabelecida com sucesso!")

        # print(site.read()) - Esta função "read()" irá realizar a leitura das informações do site em html

        # Bom, assim você saberá que o site pesquisado está realmente no ar!


site = str(input('Digite o nome do site a qual deseja pesquisar [Necessário utilizar o http]: '))
testar_website(site)

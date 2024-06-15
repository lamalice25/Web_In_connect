import requests as re

def recup():



    while True:
        url = input("Le site peut etre en http ou https le test fonctionera aussi\n\n tape 'q' pour quitter\n\nEntrer l'url du sites : ")

        if url == "q":
            break
        else:
            response = re.get(url)
            indexing = response.text
            print(indexing)
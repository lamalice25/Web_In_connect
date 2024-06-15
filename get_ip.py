import os as cmd

def get_ip():
    print('voici les exemples a faire pour que sa marche : \n\n Les lien : https://youtube.com ou le domain : youtube.com')
    while True:
        
        IP = input('Tape "q" pour quitter\n\nEntrer le lien ou nom de domain: ')

        if IP == "q":
            break
        
        else:
            cmd.system(f"nslookup {IP}")
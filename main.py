import os

if os.name != "nt" :
    print('Your device is not supported...')
    exit()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colorama import init, Fore, Back, Style
from message_content import message, html_content, text_content


import smtplib
import json

def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL,back=Back.BLACK, **kwargs):
    print(f"{brightness}{color}{back}{s}{Style.RESET_ALL}", **kwargs)

fileObject = open("account.json", "r")
jsonContent = fileObject.read()
credentials = json.loads(jsonContent)

mail = credentials['email']
passwd = credentials['password']


def get_port():
    port = input('Sur quel port voulez vous lancer la connexion ? [default : 587] >> ')

    if port == '' :
        port = 587
        return port
    elif port != 587 :
        return port
    else :
        return int(port)

def print_subscribed() :
    os.system('cls')

    fileObject = open("subscribed.json", "r")
    jsonContent = fileObject.read()
    obj_python = json.loads(jsonContent)
    try :
        for elem in (obj_python['subscribed']):
                print('+ '+ elem)
    except :
        print('Aucun email enregistré trouvé...')


    os.system('pause')
    os.system('cls')
    menu()

def get_server():
    serv = input('Adresse du serveur SMTP [default : smtp.gmail.com](Appuyer sur entrée pour def.) >> ')
    if serv == '' :
        serv = "smtp.gmail.com"
        return serv
    else :
        return serv

def get_message():
    os.system('notepad ./message_content/message.py')

    return message.message_to_send

def get_subscribed():
    fileObject = open("subscribed.json", "r")
    jsonContent = fileObject.read()
    obj_python = json.loads(jsonContent)
    subscribed = obj_python['subscribed']

    return subscribed

def send_email():
    smtp_server = get_server()
    port = get_port()
    mess = get_message()
    subscribed = get_subscribed()

    try :
        connection = smtplib.SMTP(f"{smtp_server}",587)
        print(print_with_color(f'[*] Connecté avec succès à {smtp_server} sur le port {port}',Fore.GREEN,Style.BRIGHT))
        connection.starttls()
    except :
        print(print_with_color(f'Une erreur est survenue lors de la connexion à ({smtp_server}) sur le port {port}...',Fore.RED,Style.BRIGHT))
        os.system('pause')
        main()

    try :
        connection.login(user = mail, password = passwd)
        print(print_with_color('[*] Connecté avec succès !',Fore.GREEN,Style.BRIGHT))
    except :
        print(print_with_color(f'Une erreur est survenue lors de la connexion à ({mail})...',Fore.RED,Style.BRIGHT))
        os.system('pause')
        main()

    for elem in subscribed :
        try :
            connection.sendmail(from_addr = mail, to_addrs= elem, msg = mess )
            print(print_with_color('---------------------------------------------------------------------------------',Fore.GREEN,Style.BRIGHT))
            print(print_with_color(f'[*] Mail envoyé avec succès à {elem} depuis {mail} !',Fore.GREEN,Style.BRIGHT))
            print(print_with_color('---------------------------------------------------------------------------------',Fore.GREEN,Style.BRIGHT))
        except :
            print(print_with_color('Votre message n\'a pas pu être envoyé...',Fore.RED,Style.BRIGHT))
            os.system('pause')
            main()

    connection.close()
    print(print_with_color('[*] Connection closed ',Fore.BLUE,Style.BRIGHT))

def send_html():
    smtp_server = get_server()
    port = get_port()
    subscribed = get_subscribed()

    try :
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        print(print_with_color(f'[*] Connecté avec succès à {smtp_server} sur le port {port}',Fore.GREEN,Style.BRIGHT))
        mail.ehlo()
        mail.starttls()
    except :
        print(print_with_color(f'Une erreur est survenue lors de la connexion à ({smtp_server}) sur le port port {port}...',Fore.RED,Style.BRIGHT))
        os.system('pause')
        main()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = input('Subject >> ')
    msg['From'] = mail
    
    os.system('msg * Rentrer le message à rentrer en plain text dans la variable text (\\n pour un retour à la ligne)')
    os.system('notepad ./message_content/text.py')
    os.system('msg * Rentrer le message à rentrer sous forme de template html dans la variable html')
    os.system('notepad ./message_content/html.py')

    try :
        mail.login(user = mail, password = passwd)
        print(print_with_color('[*] Connecté avec succès !',Fore.GREEN,Style.BRIGHT))
    except :
        print(print_with_color(f'Une erreur est survenue lors de la connexion avec votre compte mail ({mail})...',Fore.RED,Style.BRIGHT))
        os.system('pause')
        main()

    msg.attach(part1)
    msg.attach(part2)
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    for elem in subscribed :
        msg['To'] = elem
        
        text = text_content.text
        html = html_content.html
        try :
            mail.sendmail(mail, elem, msg.as_string())
            print(print_with_color('---------------------------------------------------------------------------------',Fore.GREEN,Style.BRIGHT))
            print(print_with_color(f'[*] Mail envoyé avec succès à {elem} depuis {mail} !',Fore.GREEN,Style.BRIGHT))
            print(print_with_color('---------------------------------------------------------------------------------',Fore.GREEN,Style.BRIGHT))
        except :
            print(print_with_color('Votre message n\'a pas pu être envoyé...',Fore.RED,Style.BRIGHT))
            os.system('pause')
            main()
    mail.quit()

def menu():
    print('''

    
 ███╗   ██╗███████╗██╗    ██╗███████╗██╗     ███████╗████████╗████████╗███████╗██████╗ 
 ████╗  ██║██╔════╝██║    ██║██╔════╝██║     ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
 ██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗██║     █████╗     ██║      ██║   █████╗  ██████╔╝
 ██║╚██╗██║██╔══╝  ██║███╗██║╚════██║██║     ██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗
 ██║ ╚████║███████╗╚███╔███╔╝███████║███████╗███████╗   ██║      ██║   ███████╗██║  ██║
 ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
                                    - BSK Esport -                                                    
########################################################################################

    1) Envoyer un mail
    2) Envoyer un mail via un template HTML
    3) Afficher les emails inscrits à la newsletter
    E) Quitter

########################################################################################
    ''')

    choice = input('>> ')

    if choice == '1' :
        send_email()
    elif choice == '2' :
        send_html()
    elif choice == '3' :
        print_subscribed()
    elif choice == 'E' or choice == 'e' :
        bye()
    else :
        print('Veuillez entrer une proposition valide...')
        os.system('pause')
        os.system('cls')
        menu()

def bye():
    end = input('\n\nMerci d\'avoir utilisé ce programme voulez-vous quitter ? [Y/n] >> ')

    if end == 'N' or end == 'n' or end == 'no' :
        os.system('cls')
        main()
    elif end == 'Y' or end == 'y' or end == 'yes' :
        exit()
    elif end == '' :
        exit()
    else :
        print('Veuillez entrer une proposition valide...')
        os.system('pause')
        os.system('cls')
        main()

def main():
    os.system('cls')

    menu()

os.system('title Newsletter BSK')
main()
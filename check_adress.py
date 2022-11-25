import json

adress = input('Entrez adresse : ')

ext = ['laposte.net','gmail.com','hotmail.com','yahoo.com','outlook.com','live.com','msn.com','aol.com','icloud.com','orange.fr','wanadoo.fr','sfr.fr','bbox.fr','neuf.fr','gmx.fr','yahoo.fr','live.fr','laposte.fr','voila.fr','club-internet.fr','aliceadsl.fr','numericable.fr','free.fr','bouyguestelecom.fr','bbox.fr','neuf.fr','hotmail.fr']

def get_subscribed():
    fileObject = open("subscribed.json", "r")
    jsonContent = fileObject.read()
    obj_python = json.loads(jsonContent)
    subscribed = obj_python['subscribed']

    return subscribed

def exist(adress):
    new = get_subscribed()
    for elem in ext :
        if adress.endswith(elem) and adress not in new: 
            new.append(adress)
            json_text ={ "subscribed" : new}
            print('ok')
            try :
                with open('subscribed.json', 'w') as outfile :
                    json.dump(json_text, outfile, indent=4, ensure_ascii=False)

            except :
                    print('error while writing')
                    exit()
            exit()
        else :
            continue
    print('Ratio ^^')

exist(adress)
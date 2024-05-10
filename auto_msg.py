import asyncio
from telethon import TelegramClient
import logging
import configparser
import argparse
import time
from telethon.errors import ChatWriteForbiddenError

async def main():

    print("**********************************************************************************")
    print("*                                                                                *")
    print("*                 Telegram Auto_Msg Sender  By M_xcore7                          *")
    print("*                          Target App : Telegram                                 *")
    print("*                                                                                *")
    print("**********************************************************************************")

    config = configparser.ConfigParser()
    config.read('config.ini')

    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    phone_number = config['Telegram']['phone_number']

    client = TelegramClient('session', api_id, api_hash)

    if not phone_number:
        phone_number = input("Veuillez entrer votre numéro de téléphone : ")
        config['Telegram']['phone_number'] = phone_number
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    await client.start(phone_number)

    message_to_send = input("Veuillez entrer votre message : ")

    dialogs = await client.get_dialogs()
    time.sleep(1)
    print("Recuperation de la liste des groupe", end='', flush=True)
    time.sleep(0.3)  
    print("\rRecuperation de la liste des groupe", end='', flush=True)
    time.sleep(0.3)  
    print("\rRecuperation de la liste des groupe=>", end='', flush=True)
    time.sleep(0.3)  
    print("\rRecuperation de la liste des groupe===>", end='', flush=True)
    time.sleep(0.3)  
    print("\rRecuperation de la liste des groupe=====>", end='', flush=True)
    time.sleep(0.3)  
    print("\rRécupération de la liste des groupe======>", end='', flush=True)
    time.sleep(0.3)  
    print("\rRecuperation de la liste des groupe========>", end='', flush=True)
    time.sleep(0.3)  
    print("\rRécupération de la liste des groupe=========> 100%  ")
    print("====================================Liste récupérée avec succès============================")
    time.sleep(1)
    print("Liste des groupes disponibles :")
    for i, dialog in enumerate(dialogs, start=1):
        if dialog.is_group:
            print(f"{i}. {dialog.title}")

   
    group_choices = input("Entrez les numéros des groupes séparés par des virgules (0 pour tous les groupes) : ")
    group_choices = [int(x.strip()) for x in group_choices.split(",")]
    temps_attente = int(input("Entrez le temps d'attente entre l'envoi dans chaque groupe ( en seconde) : "))
    temps_attente_repetition = int(input("Entrez le temps d'attente avant de reparcourir les groupes ( en seconde) : "))

    if 0 in group_choices:
        group_choices = range(1, len(dialogs) + 1)
    
    print("***************************************Lancement************************************************")

    while True:
        for i, dialog in enumerate(dialogs, start=1):
            if dialog.is_group and i in group_choices:
                try:
                    await client.send_message(dialog, message_to_send)
                    print(f"Message envoyé dans le groupe '{dialog.title}'.")
                except ChatWriteForbiddenError:
                    print(f"Envoi non autorisé dans le groupe '{dialog.title}'.")
                    continue
                time.sleep(temps_attente) 

        print(f"Attente de {temps_attente_repetition } secondes avant de recommencer...")
        time.sleep(temps_attente_repetition)



if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

    asyncio.run(main())

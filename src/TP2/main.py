from datetime import datetime
import pytz
import logging
import sys
import os


def get_fichier_sortie_args():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "traitement.log"


def get_fichier_sortie_env():
    from dotenv import load_dotenv
    load_dotenv()
    if os.environ["CHEMIN_FICHIER_LOG"] is not None:
        return os.environ["CHEMIN_FICHIER_LOG"]
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "traitement.log"


def get_fichier_sortie():
    return get_fichier_sortie_args()


timezone = pytz.timezone('Europe/Paris')

logging.basicConfig(filename="traitement.log", encoding='utf-8',
                    level=logging.DEBUG)
logging.info("Lancement du traitement")
logging.debug(f"Demande d'heure sur le timezone : {timezone}")

if timezone is None:
    logging.error("aucune timezone n'a été renseignée")
    raise ValueError("aucune timezone n'a été renseignée")

timezone_paris = pytz.timezone('Europe/Paris')
timezone_reunion = pytz.timezone('Indian/Reunion')


def get_date_formatted(timezone):
    date = datetime.now(timezone)
    return date.strftime("%H:%M:%S")


print(get_date_formatted(timezone_paris))
print(get_date_formatted(timezone_reunion))

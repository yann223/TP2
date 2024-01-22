from datetime import datetime
import pytz
import logging

timezone = pytz.timezone('Europe/Paris')

logging.basicConfig(filename=None, encoding='utf-8', level=logging.DEBUG)
logging.info(f"Lancement du traitement")
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
#Licenced under MIT License
#charset = "utf-8"
#Language = "Python3"
#Bot Framework = "python-telegram-bot"
#The Code is without Proxy, Actual code contains Proxy
#Proxy should be used is of the type SOCKS5
#Special thanks to cyberboySumanjay
#The bot will work till you press ctrl+c in the terminal or command line.,

#import the required files
import requests
import logging
from telegram import *
from telegram.ext import *

#enable logger (optional)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "Your Token Here"


#CommandHandler to get torrents for the query
def find(update: Update, context: CallbackContext) -> None:
    try:
        update.message.reply_text("Searching results for 👉{}👈".format(update.message.text))
        #yts api
        url = "https://api.api-zero.workers.dev/yts/{}".format(update.message.text)
        results = requests.get(url).json()
        print(results)
        for item in results:
            name = item.get('Name')
            up = item.get('ReleasedDate')
            gen = item.get('Genre')
            rat = item.get('Rating')
            time = item.get('Runtime')
            img = item.get('Poster')
            lnk1 = item.get('Dwnload1')
            lnk2 = item.get('Download2')
            lnk3 = item.get('Download3')
            update.message.reply_text(f"""*➲Name:* `{name}`
Released on {up}
Watch Time {time}
*Genre:* {gen}
*Rating:* {rat}
*Poster:* {img}
*Link1:* `{lnk3}`
*Link2:* `{lnk1}`
*Link3:* `{lnk2}`""", parse_mode=ParseMode.MARKDOWN)
        update.message.reply_text("End of Results")
    except:
        update.message.reply_text("""Search Completed""")


#Add all handlers to the main function.
def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), find))
    updater.start_polling() #set bot to polling, if you use webhooks, replace this statement with the url of webhook.,
    updater.idle()

#Call the main function
if __name__ == '__main__':
    main()

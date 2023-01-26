import telebot
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


API_KEY = "APIKEYAPIKEYAPIKEYAPIKEY"
bot=telebot.TeleBot(API_KEY, parse_mode=None)
@bot.message_handler(commands=["ctf"])
def send_message(msg):
    url = 'https://ctftime.org/event/list/upcoming'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.103 Safari/537.36'}
    page = requests.get(url, headers=header)
    soup = bs(page.text, 'lxml')
    table_body = soup.find('table')
    row_data = []
    for row in table_body.find_all('tr'):
        col = row.find_all('td')
        col = [ele.text.strip() for ele in col]
        row_data.append(col)
    df = pd.DataFrame(row_data)
    dfdf = df.iloc[1:6, 0:2]
    vivod = dfdf.set_index(1).to_markdown(tablefmt="presto", headers=["Название и дата CTF"])
    bot.reply_to(msg, "" + vivod)
bot.polling()

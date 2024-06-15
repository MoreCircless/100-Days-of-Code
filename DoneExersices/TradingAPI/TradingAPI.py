import requests
from datetime import datetime, timedelta
from colorama import init, Fore

init(autoreset=True)

STOCK_NAME = "BTC"
COMPANY_NAME = "Bitcoin"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "OWIDLYKS6DTVL4G4"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "135f55c35ac3483093db8b835cec0011"


stock_rq = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&interval=5min&apikey={STOCK_KEY}")
stock_ft = stock_rq.json()

last_refresh = stock_ft["Meta Data"]["3. Last Refreshed"] 
one_day = timedelta(days=1)
close_value = stock_ft["Time Series (Daily)"][last_refresh]["4. close"]
last_refresh_ft = datetime.strptime(last_refresh, "%Y-%m-%d")
bf_close_value = stock_ft["Time Series (Daily)"][f"{last_refresh_ft.date() - timedelta(days=1)}"]["4. close"]


change = abs(float(close_value) - float(bf_close_value))
change_ptg = (float(change)/float(bf_close_value) * 100)


if close_value > bf_close_value: 
    print(Fore.GREEN + f"{COMPANY_NAME} stock {last_refresh}: \n   NASDAQ: {STOCK_NAME} 🔺 {change_ptg:.2f} %")
else: 
    print(Fore.RED + f"{COMPANY_NAME} stock {last_refresh}: \n   NASDAQ: {STOCK_NAME} 🔻 {change_ptg:.2f} %")

news_call = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_KEY}")
news_call = news_call.json()


print("\n\nNEWS!\n")
for n in range(3):
    print(f"{news_call["articles"][n]["title"]}\n{news_call["articles"][n]["description"]}\nSource: {news_call["articles"][0]["url"]}\n")




import requests
from datetime import datetime, timedelta
from colorama import init, Fore

init(autoreset=True)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "OWIDLYKS6DTVL4G4"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "135f55c35ac3483093db8b835cec0011"


stock_rq = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&interval=5min&apikey={STOCK_KEY}")
stock_ft = stock_rq.json()

last_refresh = stock_ft["Meta Data"]["3. Last Refreshed"] # Date of the last refresh
one_day = timedelta(days=1)
close_value = stock_ft["Time Series (Daily)"][last_refresh]["4. close"]
last_refresh_ft = datetime.strptime(last_refresh, "%Y-%m-%d")
bf_close_value = stock_ft["Time Series (Daily)"][f"{last_refresh_ft.date() - timedelta(days=1)}"]["4. close"]


close_value = 177.4800
bf_close_value = 190
last_refresh = "2024-6-6"


change = abs(close_value - bf_close_value)
change_ptg = (change/bf_close_value * 100)


if close_value > bf_close_value: 
    print(Fore.GREEN + f"{COMPANY_NAME} stock {last_refresh}: \n   NASDAQ: TSLA 🔺 {change_ptg:.2f} %")
else: 
    print(Fore.RED + f"{COMPANY_NAME} stock {last_refresh}: \n   NASDAQ: TSLA 🔻 {change_ptg:.2f} %")

news_call = requests.get(f"https://newsapi.org/v2/everything?q=tesla&apiKey={NEWS_KEY}")
news_call = news_call.json()

if change_ptg >= 5:
    print("\n\nNEWS!\n")
    for n in range(3):
        print(f"{news_call["articles"][n]["title"]}\n{news_call["articles"][n]["description"]}\nSource: {news_call["articles"][0]["url"]}\n")




import requests
import json
data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

questions = data.json()

question_data = questions["results"]

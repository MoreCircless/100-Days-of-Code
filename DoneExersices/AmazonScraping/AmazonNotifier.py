import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
info = BeautifulSoup(data, "lxml.parser")
print(info.title)

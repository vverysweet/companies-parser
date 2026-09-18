from bs4 import BeautifulSoup
import pandas as pd
import re

str ="""<div class="company">
    <h3>Оптика №1</h3>
    <p class="address">Минск, ул. Ленина 5</p>
    <p class="phone">+375 29 123-45-67</p>
    <p class="hours">9:00-21:00</p>
</div>"""
soup = BeautifulSoup(str, "html.parser")


baza = {"Название": [], "Адрес": [], "Телефон": [], "Время работы": []}

for cp in soup.find_all(class_="company"):
    baza["Название"].append(cp.find("h3").text)
    baza["Адрес"].append(cp.find(class_="address").text)
    phone = cp.find(class_="phone").text
    phone = re.sub(r"\D", "", phone)
    baza["Телефон"].append(phone)
    baza["Время работы"].append(cp.find(class_="hours").text)

df = pd.DataFrame(baza)

df = df.drop_duplicates()

df.to_excel("baza.xlsx", index=False)
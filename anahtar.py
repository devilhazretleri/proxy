import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Web sayfasının URL'si
url = 'http://www.mersinmavim.com'

# Sayfanın içeriğini çekme
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Metni çekme ve düzenleme
text = soup.get_text()
text = re.sub(r'[^a-zA-ZğüşöçİĞÜŞÖÇ ]', '', text)
words = text.lower().split()

# Kelime sıklığını hesaplama
counter = Counter(words)

# En sık kullanılan 10 kelimeyi bulma
most_common = counter.most_common(10)
print(most_common)

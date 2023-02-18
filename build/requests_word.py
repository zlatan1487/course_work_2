import requests

# загрузка списка json из внешнего ресурса "json keeper" с расширенным вариантом слов.
list_words = requests.get('https://www.jsonkeeper.com/b/61YI')
data = list_words.json()

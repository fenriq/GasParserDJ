# Парсер цен на бензин
# Импорт библиотеки для работы с url
import requests
from datetime import date


# Определение функции для очистки строки


def cleaner(cline):
    cline = cline.replace('<td>', '')
    cline = cline.replace('</td>', '')
    s_line = float(cline)
    return s_line


# Получение нужной страницы в файл


st_accept = "text/html"
st_useragent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 "
                "Safari/605.1.15")
headers = {"Accept": st_accept, "User-Agent": st_useragent}

source = requests.get("https://driff.ru/fuel-dynamics/", headers)
page = source.text
page_text = open("./page.txt", 'w')
page_text.write(page)
page_text.close()

# Определение переменных:
# Искомые слова:
ai92 = "<td>АИ-92</td>"
ai95 = "<td>АИ-95</td>"
ai98 = "<td>АИ-98</td>"
# Индексы искомых записей в файле
ai92index = 0
ai95index = 0
ai98index = 0
# Списки всех найденных записей в файле
ai92found = []
ai95found = []
ai98found = []
today = date.today()
# Счетчик
n = 0

# Обработка файла:
page_text = open("./page.txt")
page_list = page_text.readlines()
page_text.close()
# Поиск совпадений по заданным названиям, запись найденных позиций в переменные
for line in page_list:
    n += 1
    if ai92 in line:
        ai92index = n + 1
        ai92found.append(ai92index)
    if ai95 in line:
        ai95index = n + 1
        ai95found.append(ai95index)
    if ai98 in line:
        ai98index = n + 1
        ai98found.append(ai98index)


# Назначение и очистка найденной строки
def liner():
    line92 = cleaner(page_list[ai92found[0]])
    line95 = cleaner(page_list[ai95found[0]])
    line98 = cleaner(page_list[ai98found[0]])
    return dict(ai92="line92", ai95="line95", ai98="line98")

# Предварительный вывод результата:
#print('Стоимость бензина(в среднем по популярным заправкам)')
#print(f'Данные на {today}: ')
#print(f'АИ-92: {line92} р\t АИ-95: {line95} р\t АИ-98: {line98}')

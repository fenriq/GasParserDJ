def liner():
    import requests
    # Получение нужной страницы в файл
    st_accept = "text/html"
    st_useragent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 "
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
    line92 = page_list[ai92found[0]]
    line92 = line92.replace('<td>', '')
    line92 = line92.replace('</td>', '')
    line92 = float(line92)
    line95 = page_list[ai95found[0]]
    line95 = line95.replace('<td>', '')
    line95 = line95.replace('</td>', '')
    line95 = float(line95)
    line98 = page_list[ai98found[0]]
    line98 = line98.replace('<td>', '')
    line98 = line98.replace('</td>', '')
    line98 = float(line98)
    return dict(ai92=line92, ai95=line95, ai98=line98)




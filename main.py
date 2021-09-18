# Author: Katashin Victor
# Будем использовать блочную модель
# Модуль, который парсит excel-расписание и выдает расписание под конкретную группу

import pandas as pd  # для работы с excel-файлами https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
from entities.table import Table


def start(schedule_path: str, group_name: str):
    """ Main function for schedule handler"""
    read_schedule = pd.read_excel(schedule_path)  # Читаем excel-файл с расписанием и грузим его в систему
    table = Table(table=read_schedule)  # Получаем объект класса таблицы


if __name__ == '__main__':
    g_name = "ИНМО-02-20"
    rasp_path = "C:/Users/Victor/Desktop/MIREASchedule/data/rasp.xlsx"
    start(schedule_path=rasp_path, group_name=g_name)



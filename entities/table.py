# Author: Katashin Victor
from pandas import DataFrame


class Table:
    """ Main class of excel table for schedule"""
    def __init__(self, table: DataFrame):
        self.__rows_count = 0           # Общее количество строк в таблице
        self.__columns_count = 0        # Общее количество столбцов в таблице
        self.table = table
        self.__research_column_count()  # Выводим общее количество колонок
        self.__research_rows_count()    # Выводим общее количество строк

    def __research_rows_count(self):
        """ Researches a rows count in the table"""
        self.__rows_count = len(self.table)

    def __research_column_count(self):
        """ Researches a column count in the table"""
        self.__columns_count = len(self.table.columns)

    def get_rows_and_columns_count(self) -> dict:
        """ Return rows and columns count value"""
        data = {
            "rows_count": self.__rows_count,
            "columns_count": self.__columns_count
        }
        print(f"Количество строк: {self.__rows_count}, столбцов {self.__columns_count}")
        return data

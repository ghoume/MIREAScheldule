# Author: Katashin Victor
# Вспомогательный класс для определения блока "День недели"
from entities.proportions import Proportions

days = {
    'Понедельник': {},
    'Вторник': {},
    'Среда': {},
    'Четверг': {},
    'Пятница': {},
    'Суббота': {}
}


class DaysOfWeek:
    """ Class describes a 'День недели' block"""
    def __init__(self, upper_bound: int, bottom_bound: int, left_bound: int, right_bound: int):
        self.__days_of_week = days
        # Устанавливаем основные размеры блока
        self.days_proportions = Proportions()
        self.days_proportions.set_bounds(upper_bound=upper_bound,
                                    bottom_bound=bottom_bound,
                                    left_bound=left_bound,
                                    right_bound=right_bound)

    def __get_days_of_week(self) -> dict:
        """ Return days of week dict"""
        return self.__days_of_week

    def get_days_of_week_block(self) -> dict:
        """ Getting a proportions DaysOfWeek block"""
        data = self.__get_days_of_week()

        bottom_bound = self.days_proportions.get_bounds()["bottom_bound"]
        upper_bound = self.days_proportions.get_bounds()["upper_bound"]
        right_bound = self.days_proportions.get_bounds()["right_bound"]
        left_bound = self.days_proportions.get_bounds()["left_bound"]

        height_difference = self.days_proportions.get_height_block(bottom_bound=bottom_bound, upper_bound=upper_bound)

        upper_border = upper_bound
        bottom_border = upper_border + height_difference

        for day in data.keys():
            data[day]["upper_bound"] = upper_border
            data[day]["bottom_bound"] = bottom_border
            data[day]["left_border"] = left_bound
            data[day]["right_border"] = right_bound
            upper_border = bottom_border
            bottom_border = bottom_border + height_difference
        return data

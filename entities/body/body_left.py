# Author: Katashin Victor
# Вспомогательный класс, разбирает группу полей: "День недели", "Группа" (номер пары, начало занятий,
# окончание занятий, неделя)
from entities.proportions import Proportions
from entities.body.days import DaysOfWeek
from entities.body.group import Group


days_block = {
    "upper": 2,
    "bottom": 20,
    "left": 0,
    "right": 1
}

group_block = {
    "upper": 1,
    "bottom": 20,
    "left": 1,
    "right": 5
}

body_left_block = {
    "upper": 1,
    "bottom": 105,
    "left": 0,
    "right": 5
}


class BodyLeft(DaysOfWeek, Group):
    """ Parse a group of next fields: Day, Group"""
    def __init__(self, upper_bound: int, bottom_bound: int, left_bound: int, right_bound: int):
        DaysOfWeek.__init__(self=self, upper_bound=days_block["upper"], bottom_bound=days_block["bottom"],
                            left_bound=days_block["left"], right_bound=days_block["right"])
        Group.__init__(self=self, upper_bound=group_block["upper"], bottom_bound=group_block["bottom"],
                       left_bound=group_block["left"], right_bound=group_block["right"])
        # Устанавливаем основные размеры блока
        self.body_proportions = Proportions()
        self.body_proportions.set_bounds(upper_bound=upper_bound, bottom_bound=bottom_bound,
                                         left_bound=left_bound, right_bound=right_bound)


bl = BodyLeft(upper_bound=body_left_block["upper"], bottom_bound=body_left_block["bottom"],
              left_bound=body_left_block["left"], right_bound=body_left_block["right"])

print(bl.get_days_of_week_block())

bl.set_group_bound()
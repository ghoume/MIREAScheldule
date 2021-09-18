# Author: Katashin Victor
# Вспомогательный класс для определения блока "День недели"
from entities.proportions import Proportions


group_bound = {
    "pair_number_block": {},
    "time_start_block": {},
    "time_end_block": {},
    "week_number_block": {}
}


class Group:
    """ Class describes a 'Группа' block"""
    def __init__(self, upper_bound: int, bottom_bound: int, left_bound: int, right_bound: int):
        self.group_data_bound = group_bound
        self.group_proportions = Proportions()
        self.group_proportions.set_bounds(upper_bound=upper_bound,
                                          bottom_bound=bottom_bound,
                                          left_bound=left_bound,
                                          right_bound=right_bound)

    def set_group_bound(self, step: int = 1):
        """ Filling group bound"""
        upper_bound = self.group_proportions.get_bounds()["upper_bound"]
        bottom_bound = self.group_proportions.get_bounds()["bottom_bound"]
        left_bound = self.group_proportions.get_bounds()["left_bound"]

        for item in self.group_data_bound.keys():
            right_bound = left_bound + step
            self.group_data_bound[item]["upper_bound"] = upper_bound + 1
            self.group_data_bound[item]["bottom_bound"] = bottom_bound
            self.group_data_bound[item]["left_bound"] = left_bound
            self.group_data_bound[item]["right_bound"] = right_bound
            left_bound = right_bound

        print(self.group_data_bound)

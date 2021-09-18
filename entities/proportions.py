# Author: Katashin Victor
# Вспомогательный класс для определения размеров блока
class Proportions:
    """ Supporting class for detecting size of block """
    def __init__(self):
        self.__upper_bound = 0   # Верхняя граница блока
        self.__bottom_bound = 0  # Нижняя граница блока
        self.__left_bound = 0    # Левая граница блока
        self.__right_bound = 0   # Правая граница блока

    def set_upper_bound(self, bound_value: int):
        """ Establish upper bound """
        self.__upper_bound = bound_value

    def set_bottom_bound(self, bound_value: int):
        """ Establish bottom bound """
        self.__bottom_bound = bound_value

    def set_right_bound(self, bound_value: int):
        """ Establish right bound """
        self.__right_bound = bound_value

    def set_left_bound(self, bound_value: int):
        """ Establish left bound """
        self.__left_bound = bound_value

    def set_bounds(self, upper_bound: int = 0, bottom_bound: int = 0, left_bound: int = 0, right_bound: int = 0):
        """ Establish all bounds """
        self.set_left_bound(left_bound)
        self.set_right_bound(right_bound)
        self.set_bottom_bound(bottom_bound)
        self.set_upper_bound(upper_bound)

    def get_bounds(self) -> dict:
        """ Function gets value of all bounds of dict format"""
        data = {
            "upper_bound": self.__upper_bound,
            "bottom_bound": self.__bottom_bound,
            "left_bound": self.__left_bound,
            "right_bound": self.__right_bound
        }
        return data

    @staticmethod
    def get_height_block(bottom_bound: int, upper_bound: int) -> int:
        """ Return height day block"""
        block_height = bottom_bound - upper_bound
        if block_height < 0:
            print("[Proportions] Height of block can't be < 0")
            return 0
        return block_height

    @staticmethod
    def get_weight_block(right_bound: int, left_bound: int) -> int:
        """ Return weight day block"""
        block_weight = right_bound - left_bound
        if block_weight < 0:
            print("[Proportions] Weight of block can't be < 0")
            return 0
        return block_weight

    @ staticmethod
    def get_dimensions_struct(weight: int = 0, height: int = 0) -> dict:
        """ Return weight and height dict struct"""
        dimensions_struct = {
            "weight": weight,
            "height": height
        }
        return dimensions_struct

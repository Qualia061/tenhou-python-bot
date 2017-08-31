# -*- coding: utf-8 -*-
from mahjong.hand_calculating.yaku import Yaku
from mahjong.utils import is_chi


class Iipeiko(Yaku):
    """
    Hand with two identical chi
    """

    def set_attributes(self):
        self.yaku_id = 7
        self.name = 'Iipeiko'

        self.han_open = None
        self.han_closed = 1

        self.is_yakuman = False

    def is_condition_met(self, hand, *args):
        chi_sets = [i for i in hand if is_chi(i)]

        count_of_identical_chi = 0
        for x in chi_sets:
            count = 0
            for y in chi_sets:
                if x == y:
                    count += 1
            if count > count_of_identical_chi:
                count_of_identical_chi = count

        return count_of_identical_chi >= 2

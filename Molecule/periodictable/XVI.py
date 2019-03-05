# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Dayana Bashirova <dayana.bashirova@yandex.ru>
#  This file is part of Molecule.
#
#  Molecule is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#
from .element import Element
from .periods import *


class GroupXVI:
    pass


class O(Element, PeriodI, GroupXVI):
    @property
    def atomic_number(self):
        return 8

    @property
    def atomic_mass(self):
        return 15.999

    @property
    def electronegativity(self):
        return 3.44

    @property
    def common_isotope(self):
        return 16

    @property
    def max_isotope(self):
        return 28

    @property
    def min_isotope(self):
        return 12

    @property
    def common_valences(self):
        return (2, 3),

    @property
    def valences_exceptions(self):
        return ((0, 2, (1, 'H')), (0, 2, (1, 'N')), (0, 2, (1, 'O')), (-1, 2, (1, 'H')), (-1, 2, (1, 'O')))

            #(0, 1, ((2, 'O'), (1, 'O')), (0, 2, (1, 'O')), (-1, 2, (1, '0')))


class S(Element, PeriodII, GroupXVI):
    @property
    def atomic_number(self):
        return 16

    @property
    def atomic_mass(self):
        return 32.059

    @property
    def electronegativity(self):
        return 2.58

    @property
    def common_isotope(self):
        return 32

    @property
    def max_isotope(self):
        return 49

    @property
    def min_isotope(self):
        return 26

    @property
    def common_valences(self):
        return (2, 3), (4, 2), (6, 3)

    @property
    def valences_exceptions(self):
        return ()


class Se(Element, PeriodIII, GroupXVI):
    @property
    def atomic_number(self):
        return 34

    @property
    def atomic_mass(self):
        return 78.96

    @property
    def electronegativity(self):
        return 2.55

    @property
    def common_isotope(self):
        return 80

    @property
    def max_isotope(self):
        return 95

    @property
    def min_isotope(self):
        return 64

    @property
    def common_valences(self):
        return (2, 3), (4, 2), (6, 3)

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupXVI', 'O', 'S', 'Se']



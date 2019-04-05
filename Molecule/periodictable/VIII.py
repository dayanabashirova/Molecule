# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
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


class GroupVIII:
    pass


class Fe(Element, PeriodIV, GroupVIII):
    @property
    def atomic_number(self):
        return 26

    @property
    def atomic_mass(self):
        return 55.845

    @property
    def electronegativity(self):
        return 1.83

    @property
    def common_isotope(self):
        return 56

    @property
    def max_isotope(self):
        return 60

    @property
    def min_isotope(self):
        return 54

    @property
    def common_valences(self):
        return (0, 5), (2, 5), (3, 4)

    @property
    def valences_exceptions(self):
        return ((-2, 5, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Fe(OH)4]2-
                (-4, 5, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Fe(OH)6]4-
                (-4, 5, ((2, 'O'), (2, 'O'), (2, 'O'))),  # [FeO3]4-
                (-2, 5, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [FeF4]2-
                (-2, 5, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [FeCl4]2-
                (-4, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Fe(CN)6]4-
                (-4, 5, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Fe(SCN)6]4-
                (-4, 5, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Fe(NCS)6]4-
                (-2, 5, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Fe(SCN)4]2-
                (-4, 5, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Fe(NCS)4]2-
                (-3, 4, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Fe(SCN)6]3-
                (-3, 4, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Fe(NCS)6]3-
                (-3, 4, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Fe(CN)6]3-
                (-1, 4, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [FeCl4]-
                (-2, 4, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [FeCl5]2-
                (-3, 4, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [FeCl6]3-
                (-3, 4, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [FeF6]3-
                (-1, 4, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),  # [FeBr4]-


__all__ = ['GroupVIII']


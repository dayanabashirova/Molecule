# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
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


class GroupXVIII:
    pass


class He(Element, PeriodI, GroupXVIII):

    @property
    def atomic_number(self):
        return 2

    @property
    def atomic_mass(self):
        return 4.0026

    @property
    def electronegativity(self):
        return 4.5

    @property
    def max_multiplicity(self):
        return 1

    @property
    def min_charge(self):
        return 0

    @property
    def max_charge(self):
        return 1

    @property
    def common_isotope(self):
        return 4

    @property
    def max_isotope(self):
        return 10

    @property
    def min_isotope(self):
        return 2

    @property
    def common_valences(self):
        return ((0, 1))

    @property
    def valences_exeptions(self):
        return ()



class Ne(Element, PeriodI, GroupXVIII):

    @property
    def atomic_number(self):
        return 10

    @property
    def atomic_mass(self):
        return 20.1797

    @property
    def electronegativity(self):
        return 4.4

    @property
    def max_multiplicity(self):
        return 1

    @property
    def min_charge(self):
        return 0

    @property
    def max_charge(self):
        return 1

    @property
    def common_isotope(self):
        return 20

    @property
    def max_isotope(self):
        return 34

    @property
    def min_isotope(self):
        return 16

    @property
    def common_valences(self):
        return ((0, 1))

    @property
    def valences_exeptions(self):
        return ()



class Ar(Element, PeriodI, GroupXVIII):

    @property
    def atomic_number(self):
        return 18

    @property
    def atomic_mass(self):
        return 39.948

    @property
    def electronegativity(self):
        return 4.3

    @property
    def max_multiplicity(self):
        return 1

    @property
    def min_charge(self):
        return 0

    @property
    def max_charge(self):
        return 1

    @property
    def common_isotope(self):
        return 40

    @property
    def max_isotope(self):
        return 53

    @property
    def min_isotope(self):
        return 30

    @property
    def common_valences(self):
        return ((0, 1))

    @property
    def valences_exeptions(self):
        return ()



class Kr(Element, PeriodI, GroupXVIII):

    @property
    def atomic_number(self):
        return 36

    @property
    def atomic_mass(self):
        return 83.798

    @property
    def electronegativity(self):
        return 3.0

    @property
    def max_multiplicity(self):
        return 1

    @property
    def min_charge(self):
        return 0

    @property
    def max_charge(self):
        return 1

    @property
    def common_isotope(self):
        return 84

    @property
    def max_isotope(self):
        return 101

    @property
    def min_isotope(self):
        return 69

    @property
    def common_valences(self):
        return ((0, 1))

    @property
    def valences_exeptions(self):
        return ()


__all__ = ['GroupXVIII', 'He']

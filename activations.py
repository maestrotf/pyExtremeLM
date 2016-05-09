# -*- coding: utf-8 -*-
"""
Created on 06.05.16
Created for pyExtremeLM

@author: Tobias Sebastian Finn, tobias.sebastian.finn@studium.uni-hamburg.de

    Copyright (C) {2016}  {Tobias Sebastian Finn}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# System modules

# External modules
import numpy as np
import scipy.special

# Internal modules


__version__ = "0.1"


def sigmoid(X):
    """
    The sigmoid function as array function
    Args:
        X (np.array): The input array.

    Returns:
        val (np.array): The activated array.
    """
    val = scipy.special.expit(X)
    return val


def tanh(X):
    """
    The tanh function
    Args:
        X (np.array): The input array.

    Returns:
        val (np.array): The activated array.
    """
    val = np.tanh(X)
    return val

_activations = {"sigmoid": sigmoid, "tanh": tanh}

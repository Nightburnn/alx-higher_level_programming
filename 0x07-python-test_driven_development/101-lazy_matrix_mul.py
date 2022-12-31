#!/usr/bin/python3
""" use numpy to multiply two matrices the lazy way"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
        """ Function that takes in 2 matrices and multiplies them

        Args:
            m_a: first matrix
            m_b: second matrix

        Return: the product of m_a and m_b
        """
        return np.matmul(m_a, m_b)

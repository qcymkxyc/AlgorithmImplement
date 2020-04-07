#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/18 16:02
@Author  : Zhang Qi
@Email   : zhangqi@onlinesign.com.cn
@File    : 协方差测试.py
@Description    :  
"""
import unittest
import numpy as np


def my_cov(x):
    n_row,n_col = x.shape
    y = x
    # y = x.transpose()
    t = np.zeros((n_row,n_row))
    for i,row_data1 in enumerate(y):
        for j,row_data2 in enumerate(y):
            # print(row_data1,row_data2)
            vec1 = (row_data1 - row_data1.mean())
            vec2 = (row_data2 - row_data2.mean())
            t[i][j] = vec1.dot(vec2) / (len(vec1) - 1)
    return t


class CovTestCase(unittest.TestCase):
    def test_my_cov(self):
        x = np.arange(12).reshape(3,4)
        print(my_cov(x))
        print(np.cov(x))
        self.assertTrue((my_cov(x) == np.cov(x)).all())


if __name__ == '__main__':
    unittest.main()

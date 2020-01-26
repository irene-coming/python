# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 PM4:13
# @Author  : jianhan513@163.com
import math

def binary_search(arr, target):
    low=0
    high=len(arr)-1

    while low <= high:
        mid_idx = math.floor((low+high)/2)
        mid = arr[mid_idx]
        if (target == mid):
            return mid_idx
        elif (target > mid):
            low = mid_idx+1
        elif (target < mid):
            high = mid_idx -1

    return None
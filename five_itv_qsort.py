from opes import *

import math
import statistics

global a,n,mid_a,intervals,next_intervals

def five_itv_qsort(lst):
    global a,n,mid_a,intervals,next_intervals

    a = lst
    n = len(a)
    mid_a = math.floor((n-1)/2)

    intervals = []
    intervals.append(a)
    next_intervals = []
    
    while len(intervals) != n:
        
        for i in range(0,len(a)):
            if type(is_mid(a[mid_a])) is list:
                split_interval(find_interval(a[mid_a]))
            r_shift_all(a)

        intervals = next_intervals
        next_intervals = []

# is_mid(target) returns a list or False
#    - if the target is the midpoint
#      in some list in intervals, then return the list
#    - Otherwise, is_mid returns False.
def is_mid(target):
    for interval in intervals:
        if len(interval) == 1:
            # In this case, we can omit split process,
            # so, we do only a preparation for updating
            # the interval set
            update_intervals(interval,[interval])
        elif target in interval:
            idx = interval.index(target)
            if idx == math.floor((len(interval) - 1)/2):
                # idx is mid in lst or not
                return interval
    return False  # target is not mid for any interval
            
'''
find_interval(target) returns a pair of index on a[] and a list.
We are given a target element. Let I be the interval including the target. Then find_interval returns the pair of start and end indexes of I in a[] and I.
'''
def find_interval(target):
    for interval in intervals:
        if target in interval:
            return [[a.index(interval[0]), a.index(interval[len(interval)-1])], interval]

def split_interval(interval_info):
    if len(a) % 2 == 1:
        split_odd(interval_info)
    else:
        split_even(interval_info)

#######################################################
def split_even(interval_info):
    #interval_info is a list of two lists: [[start index in a, end index in a], [elements in this interval]]

    start_end_pair = interval_info[0]
    interval = interval_info[1]
    med_interval = statistics.median_low(interval)

    if len(interval) == 2:
        if a[mid_a] > a[mid_a + 1]:
            swap_centers(a)
            update_intervals(interval,
                             [[interval[0]],[interval[1]]])
        else:
            update_intervals(interval,
                             [[interval[0]],[interval[1]]])
    else:
        count_down_smaller = math.ceil(len(interval)/2)
        count_down_larger = math.floor(len(interval)/2)
        # Jump process
        while not((count_down_smaller == 0) and
                  (count_down_larger == 0)):
            if (count_down_smaller > 0) and (a[mid_a] <= med_interval):                
                jump_left_even()
                count_down_smaller -= 1
            if (count_down_larger > 0) and a[mid_a +1] > med_interval:
                jump_right_even()
                count_down_larger -= 1
            if (count_down_smaller > 0) and (count_down_larger > 0) and (a[mid_a] > med_interval) and (a[mid_a +1] <= med_interval):
                swap_centers(a)

        # Reconstruction process: Go back around center
        #count_down_smaller = math.ceil(len(interval))
        #count_down_larger = math.floor(len(interval))
        for i in range(0, math.ceil(len(interval)/2)):
            l_shift_1st(a)
        for i in range(0, math.floor(len(interval)/2)):
            r_shift_last(a)

        update_intervals(interval,
                        [a[get_start_idx(interval_info):mid_a +1], a[mid_a + 1:get_end_idx(interval_info) + 1]])
                
def jump_left_even():
    r_shift_1st(a)

def jump_right_even():
    l_shift_last(a)

#######################################################
def split_odd(interval_info):

    start_end_pair = interval_info[0]
    interval = interval_info[1]
    med_interval = statistics.median_low(interval)

    # Jump to leftmost or rightmost
    for i in range(0,len(interval)-1):
        if a[mid_a] <= med_interval:
            start_end_pair = jump_left_odd(start_end_pair[0], start_end_pair[1], med_interval)
        else:
            start_end_pair = jump_right_odd(start_end_pair[0], start_end_pair[1], med_interval)

    # Go back to around center.
    if a[mid_a] <= med_interval:
        for i in range(0, math.ceil(len(interval)/2)-1):
            l_shift_1st(a)
        for i in range(0, math.floor(len(interval)/2)):
            r_shift_last(a)
            swap_center_r(a)
    else:
        for i in range(0, math.ceil(len(interval)/2)-1):
            r_shift_last(a)
        for i in range(0, math.floor(len(interval)/2)):
            l_shift_1st(a)
            swap_center_l(a)

    # Edit interval set: ``intervals''
    update_intervals(interval, [a[get_start_idx(interval_info):mid_a + 1], a[mid_a + 1:get_end_idx(interval_info) + 1]])

def update_intervals(del_itv, ins_itv_lst):
    intervals.remove(del_itv)
    for itv in ins_itv_lst:
        next_intervals.append(itv)
    
def jump_left_odd(start,end,med_interval):
    if start == mid_a:
        swap_center_r(a)
        if a[mid_a] <= med_interval:
            # This case never happen.
            start_end_pair = jump_left_odd(start, end, med_interval)

        else:
            start_end_pair = jump_right_odd(start, end, med_interval)
        return start_end_pair
    else:
        r_shift_1st(a)
        return [start+1,end]

def jump_right_odd(start, end, med_interval):
    if end == mid_a:
        swap_center_l(a)
        if a[mid_a] <= med_interval:
            start_end_pair = jump_left_odd(start, end, med_interval)
        else:
            start_end_pair = jump_right_odd(start, end, med_interval)
        return start_end_pair
    else:
        l_shift_last(a)
        return [start, end-1]

def get_start_idx(itv_info):
    return itv_info[0][0]

def get_end_idx(itv_info):
    return itv_info[0][1]

def swap_on_lst(lst,i,j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    

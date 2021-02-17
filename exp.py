import opes 
from five_itv_qsort import *

import random
import sys
import math
import statistics
import itertools
import copy

def all_exp(num_elem, sort_func=five_itv_qsort):
    global a,n,num_reversals,mid_a,intervals
    
    n = num_elem
    total_num_reversals = 0
    print('permutation, number of reversals')
    for perm in itertools.permutations(range(1,n+1)):
        a = list(perm)
        n = len(a)
        mid_a = math.floor((n-1)/2)
        intervals = []
        intervals.append(a)
        next_intervals = []
        #print(a)
        opes.num_reversals = 0
        sort_func(a)
        print(f'{list(perm)}, {opes.num_reversals}')
        total_num_reversals = total_num_reversals + opes.num_reversals

    print(f'All permutation of {num_elem} elements\nSorting algo: {sort_func}\nAverage num_reversals: {total_num_reversals / math.factorial(n)}')

def perm_randomize(n, lst):
    for i in reversed(range(0,n)):
        j = random.randint(0,i)
        swap_on_lst(lst, i,j)
    return lst

### Test function:
### num_elem: number of elements in a permutation
### num_trials: How many permutations the function tests
def random_exp(num_elem, num_trials, sort_func=five_itv_qsort):
    global a,n,mid_a,intervals,next_intervals,num_reversals,total_num_reversals

    total_num_reversals = 0

    print('permutation, number of reversals')
    for i in range(0,num_trials):
        #perm_length = random.randint(2,50)
        #a = perm_random.generate_a_perm(perm_length)
        a = list(range(1,num_elem+1))
        a = perm_randomize(num_elem,a)
        temp_a = copy.copy(a)
        n = len(a)
        mid_a = math.floor((n-1)/2)
        intervals = []
        intervals.append(a)
        next_intervals = []
        opes.num_reversals = 0
        sort_func(a)
        print(f'{temp_a}, {opes.num_reversals}')
        total_num_reversals = total_num_reversals + opes.num_reversals
        id_perm = list(range(1,num_elem+1))
        if id_perm == a:
            pass
        else:
            print('is not sorted correctly.')
            break
    print(f'{num_elem} elements,\n{num_trials} trials,\nSorting algo: {sort_func}\nAverage num_reversals: {total_num_reversals / num_trials}')

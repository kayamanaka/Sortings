import opes

from three_itv_qsort import three_itv_qsort
from four_itv_qsort import four_itv_qsort
from five_itv_qsort import five_itv_qsort

import random
import sys
import math
import statistics
import itertools
import copy

def all_exp(num_elem, sort_func):

    total_num_reversals = 0
    max_num_reversals = 0
    min_num_reversals = 1000000000

    for perm in itertools.permutations(range(1,num_elem+1)):
        a = list(perm)
        opes.num_reversals = 0
        sort_func(a)
        print(f'{list(perm)}, {opes.num_reversals}')
        total_num_reversals = total_num_reversals + opes.num_reversals
        max_num_reversals = max(opes.num_reversals,max_num_reversals)
        min_num_reversals = min(opes.num_reversals,min_num_reversals)
        id_perm = list(range(1,num_elem+1))
        if id_perm == a:
            pass
        else:
            print('is not sorted correctly.')
            break

    print(f'All permutation of {num_elem} elements\nSorting algo: {sort_func}\nAve num_reversals: {total_num_reversals / math.factorial(num_elem)}\nMax num_reversals: {max_num_reversals}\nMin num_reversals: {min_num_reversals}')

def swap_on_lst(lst,i,j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    
def perm_randomize(n, lst):
    for i in reversed(range(0,n)):
        j = random.randint(0,i)
        swap_on_lst(lst, i,j)
    return lst

### Test function:
### num_elem: number of elements in a permutation
### num_trials: How many permutations the function tests
def random_exp(num_elem, num_trials, sort_func):
    total_num_reversals = 0
    max_num_reversals = 0
    min_num_reversals = 100000000000

    print('permutation, number of reversals')
    for i in range(0,num_trials):
        a = list(range(1,num_elem+1))
        a = perm_randomize(num_elem,a)
        temp_a = copy.copy(a)
        opes.num_reversals = 0
        sort_func(a)
        print(f'{temp_a}, {opes.num_reversals}')
        total_num_reversals = total_num_reversals + opes.num_reversals
        max_num_reversals = max(opes.num_reversals,max_num_reversals)
        min_num_reversals = min(opes.num_reversals,min_num_reversals)
        id_perm = list(range(1,num_elem+1))
        if id_perm == a:
            pass
        else:
            print('is not sorted correctly.')
            break
    print(f'{num_elem} elements,\n{num_trials} trials,\nSorting algo: {sort_func}\nAve num_reversals: {total_num_reversals / num_trials}\nMax num_reversals: {max_num_reversals}\nMin num_reversals: {min_num_reversals}')

def random_exp_allalgos(num_elem, num_trials):
    total_num_reversals_three = 0
    total_num_reversals_four = 0
    total_num_reversals_five = 0
    max_num_reversals_three = 0
    max_num_reversals_four = 0
    max_num_reversals_five = 0
    min_num_reversals_three = 100000000000
    min_num_reversals_four = 100000000000
    min_num_reversals_five = 100000000000

    #print('permutation, number of reversals')
    for i in range(0,num_trials):
        a = list(range(1,num_elem+1))
        a = perm_randomize(num_elem,a)
        temp_a = copy.copy(a)

        opes.num_reversals = 0
        three_itv_qsort(a)
        #print(f'{temp_a}, {opes.num_reversals}')
        total_num_reversals_three = total_num_reversals_three + opes.num_reversals
        max_num_reversals_three = max(opes.num_reversals,max_num_reversals_three)
        min_num_reversals_three = min(opes.num_reversals,min_num_reversals_three)

        a = copy.copy(temp_a)
        opes.num_reversals = 0
        four_itv_qsort(a)
        #print(f'{temp_a}, {opes.num_reversals}')
        total_num_reversals_four = total_num_reversals_four + opes.num_reversals
        max_num_reversals_four = max(opes.num_reversals,max_num_reversals_four)
        min_num_reversals_four = min(opes.num_reversals,min_num_reversals_four)

        a = copy.copy(temp_a)
        opes.num_reversals = 0
        five_itv_qsort(a)
        print(f'{temp_a}, {opes.num_reversals}')
        total_num_reversals_five = total_num_reversals_five + opes.num_reversals
        max_num_reversals_five = max(opes.num_reversals,max_num_reversals_five)
        min_num_reversals_five = min(opes.num_reversals,min_num_reversals_five)
        
    print(f'{num_elem} elements,\n{num_trials} trials,\n\nSorting algo: three_itv_qsort\nAve num_reversals_three: {total_num_reversals_three / num_trials}\nMax num_reversals: {max_num_reversals_three}\nMin num_reversals: {min_num_reversals_three}')
    print(f'\nSorting algo: four_itv_qsort\nAve num_reversals_four: {total_num_reversals_four / num_trials}\nMax num_reversals: {max_num_reversals_four}\nMin num_reversals: {min_num_reversals_four}')
    print(f'\nSorting algo: five_itv_qsort\nAve num_reversals_five: {total_num_reversals_five / num_trials}\nMax num_reversals: {max_num_reversals_five}\nMin num_reversals: {min_num_reversals_five}')

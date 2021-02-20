from opes import *

import math

global a,b,n,center_idx_ceil,center_idx_floor,num_reversals
intervals = []

def center_idx(lst):
    return math.ceil(len(lst)/2)-1

def is_r_before_p(p,r):
    #print(f'{a.index(r)},{a.index(p)}')
    if a.index(r) < a.index(p):
        if a.index(r) == 0 and a.index(p) == n-1:
            return False
        else: 
            return True
    else:
        if a.index(r) == n-1 and a.index(p) == 0:
            return True
        else:
            return False

# Return the first index i s.t. p <= a[i] <= q
def find_first_elem(min,max):
    for i in range(n):
        if min <= a[i] and a[i] <= max:
            return i

# Return the last index i s.t. p <= a[i] <= q
def find_last_elem(min, max):
    for i in reversed(range(n)):
        if min <= a[i] and a[i] <= max:
            return i

def find_middle_elem(min,max):
    return (min-1) + math.ceil((max - min + 1) / 2)

# Move ``target'' element to the ``position'' in a,
# where target is an element and position is the index
def move_target_to_position(target_elem,position):
    # target: element, position: index on a

    target_elem_idx = a.index(target_elem)
    if target_elem_idx == position:
        return
    elif target_elem_idx < position:
        right_distance = position - target_elem_idx
        for i in range(right_distance):
            R_1_n_1(a)
    else: # target_elem_idx > position
        left_distance = target_elem_idx - position
        for i in range(left_distance):
            L_1_n_1(a)

#
# Main Procedure: ``partition(p,q,r)''
#
def four_itv_partition(p,q,r):
    # p: minimum element in the target block
    # r: maximum element in the target block
    # q: center index of target block = center index of the entire array
    #print(f'In partition  p:{p}, q:{q}, r:{r}')

    # 'n' in the paper by BassS03 is block_size
    block_size = r - p + 1

    if r == p:
        return
    else:
        if r - p == 1:
            # The case of the block size is 2
            if a.index(p) < a.index(r):
                pass
            else:
                # p and r are swapped.
                L_ceilH_n_1(a)
                R_ceilHadd1_n_1(a)
        else: #More_than_two_elems
            # 5) Move the element in position q to position ``center_idx_ceil''
            
            # We maintain the left and right indexes of
            # the target block: left_end & right_end
            if p == 1 and r == n:
                left_end = 1
                right_end = n-1
            else:
                left_end = find_first_elem(p,r)
                right_end = find_last_elem(p,r)

            # The index q (zero-base index) is moved 
            # such that the elem in position q is moved
            # to the position center_idx_ceil
            # (also zero-base index) by shilfs
            if q <= center_idx_ceil:
                for i in range(center_idx_ceil - q):
                    R_1_n_1(a)
            else:
                for i in range(q - center_idx_ceil):
                    L_1_n_1(a)
            #print('a: {}'.format(a))

            # Middle element in target block
            middle_elem = find_middle_elem(p,r)
            #print(f'mid_elem: {middle_elem}')
            # smaller elements in target block
            smallers = list(range(p,middle_elem+1))
            num_smallers = len(smallers)
            #print('smallers:{}'.format(smallers))
            # Larger elements in target block
            largers = list(range(middle_elem+1,r+1))
            #print('largers:{}'.format(largers))
            num_largers = len(largers)
            
            while p <= a[center_idx_ceil] and a[center_idx_ceil] <= r:
             
                if a[center_idx_ceil] <= middle_elem:
                    if len(smallers) == 0:
                        break
                    else:
                        smallers.remove(a[center_idx_ceil])
                        R_1_ceilH_1(a)
                else:
                    if len(largers) == 0:
                        break
                    else:

                        largers.remove(a[center_idx_ceil])
                        L_ceilH_n_1(a)

            # Confirm all elements on the left or right end
            while len(smallers) != 0:
                if len(smaller) >= 2:
                    smallers.remove(a[center_idx_ceil-1])
                    smallers.remove(a[center_idx_ceil-2])
                    # The following operation ..._2 is replaced with two ..._1 operations. The replacement reduces number of reversals
                    #R_1_floorH_2(a)  # 8) for 3 itv ver.
                    #
                    R_1_floorH_1(a) # for 4 itv ver.
                    R_1_floorH_1(a) # for 4 itv ver.
                else:
                    break  # last one continue to stay middle

            while len(largers) != 0:
                if len(largers) >= 2:
                    largers.remove(a[center_idx_ceil+1])
                    largers.remove(a[center_idx_ceil+2])
                    #
                    #L_ceilHadd1_n_2(a)  # 9) for 3 itv
                    #
                    L_ceilHadd1_n_1(a)  # 9) for 4 itv
                    L_ceilHadd1_n_1(a)  # 9) for 4 itv
                else:
                    #largers.remove(a[center_idx_ceil+1])
                    # #L_ceilHadd1_n_1_swap() # This operation makes the program wrong...
                    #L_ceilHadd1_n_1(a)
                    break

            # Process for getting back
            for i in range(num_smallers - len(smallers)):
                L_1_ceilH_1(a)  # 10)

            for i in range(num_largers - len(largers)):
                #R_ceilH_n_1(a)  # 11)
                #R_floorH_ceilHadd1_1(a)  # 12)
                R_ceilHadd1_n_1(a)


def find_block(min_elem, max_elem):
    if min_elem == 1 and max_elem == n:
        first_block_idx = 0
        last_block_idx = n-1
        center_block_idx = center_idx_ceil
    else:
        if (min_elem <= a[0] and a[0] <= max_elem) and (min_elem <= a[n-1] and a[n-1] <= max_elem):
            # Cyclic block case
            for i in range(n):
                if a[i] < min_elem or max_elem < a[i]:
                    last_block_idx = i-1
                    break
            for i in reversed(range(n)):
                if a[i] < min_elem or max_elem < a[i]:
                    first_block_idx = i+1
                    break
            center_block_idx = math.ceil((((n-1) - first_block_idx +1) + (last_block_idx +1))/2) - 1 + first_block_idx
            if center_block_idx > n-1:
                center_block_idx = center_block_idx - n
        else: # Non-cyclic block case
            for i in range(n):
                if a[i] >= min_elem and a[i] <= max_elem:
                    first_block_idx = i
                    break
            for i in reversed(range(n)):
                if a[i] >= min_elem and a[i] <= max_elem:
                    last_block_idx = i
                    break
            center_block_idx = math.ceil((last_block_idx - first_block_idx + 1)/2) + first_block_idx -1
            
    return [first_block_idx,center_block_idx,last_block_idx]
        
def find_interval(elem):
    for interval in intervals:
        if elem in interval:
            return interval
    return []

def get_center_elem(lst):
    return lst[center_idx(lst)]

def print_intervals():
    for i in range(n):
        curr_itv = find_interval(a[i])
        if len(curr_itv) == 2 and curr_itv[0] == a[i]:
            print(f'{curr_itv},',end='')
        elif len(curr_itv) == 1:
            print(f'{curr_itv},',end='')
    print('')    

def is_only_size_one_intervals(itvs):
    if itvs == []:
        return False
    else:
        for itv in itvs:
            if len(itv) > 1:
                return False
    return True
    
def four_itv_qsort(lst):
    global a,n,intervals,center_idx_ceil, center_idx_floor
    a = lst
    n = len(a)
    intervals = []  # Initialization
    intervals.append(a)
    center_idx_ceil = math.ceil((n/2) -1)
    center_idx_floor = math.floor((n/2) -1)

    round = 0
    while round <= math.ceil(math.log2(n))-2:
        round = round +1
        for i in range(n):
            center_interval = find_interval(a[center_idx_ceil])
            if get_center_elem(center_interval) == get_center_elem(a) and len(center_interval) > 1:
                # Call partition procedure
                four_itv_partition(min(center_interval),center_idx_ceil,max(center_interval))
                intervals.remove(center_interval)
                first_half_interval = a[center_idx_ceil - math.ceil(len(center_interval)/2)+1:center_idx_ceil+1]
                intervals.append(first_half_interval)

                second_half_interval = a[center_idx_ceil+1:(center_idx_ceil + 1) + math.floor(len(center_interval)/2)]
                #print(f'a[W:Z]: {second_half_interval}')
                intervals.append(second_half_interval)
                for j in range(len(first_half_interval)-1):
                    R_1_n_1(a)
                    i += 1

            R_1_n_1(a)

    move_target_to_position(n,n-1)

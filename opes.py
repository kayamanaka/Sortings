#
# Operations
#

import math
global num_reversals
num_reversals = 0  # For counting the number of flips

# Reversal operation [0,i]. Note ZERO-BASED index.
def rev(a,i): # Designate an (zero-base) index number in a
    if i > 0:
        for j in range(0,math.ceil(i/2)):
            swap(a,j,i-j)

# Swap a[i] with a[j]
def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

# Five primitive operations
def rev_2(a):
    global num_reversals
    num_reversals = num_reversals+1
    rev(a,1)
def rev_floor(a):
    global num_reversals
    num_reversals = num_reversals+1
    rev(a,math.ceil(len(a)/2)-2)
def rev_ceil(a):
    global num_reversals
    num_reversals = num_reversals+1
    rev(a,math.ceil(len(a)/2)-1)
def rev_allm1(a):
    global num_reversals
    num_reversals = num_reversals+1
    rev(a,len(a)-2)
def rev_all(a):
    global num_reversals
    num_reversals = num_reversals+1
    rev(a,len(a)-1)
def rev_s(a):
    global num_reversals
    #rev(center_idx_floor-1)
    rev(a,math.ceil(len(a)/2)-3)
    #print(num_reversals)
    num_reversals = num_reversals+1
    
# Shift operations
def r_shift_1st(a):
    rev_floor(a)
    rev_ceil(a)
def l_shift_1st(a):
    rev_ceil(a)
    rev_floor(a)
def r_shift_last(a):
    rev_all(a)
    rev_ceil(a)
    rev_floor(a)
    rev_all(a)
def l_shift_last(a):
    rev_all(a)
    rev_floor(a)
    rev_ceil(a)
    rev_all(a)
def r_shift_all(a):
    rev_allm1(a)
    rev_all(a)
def l_shift_all(a):
    rev_all(a)
    rev_allm1(a)

#
# Operations for odd cases
#
# swap_center_l works only in odd case.
def swap_center_l(a):
    rev_ceil(a)
    rev_2(a)
    rev_ceil(a)

# swap_center_r works only in odd case.
def swap_center_r(a):
    rev_all(a)
    rev_ceil(a)
    rev_2(a)
    rev_ceil(a)
    rev_all(a)

#
# Operation for even cases
#
def swap_centers(a):
    l_shift_all(a)
    rev_ceil(a)
    rev_2(a)
    rev_ceil(a)
    r_shift_all(a)


#
# Primitive operations for three itv and four itv qsorts
#
# R(1,n,1): Right shift a[1,n] with 1 shift.
# R(1,n,1) is implemented by (F,A,C)^2.
def R_1_n_1(a):
    rev_floor(a)
    rev_all(a)
    rev_ceil(a)
    rev_floor(a)
    rev_all(a)
    rev_ceil(a)

def R_1_n_2(a):
    R_1_n_1(a)
    R_1_n_1(a)

# L(1,n,1): Left shift a[1,n] with 1 shift.
# L(1,n,1) is implemented by (C,A,F)^2.
def L_1_n_1(a):
    rev_ceil(a)
    rev_all(a)
    rev_floor(a)
    rev_ceil(a)
    rev_all(a)
    rev_floor(a)

def L_1_n_1_conf(a):
    temp = copy.copy(b)
    for i in range(0,n-1):
        b[i] = temp[i+1]
    b[n-1] = temp[0]
    
# Operation (1)
def R_1_ceilH_1(a):
    rev_floor(a)
    rev_ceil(a)

def R_1_ceilH_1_conf(a):
    temp = copy.copy(b)
    b[0] = temp[center_idx_ceil]
    for i in range(1,center_idx_ceil+1):
        b[i] = temp[i-1]
        
# Operation (1)'
def L_1_ceilH_1(a):
    rev_ceil(a)
    rev_floor(a)
    
# Operation (2)
def L_ceilH_n_1(a):
    rev_all(a)
    R_1_ceilH_1(a)
    rev_all(a)

def L_ceilH_n_1_conf(a):
    temp = copy.copy(b)
    b[n-1] = temp[center_idx_ceil]
    for i in range(center_idx_ceil,n-1):
        b[i] = temp[i+1]

# Additional Operation for (3)
def R_ceilH_n_1(a):
    rev_all(a)
    L_1_ceilH_1(a)
    rev_all(a)

# Operation (3)
def L_floorH_ceilHadd1_1(a):
    L_ceilH_n_1(a)
    R_1_ceilH_1(a)
    R_ceilH_n_1(a)
    L_1_ceilH_1(a)

def L_floorH_ceilHadd1_1_conf(a):
    temp = copy.copy(b)
    b[center_idx_ceil-1] = temp[center_idx_ceil]
    b[center_idx_ceil] = temp[center_idx_ceil+1]
    b[center_idx_ceil+1] = temp[center_idx_ceil-1]

# Operation (3)'
# 1234567 --> 1253467
def R_floorH_ceilHadd1_1(a):
    rev_all(a)
    L_floorH_ceilHadd1_1(a)
    rev_all(a)

# Operation (4):
def L_ceilHadd1_n_2(a):
    L_floorH_ceilHadd1_1(a)
    L_ceilH_n_1(a)
    L_floorH_ceilHadd1_1(a)
    L_ceilH_n_1(a)
def L_ceilHadd1_n_2_acfs(a):
    pass

# Operation (4)'
def R_ceilHadd1_n_2(a):
    R_ceilH_n_1(a)
    R_floorH_ceilHadd1_1(a)
    R_ceilH_n_1(a)
    R_floorH_ceilHadd1_1(a)

# Operation (5)
def R_1_floorH_2(a):
    rev_all(a)
    L_ceilHadd1_n_2(a)
    rev_all(a)

# Two operation for (6)
def L_1_n_2(a):
    L_1_n_1(a)
    L_1_n_1(a)
    
def R_ceilH_n_2(a):
    R_ceilH_n_1(a)
    R_ceilH_n_1(a)    
    
# Operation (6)
def swap_2pairs(a):
    R_1_ceilH_1(a)
    L_ceilH_n_1(a)
    R_1_ceilH_1(a)
    L_ceilH_n_1(a)
    R_ceilH_n_2(a)
    L_1_n_2(a)
    R_ceilH_n_2(a)

# n=8 doesn't work
# n=13, doesn't work
def E_floorH_ceilH(a):
    rev_ceil(a)
    L_1_n_2(a)
    for i in range(math.floor(len(a)/2)):
        rev_floor(a)
        L_1_n_1(a)
    #if n == 13:
    #    rev_floor(a)

def R_1_floorH_1(a):
    R_floorH_ceilHadd1_1(a)
    R_1_ceilH_1(a)
    R_floorH_ceilHadd1_1(a)
    E_floorH_ceilH(a)
        
#####
##### Start: The operations for Three itv methods #####
#####
#def L_1_floorHsub1_1(a):
def L_1_floorH_1(a):
    rev_floor(a)
    rev_s(a)

#def R_1_floorHsub1_1(a):
def R_1_floorH_1(a):
    rev_s(a)
    rev_floor(a)

def L_ceilHadd1_n_1(a):
    rev_all(a)
    #R_1_floorHsub1_1(a)
    R_1_floorH_1(a)
    rev_all(a)

def R_ceilHadd1_n_1(a):
    rev_all(a)
    #L_1_floorHsub1_1(a)
    L_1_floorH_1(a)
    rev_all(a)
##### End: The operations for Three itv methods #####

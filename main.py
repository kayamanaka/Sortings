import opes
from three_itv_qsort import *
from four_itv_qsort import *
from five_itv_qsort import *
import exp

#
# Write your program here. After that, perform main.py
# using python3 command.
# This program runs on Python 3.8.6
#

#
# three_itv_qsort:
#

#
# ``exp.random_exp(23,5,three_itv_qsort)'' returns
# the average number of flips when we run
# three-interval quicksort
# for 5 random permutations of n=23 elements.
#
exp.random_exp(23,5,three_itv_qsort)
#

#
# ``exp.all_exp(7,three_itv_qsort)'' returns
# the average number of flips when we run
# three-interval quicksort
# for all the permutations of n=7 elements.
#
# exp.all_exp(7,three_itv_qsort)
#

#
# four_itv_qsort
#

#
# ``exp.random_exp(23,5,four_itv_qsort)'' returns
# the average number of flips when we run
# four-interval quicksort
# for 5 random permutations of n=23 elements.
#
#exp.random_exp(23,5,four_itv_qsort)
#

#
# ``exp.all_exp(7,four_itv_qsort)'' returns
# the average number of flips when we run
# four-interval quicksort
# for all the permutations of n=7 elements.
#
#exp.all_exp(7,four_itv_qsort)
#

#
# five_itv_qsort
#

#
# ``exp.random_exp(23,5,five_itv_qsort)'' returns
# the average number of flips when we run
# five-interval quicksort
# for 5 random permutations of n=23 elements.
#
#exp.random_exp(23,500,five_itv_qsort)
#

#
# ``exp.all_exp(7,five_itv_qsort)'' returns
# the average number of flips when we run
# five-interval quicksort
# for all the permutations of n=7 elements.
#
#exp.all_exp(7,five_itv_qsort)
#

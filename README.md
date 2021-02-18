# Sortings

## Usage

main.py is the main program file.
To run the programs, execute main.py using python command.

'''
% python main.py
'''

Then, output is as follows.

'''
permutation, number of reversals
[36, 2, 37, 12, 21, 32, 35, 11, 22, 47, 15, 19, 4, 42, 33, 38, 24, 9, 34, 6, 46, 5, 28, 26, 39, 43, 45, 29, 17, 18, 1, 40, 27, 30, 25, 16, 44, 8, 7, 14, 41, 23, 20, 3, 10, 13, 31], 5608
[28, 23, 47, 42, 13, 19, 17, 5, 40, 39, 37, 34, 33, 41, 43, 32, 22, 38, 36, 4, 15, 44, 24, 46, 26, 3, 14, 25, 45, 12, 16, 29, 21, 9, 7, 31, 35, 18, 10, 6, 30, 11, 27, 8, 1, 2, 20], 5970
[20, 30, 10, 7, 13, 4, 38, 46, 33, 9, 34, 18, 25, 29, 6, 43, 14, 44, 16, 5, 22, 24, 28, 21, 39, 41, 8, 12, 1, 45, 31, 19, 27, 17, 42, 15, 2, 11, 40, 47, 36, 3, 37, 23, 26, 32, 35], 5972
[7, 44, 28, 39, 42, 18, 16, 21, 33, 25, 29, 11, 14, 47, 32, 22, 27, 36, 20, 9, 46, 15, 10, 6, 41, 40, 30, 34, 23, 24, 38, 5, 35, 26, 31, 19, 8, 37, 13, 1, 43, 12, 3, 45, 2, 4, 17], 5986
[27, 34, 3, 42, 36, 46, 15, 41, 1, 5, 35, 44, 37, 18, 39, 23, 7, 8, 21, 40, 22, 9, 6, 45, 32, 19, 29, 4, 43, 24, 11, 47, 25, 12, 30, 28, 16, 17, 2, 10, 33, 20, 38, 26, 31, 13, 14], 6236
47 elements,
5 trials,
Sorting algo: <function three_itv_qsort at 0x1091c79d0>
Average num_reversals: 5954.4
'''

The above output is the result when we execute three-interval quicksort for 5 random permutations of n=47 elements.
The first list [36, 2, ...] is a randomly generated permutation.
The second list [28, 23, ...] is ..., and so on.
The last line represents the average number of flips.



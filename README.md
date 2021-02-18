# Sortings

## Usage

main.py is the main program file.
To run the programs, execute main.py using python command.

```
% python main.py
```

Then, you will get the following output.

```
permutation, number of reversals
[4, 17, 18, 10, 23, 1, 12, 16, 11, 13, 5, 14, 21, 8, 19, 20, 3, 15, 9, 22, 2, 7, 6], 2372
[7, 21, 2, 23, 3, 17, 5, 14, 19, 16, 1, 22, 9, 13, 8, 10, 12, 15, 20, 6, 11, 18, 4], 2310
[8, 9, 17, 16, 10, 13, 4, 6, 3, 11, 12, 22, 23, 14, 20, 19, 21, 2, 18, 1, 15, 5, 7], 2432
[14, 10, 12, 2, 22, 6, 15, 1, 13, 4, 18, 8, 16, 7, 9, 21, 3, 17, 20, 5, 23, 19, 11], 2254
[11, 20, 1, 3, 13, 6, 22, 8, 18, 9, 19, 16, 7, 15, 5, 14, 21, 2, 12, 4, 17, 23, 10], 2184
23 elements,
5 trials,
Sorting algo: <function three_itv_qsort at 0x109656af0>
Average num_reversals: 2310.4
```

The above output is the result when we execute three-interval quicksort for 5 random permutations of n=47 elements.
The first line explains the format
The second line contains the permutation `[4, 17, ...]`, which is generated first and the number of flips to sort the permutation.
The third line is same, and so on.
The last line represents the average number of flips for sorting 5 permutations.

In this repository, we prepared two methods for measuring average number of flips:
(1) for randomly generated permutations and (2) for all the permutations.

If you run the program in a different way, you have to edit main.py.
The details for editting are shown below.

# Sorting permutations generated uniformly at random

You can use the method `exp.random_exp(n,k,alg)` which returns the average number of flips for `k` generated permutations of `n` elements by the sorting algorithm designated in the last argument `alg`
You can choose one sorting algorithm from the following three algorithms:

- `three_itv_qsort`: Quicksort using 3 intervals
- `four_itv_qsort`: Quicksort using 4 intervals
- `five_itv_qsort`: Quicksort using 5 intervals

If you insert a call of the method, for example, `exp.random_exp(5,100,five_itv_qsort)`, in main.py, and execute `main.py`,
then you will see the average number of flips.

# Sorting all the permutations of n elements

You can use the method `exp.all_exp(n,alg)` which returns the average number of flips for all the permutations of `n` elements by the sorting algorithm designated in the last argument `alg`
You can choose one sorting algorithm from the three algorithms shown in above.

If you insert a call of the method, for example, `exp.all_exp(5,100,five_itv_qsort)`, in main.py, and execute `main.py`,
then you will see the average number of flips.



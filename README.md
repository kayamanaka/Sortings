# Sortings

## Usage
### Run sample program

main.py is the main program file.
To run the programs, execute main.py using python command.

```
% python main.py
```

Then, you will get the following output.

```
permutation, number of reversals
[3, 8, 22, 2, 4, 10, 1, 15, 17, 9, 18, 12, 20, 5, 11, 14, 23, 7, 19, 13, 21, 6, 16], 2322
[16, 17, 1, 22, 7, 9, 13, 10, 15, 12, 18, 5, 6, 2, 11, 20, 14, 23, 19, 4, 8, 21, 3], 2092
[1, 13, 15, 9, 16, 3, 5, 4, 22, 6, 7, 12, 14, 23, 18, 21, 2, 11, 17, 10, 19, 8, 20], 2040
[19, 6, 8, 9, 13, 14, 23, 2, 20, 7, 10, 21, 3, 22, 18, 4, 12, 11, 16, 5, 15, 17, 1], 1818
[15, 21, 5, 1, 10, 18, 23, 12, 17, 19, 13, 8, 22, 2, 7, 16, 9, 4, 14, 20, 3, 6, 11], 2524
23 elements,
5 trials,
Sorting algo: <function three_itv_qsort at 0x10d9bd8b0>
Ave num_reversals: 2159.2
Max num_reversals: 2524
Min num_reversals: 1818

```

The above output is the result when we execute three-interval quicksort for 5 random permutations of n=23 elements.
The first line explains the format
The second line contains the permutation `[3, 8, ...]`, which is generated first and the number of flips to sort the permutation.
The third line is same, and so on.
The last three line represent the average, maximum, and minimum numbers of flips for sorting 5 permutations.

In this repository, we prepared two methods for measuring average, maximum, and minimum numbers of flips:
(1) for randomly generated permutations and (2) for all the permutations.

If you run the program in a different way, you have to edit main.py.
The details for editting are shown below.

### Sorting permutations generated uniformly at random

You can use the method `exp.random_exp(n,k,alg)` which returns the average, maximum, and minimum numbers of flips for `k` generated permutations of `n` elements by the sorting algorithm designated in the last argument `alg`
You can choose one sorting algorithm from the following three algorithms:

- `three_itv_qsort`: Quicksort using 3 intervals. This program is an implementation of the algorithm in [BS03]. Their algorithm works when n is odd, n mod 4 \neq 1, and (n >= 13 and n mod 8 \neq 5).
- `four_itv_qsort`: Quicksort using 4 intervals. This program works when n is odd.
- `five_itv_qsort`: Quicksort using 5 intervals. This program works for any positive integer n.

If you insert a call of the method, for example, `exp.random_exp(5,100,five_itv_qsort)`, in main.py, and execute `python main.py` on your terminal,
then you will see the average, maximum, and minimum numbers of flips with all the generated permutations.
More precisely, first each generated permutation and its number of flips to sort it is output, and the average, maximum, and minimum numbers of flips with additional information are output.

### Sorting all the permutations of n elements

You can use the method `exp.all_exp(n,alg)` which returns the average, maximum, and minimum numbers of flips for all the permutations of `n` elements by the sorting algorithm designated in the last argument `alg`
You can choose one sorting algorithm from the three algorithms shown in above.

If you insert a call of the method, for example, `exp.all_exp(5,100,five_itv_qsort)`, in main.py, and execute `main.py`,
then you will see the average, maximum, and minimum numbers of flips.

### Sorting permutations generated uniformly at random by three algorithms

You can use the method `exp.random_exp_allalgos(n,k)' which returns 
the average, maximum, and minimum numbers of flips for the three algorithms (three_itv_qsort, four_itv_qsort, five_itv_qsort)

## References

[BS03] Douglas W. Bass and I.Hal Sudborough, Pancake problems with restricted prefix reversals and some corresponding Cayley networks, Journal of Parallel and Distributed Computing, vol.63, no.3, pp.327-336, March 2003.

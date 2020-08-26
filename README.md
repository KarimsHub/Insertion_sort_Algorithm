# Insertion sort Algorithm

Insertion sort is a sorting algorithm that builds a final sorted array (sometimes called a list) one element at a time.


## Working of this algorithm:
- Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
- It repeats until no input elements remain.


## Complexity:
- Insertion sort has an average and worst-case running time of O(n²), so in most cases, a faster algorithm is more desirable.
- Comparison to Selection sort: Time Complexity of selection sort is always n(n - 1)/2, whereas insertion sort has better time complexity as its worst case complexity is n(n - 1)/2. Generally it will take lesser or equal comparisons then n(n - 1)/2.


## Advantages of Insertion sort:

- Efficient for small data sets, especially in practice than other quadratic algorithms — i.e. O(n²).
- It’s really simple to code
- Very memory efficient (in-place algorithm if the element is taken out of the original list)

## Disadvantages of Insertion sort:

- With n² steps required for every n element to be sorted, the insertion sort does not deal well with a huge list.
- Additionally, its performance is easily influenced by the initial ordering of the items before the sorting process.


![ImgName](https://github.com/KarimsHub/Insertion_sort_Algorithm/blob/master/insertion_sort.png?raw=true)

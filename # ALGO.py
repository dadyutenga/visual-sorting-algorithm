# g(n) = n^2
# f(n) < O(n^2); => We have constant 'k' which makes k*n^2 always bigger than f(n) for any value of n > n0. e.g. 2n^2 + 2n < 3n^2
# simply,  O(n^2) will always go over f(n) after a certain value of n

# Bubble Sort: Hello world of sorting algorithms.
# Loop through array while keeping an eye on current and next element
# Swap the two whenever current one is bigger until you reach the
# keep repeating this process until no swap is done in a loop 

async def bubble_sort(arr, draw_arr):
    n = len(arr)
    _c = 0
    swapped = False
    
    while swapped == True or swapped is False:
        swapped = False
        for j in range(n - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
                await draw_arr(arr, 3, j + 1, j)
            await draw_arr(arr, 2)
            _c += 1
        await draw_arr(arr, 1)

    print(f"bubblesort {arr} -> {_c}")
    return arr

# Cocktail Sort: bubble sort bouncing back and forth.
# Same as bubble sort, instead of looping from the start every time,
# when it reaches the end, it starts the loop from the end swapping in
# reverse.

async def cocktail_sort(arr, draw_arr):
    n = len(arr)
    _c = 0
    swapped = False
    
    while swapped == True or swapped is False:
        swapped = False
        
        for j in range(n - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
                await draw_arr(arr, 3, j + 1, j)
            _c += 1
            await draw_arr(arr, 2)
        
        if not swapped:
            break
        
        for j in range(n - 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
                await draw_arr(arr, 3, j, j - 1)
            _c += 1
            await draw_arr(arr, 2)
        
        await draw_arr(arr, 1)

    print(f"cocktail sort {_c}")
    return arr

# Insertion Sort: Pick an item, and loop back to first item while swapping
# where required, like bubble sort backwards each iteration. 
# Pick next element and repeat til end of array.

async def insertion_sort(arr, draw_arr):
    n = len(arr)
    _c = 0
    
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                await draw_arr(arr, 3, j - 1, j)
            _c += 1
            await draw_arr(arr, 2)
        await draw_arr(arr, 1)

# Gnome Sort (Stupid Sort): An upgrade to insertion sort
# Unlike insertion sort, which even after correctly positioning the selected 
# item still runs upto first item, Gnome Sort skips those comparisons and
# picks the next item to sort.

async def gnome_sort(arr, draw_arr):
    n = len(arr)
    _c = 0
    
    pos = 0
    while pos < n:
        if pos == 0 or arr[pos - 1] < arr[pos]:
            pos += 1
        else:
            arr[pos - 1], arr[pos] = arr[pos], arr[pos - 1]
            await draw_arr(arr, 3, pos, pos - 1)
            pos -= 1
        await draw_arr(arr, 1)
        await draw_arr(arr, 2)
        _c += 1
        
    print(f"gnome sort {_c}")
    return arr

# Comb Sort: A Bubble Sort with varying swap items distance
# Bubble sort always swap adjacent items, while Comb Sort starts swapping very
# distant items and gradually narrows the distance on each iteration. This
# also increases the comparisons on each iteration.

async def combSort(arr, draw_arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    _c = 0
    _s = 0

    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                swap(arr, i, i + gap)
                sorted = False

                _s += 1
                await draw_arr(arr, 3, i, i + gap)
            await draw_arr(arr, 2, i, i + gap)
            _c += 1
        await draw_arr(arr, 1)

    print(f"comb sort {_c}")
    return arr

# Shell Sort: Applies gapping method (as in comb sort) on insertion sort
 
 async function shellSort(arr, draw_wait) {
    const n = arr.length;
    const gaps = [7501, 701, 301, 132, 57, 23, 10, 4, 1]; // most optimized gap sequence
    let _c = 0, _c2 = 0;

    for (let g = 0; g < gaps.length; g++) {
        const gap = gaps[g];

        for (let i = gap; i < n; i++) { // select a gap value within list, and loop upto last element in list
            const temp = arr[i]; // pick element on that position

            let j = i
            
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                await draw_wait(arr, 3, j);

                j -= gap;
                _c++;
            }
            arr[j] = temp;
            await draw_wait(arr, 3, j);
            
            _c2++;
            await draw_wait(arr, 2);
        }
        await draw_wait(arr, 1);
    }
    console.log(`shellsort ${_c + _c2}`);
    return arr;
}

# Selection Sort: A simple algorithm like bubble sort
# start from first item and iterate through remaining list to find a 
# smaller item when found, swap with it and move to next position and 
# repeat the process

async def selectionSort(arr, draw_arr):
    n = len(arr)
    _c = 0

    imin = 0
    for j in range(n - 1):
        imin = j
        for i in range(j + 1, n): # loop to find minimum
            if arr[imin] > arr[i]:
                imin = i
                await draw_arr(arr, 3, imin)
            _c += 1

        if imin != j: # swap with newly found minimum
            arr[j], arr[imin] = arr[imin], arr[j]
            await draw_arr(arr, 3, j, imin)
        await draw_arr(arr, 2)
        await draw_arr(arr, 1)


# Merge Sort: Basic divide and conquer. Split an array recursively until it can not be further divided.
# Sorting happens on merge. Splitted arrays are merge in a way so that final array is sorted. This 
# goes on until all pieces are merged making on sorted array.

async def mergeSort(arr, draw_arr):
    n = len(arr)
    _c = 0

    async def split(arr, i1, i2):
        if i2 == i1:
            return

        m = (i1 + i2) // 2
        await split(arr, i1, m)
        await split(arr, m + 1, i2)

        await merge(arr, i1, m, m + 1, i2)

        await draw_arr(arr, 1)

    async def merge(arr, i1, i2, j1, j2):
        a1 = arr[i1:i2 + 1]
        a2 = arr[j1:j2 + 1]

        i, j, k = 0, 0, i1

        while k <= j2:
            if i >= len(a1):
                arr[k] = a2[j]
                j += 1
            elif j >= len(a2):
                arr[k] = a1[i]
                i += 1
            elif a1[i] < a2[j]:
                arr[k] = a1[i]
                i += 1
            else:
                arr[k] = a2[j]
                j += 1
            await draw_arr(arr, 3, k)
            k += 1
        await draw_arr(arr, 2)

    await split(arr, 0, len(arr) - 1)

# Merge Sort Parallel: Same as original, both branches of split work on different data, they are only made
# to run in parallel instead of one after another.
         
import asyncio

async def parallel_merge_sort(arr, draw_arr):
    n = len(arr)
    _c = 0

    async def split(_arr, i1, i2):
        if i2 == i1:
            return

        m = (i1 + i2) // 2
        s1 = split(_arr, i1, m)
        s2 = split(_arr, m + 1, i2)

        await asyncio.gather(s1, s2)

        await merge(_arr, i1, m, m + 1, i2)

        await draw_arr(_arr, 1)

    async def merge(_arr, i1, i2, j1, j2):
        a1 = _arr[i1:i2 + 1]
        a2 = _arr[j1:j2 + 1]

        i = j = 0
        k = i1

        while k <= j2:
            if i >= len(a1):
                _arr[k] = a2[j]
                j += 1
            elif j >= len(a2):
                _arr[k] = a1[i]
                i += 1
            elif a1[i] < a2[j]:
                _arr[k] = a1[i]
                i += 1
            else:
                _arr[k] = a2[j]
                j += 1
            await draw_arr(_arr, 3, k)
            k += 1
        await draw_arr(_arr, 2)

    await split(arr, 0, n - 1)

# Radix Sort: Sort without comparisons, the weird one
# put items in buckets based on their last digits, then empty the buckets
# back on the list. do it again for second last digit. after going 
# through all digits list will be sorted

async def radixSort(arr, draw_arr):
    n = len(arr)
    _c = 0

    def getDigit(number, index):
        return (abs(number) // 10**index) % 10

    def countDigits(number):
        return int(math.log10(abs(number))) + 1

    maxDigits = 0
    for i in range(n):
        d = countDigits(arr[i])
        maxDigits = d if d > maxDigits else maxDigits

    # init 2d array
    buckets = [[] for i in range(10)]

    for di in range(maxDigits):
        # pick each number, and put it in bucket matching its selected digit
        for j in range(n):
            d = getDigit(arr[j], di)
            buckets[d].append(arr[j])

        # empty all buckets one by one into the original array
        i = 0
        for j in range(10):
            while buckets[j] and len(buckets[j]) > 0:
                arr[i] = buckets[j].pop(0)
                await draw_arr(arr, 3, i)
                i += 1
            await draw_arr(arr, 2)
            await draw_arr(arr, 1)


# Quick Sort: Put all smaller and all greater items on left and right of a selected pivot in any order.
# Start by selecting right most as pivot. Compare with first item, if bigger, move
# it to right side of pivot by shifting pivot to left. Continue moving right and shifting
# pivot to left until all bigger items are on its right. Repate on left and right sides of pivot.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = []
        right = []
        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

# Odd-Even Sort: This is for parallel processors, a modification of bubble sort.
# Too loops, one for even indexes, one for odd.

async def odd_even_sort(arr, draw_arr):
    n = len(arr)
    c = 0
    swapped = True

    while swapped:
        swapped = False
        for j in range(0, n-1, 2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                await draw_arr(arr, 3, j+1, j)
            c += 1
            await draw_arr(arr, 2)

        for j in range(1, n-1, 2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                await draw_arr(arr, 3, j+1, j)
            c += 1
            await draw_arr(arr, 2)

        await draw_arr(arr, 1)

    print(f"Odd-even sort: {c} comparisons")
    return arr

# Cycle Sort: Take each item one by one and only write it on its correct position.
# Least number of write operations but O(n^2).

async def cycle_sort(arr, draw_arr):
    n = len(arr)
    _w = 0
    _c = 0

    for cycle_start in range(n - 1):
        item = arr[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
            _c += 1

        if pos == cycle_start:
            continue

        while item == arr[pos]:
            pos += 1
        t = arr[pos]
        arr[pos] = item
        item = t
        # arr[pos], item = item, arr[pos]
        await draw_arr(arr, 3, pos)

        _w += 1

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            tt = arr[pos]
            arr[pos] = item
            item = tt
            _w += 1
            await draw_arr(arr, 3, pos)

        await draw_arr(arr, 2)
        await draw_arr(arr, 1)

    print(f"cyclesort {_w}")
    return {"_c": _c, "_w": _w}

# TODO
async def pigeonhole_sort(arr):
    pass

# TODO
async def intro_sort(arr):
    n = len(arr)

    def sort(arr, max_depth):
        pass

async def heap_sort(arr, draw_arr):
    n = len(arr)

    def i_parent(i):
        return (i - 1) // 2

    def i_left_child(i):
        return 2 * i + 1

    def i_right_child(i):
        return 2 * i + 2

    async def max_heapify(arr, i, max_val):
        parent = None
        while i < max_val:
            parent = i
            left_child = i_left_child(parent)
            right_child = i_right_child(parent)

            if left_child < max_val and arr[left_child] > arr[parent]:
                parent = left_child

            if right_child < max_val and arr[right_child] > arr[parent]:
                parent = right_child

            if parent == i:
                return

            arr[parent], arr[i] = arr[i], arr[parent]
            await draw_arr(arr, 3, parent, i)
            i = parent

    def verify_heap(arr):
        for i in range(len(arr)):
            if arr[i] < arr[i_left_child(i)] or arr[i] < arr[i_right_child(i)]:
                print("heap is incorrect at", i)
                print(arr)
                return

        print("heap is correct")

    async def build_max_heap(arr):
        i = i_parent(len(arr) - 1)
        while i >= 0:
            await max_heapify(arr, i, len(arr))
            i -= 1

    await build_max_heap(arr)

    last = n - 1

    while last > 0:
        arr[0], arr[last] = arr[last], arr[0]
        await draw_arr(arr, 3, 0, last)

        await max_heapify(arr, 0, last)

        await draw_arr(arr, 2)
        await draw_arr(arr, 1)
        last -= 1

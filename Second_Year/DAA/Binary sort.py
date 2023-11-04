import bisect

def binary_search(arr, val, start, end):
	idx = bisect.bisect_left(arr[start:end+1], val)
	return start + idx

def insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
	return arr

print("Sorted array:")
print(insertion_sort([37, 23, 0, 17, 12, 72, 31,
					46, 82, 100, 54]))
N=4
def getInvCount(arr):
	arr1=[]
	for y in arr:
		for x in y:
			arr1.append(x)
	arr=arr1
	inv_count = 0
	for i in range(N * N - 1):
		for j in range(i + 1,N * N):
			# count pairs(arr[i], arr[j]) such that
			# i < j and arr[i] > arr[j]
			if (arr[j] and arr[i] and arr[i] > arr[j]):
				inv_count+=1
		
	
	return inv_count


# find Position of blank from bottom
def findXPosition(puzzle):
	# start from bottom-right corner of matrix
	for i in range(N - 1,-1,-1):
		for j in range(N - 1,-1,-1):
			if (puzzle[i][j] == 0):
				return N - i


# This function returns true if given instance of N*N - 1 puzzle is solvable
def isSolvable(puzzle):
	# Count inversions in given puzzle
	invCount = getInvCount(puzzle)

	# If grid is odd, return true if inversion
	# count is even.
	if (N & 1):
		return ~(invCount & 1)

	else: # grid is even
		pos = findXPosition(puzzle)
		if (pos & 1):
			return ~(invCount & 1)
		else:
			return invCount & 1
	


# Driver program to test above functions
if __name__ == '__main__':

	puzzle =[
		[12, 1, 10, 2,],
		[7, 11, 4, 14,],
		[5, 0, 9, 15,], # Value 0 is used for empty space
		[8, 13, 6, 3,],]

	print("Solvable") if isSolvable(puzzle) else print("Not Solvable")

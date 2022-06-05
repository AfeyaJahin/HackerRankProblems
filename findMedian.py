def findMedian(arr):
    # Write your code here
    arr = sorted(arr)
    #len/2 will give a float so we have to convert it to the lower bound interger
    i = int((len(arr))/2)  
    median = arr[i]
    return median

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

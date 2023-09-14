def fold(arr):
    #find mid point
    isOdd = len(arr) % 2 # is 0 or 1 boolean
    #add RHS to LHS
    for i in range(0, int(len(arr)/2)): 
        arr[i] += arr[len(arr)-1-i]

    #split array
    return arr[:int(len(arr)/2+isOdd)] #add isOdd so if its odd the midpoint is included

def main():
    arr = [81, 44, 29, 14, 75, 51, 68, 58, 64, 8, 6,15, 28, 23, 80, 51, 10, 26, 94, 38, 72, 62, 62, 17, 17, 80, 97, 57, 56, 24, 36, 59, 21, 10, 34, 27, 98, 34, 88, 97, 1, 16, 61, 42, 50, 69, 73, 85, 22, 31, 65, 14, 21, 71, 54, 3, 19, 11, 45, 20, 0, 28, 72, 96, 78, 99, 75, 52, 90, 52, 14, 10, 67, 100, 66, 45, 62, 17, 83, 1, 36, 95, 45, 18, 89, 76, 55, 77, 4, 55, 63, 100, 57, 45, 58, 62, 27, 16, 5, 23, 55, 64, 76, 32, 27, 19, 15, 11, 80, 61, 82, 85, 87, 51, 54, 24, 25, 15, 69, 47, 54, 58, 3, 32, 99, 83, 47, 21, 37, 92, 58, 9, 93, 1, 0, 15, 58, 53, 6, 20, 62, 39, 65, 17, 12, 93, 61, 23, 71, 63, 38, 65, 58, 79, 52, 33, 43, 17, 38, 61, 50, 21, 33, 66, 86, 55, 4, 3, 34, 70, 77, 4, 66, 62, 9, 48, 44, 34, 4, 13, 55, 57, 58, 89, 6, 45, 44, 16, 42, 27, 69, 25, 90, 71, 19, 42, 66, 4, 84, 3, 85, 47, 9, 25, 22, 31, 23, 77, 7, 0, 7, 11, 82, 74, 18, 76, 9, 12, 72, 90, 46, 14, 7, 56, 83, 16, 10, 25, 56, 24, 33, 29, 57, 9, 59, 8, 6, 52, 82, 21, 100, 92, 0, 54, 41, 80, 33, 81, 54, 48, 32, 29, 23, 57, 0, 4, 64, 19, 11, 68, 39, 52, 56, 80, 27, 21, 55, 95, 92, 90, 57, 46, 98, 52, 77, 75, 0, 25, 51, 26, 81, 33, 0, 25, 6, 95, 28, 21, 64, 23, 2, 74, 47, 19, 29, 69, 2, 75, 21, 87, 33, 63, 25, 67, 50, 79, 81, 6, 29, 14, 47, 61, 7, 62, 79, 91, 81, 44, 94, 35, 60, 37, 16, 87, 60, 5, 58, 3, 79, 93, 55, 7, 77, 83, 18, 70, 28, 54, 3, 28, 26, 30, 48, 50, 84, 35, 10, 70, 66, 25, 6, 79, 17, 20, 81, 88, 28, 33, 52, 65, 33, 25, 49, 62, 10, 99, 52, 30, 78, 39, 47, 3, 45, 25, 66, 3, 6, 12, 29, 81, 57, 83, 51, 99, 67, 29, 80, 77, 36, 83, 57, 47, 57, 51, 64, 31, 80, 79, 12, 40, 100, 342, 2, 3, 12, 96]
    for i in range(0,7):
        arr = fold(arr)
    print(arr)

if __name__ == "__main__":
    main()

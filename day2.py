
def main():
    arr =  ['OOXOOXOXOOXOOOOOOXOX',
            'XOOXOOXOOOOXXOOOOOXO',
            'OXXOOXOXOOOOXOOOXXOO',
            'OXXOXXOOOOOOXOXOXOOX',
            'OOOXXOOOOXOXOOOOOXXO',
            'OOOXOOOOXOXXOOOXOOOO',
            'OOOOOOXOOXXXXXXXXOXO',
            'OOOXOOOOOXXOOXOOOOXX',
            'XXXOOOOOOOOOXOOOOXOO',
            'OOXXOOOOOOOOOXOOXXOX']
    perimeter = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'X':
                for k in [-1,1]:
                    try:
                        if i+k == -1:
                            throw(e)#needed because -1 is a valid index position in python
                        if arr[i+k][j] == 'O':
                            perimeter += 1
                    except:
                        perimeter += 1
                    try:
                        if arr[i][j+k] == 'O':
                            perimeter += 1
                    except:
                        perimeter += 1
    print(perimeter)

if __name__ == "__main__":
    main()

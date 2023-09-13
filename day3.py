import sys
sys.set_int_max_str_digits(0)
# setting there to be no limit on string conversion digits
# so larger value primes can be calculated

def main():
    num = 34234 # number to get factiorial of
    stringFactorial = '1'
    for i in range(2,num+1):
        stringFactorial = str(int(stringFactorial)*i)
        #get the string of the next value
        #splice off all stuff after first non-zero value starting from the right
        count = 0
        for c in stringFactorial[::-1]:
            if c != '0':
                break;
            count += 1
        stringFactorial = stringFactorial[len(stringFactorial)-1-count:]
    print(len(stringFactorial)-1)

if __name__ == "__main__":
    main()

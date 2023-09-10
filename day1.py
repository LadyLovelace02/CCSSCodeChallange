def main():
    sum = 0
    for i in range(0, 3452342):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    print(sum)

if __name__ == "__main__":
    main()

def count_down(number):
    if number < 0:
        print("Done!")
        return
    print(number)
    count_down(number - 1)


count_down(5)

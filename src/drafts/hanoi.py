
def hanoi(n, src, des, tmp):
    if n > 0:
        hanoi(n - 1, src, tmp, des)
        print("src =", src, "\tdes =", des, "\n**************************")
        hanoi(n - 1, tmp, des, src)

#test
hanoi(3, "A", "B", "C")

# Program 9: Tower of Hanoi using recursion

def hanoi(n, source, target, helper):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    hanoi(n-1, source, helper, target)
    print("Move disk", n, "from", source, "to", target)
    hanoi(n-1, helper, target, source)

hanoi(3, "A", "C", "B")

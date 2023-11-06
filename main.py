from node import *

def main():
    #Question 1
    head = node("T", None) # T
    head = node("k", head) # K -> T
    head = node("N", head) # N -> K -> T
    head = node("I", head) # I -> N -> K -> T
    head = node("L", head) # L -> I -> N -> K -> T

    #Question 2
    selection = head

    #Question 3
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    #Question 4
    selection.addNodeAfter("E")

    #Question 5
    selection = selection.getLink()

    #Question 6
    selection.addNodeAfter("D")

    #Question 7
    selection = selection.getLink()

    #Question 8
    selection.addNodeAfter("L")

    #Question 9
    selection = selection.getLink()

    #Question 10
    selection.addNodeAfter("I")

    #Question 11
    selection = selection.getLink()

    #Question 12
    selection.addNodeAfter("S")

    #Question 13
    print("How many nodes does head contain? ", node.listlength(head))
    print("How many nodes does selection contain? ", node.listlength(selection))

    #Question 14
    tail = selection

    #Question 15
    tail = tail.getLink()
    tail = tail.getLink()

    #Question 16
    print("How many nodes does tail contain? ", node.listlength(tail))



if __name__ == "__main__":
    main()
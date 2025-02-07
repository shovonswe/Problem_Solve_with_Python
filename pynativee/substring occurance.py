list_x = list(map(str,input("some words: ").split()))

y = input("sub: ")

occurance =list_x.count(y)

print(y, "is appeared", occurance, "times")

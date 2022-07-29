list1 = ["Cucumber - 1 Kg", " Rasberry - 4 Kg"]

for i in list1:
    g = i.strip("Cucumber -")
    g.split(" ")
    print(g[0])
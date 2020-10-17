def sortf(files):
    sortedf = []
    for file in files:
        f = open(file, "r", encoding = "utf8")
        filemas = f.read().split("\n")
        filemas = [file] + [len(filemas)] + filemas
        sortedf.append(filemas)
        f.close()
    sortedf.sort(key = lambda quantity: quantity[1])
    [print(string) for fl in sortedf for string in fl]
sortf(["1.txt", "2.txt", "3.txt"])

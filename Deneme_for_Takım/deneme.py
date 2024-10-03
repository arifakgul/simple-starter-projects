with open("deneme_rasgeler_takım", "r", encoding="utf-8") as file:
    gs = list()
    fb = list()
    bjk = list()
    for a in file:
        a = a[:-1]
        elemanlar = a.split(",")
        if (elemanlar[2] == "Galatasaray"):
            gs.append(a + "\n")
        elif (elemanlar[2] == "Fenerbahçe"):
            fb.append(a + "\n")
        else:
            bjk.append(a + "\n")
with open("gs.txt","w",encoding= "utf-8") as file1:
    for b in gs:
        file1.write(b)
with open("fb.txt","w",encoding= "utf-8") as file2:
    for c in fb:
        file2.write(c)
with open("bjk.txt","w",encoding= "utf-8") as file3:
    for d in bjk:
        file3.write(d)
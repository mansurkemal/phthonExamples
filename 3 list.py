lst = [1,2,3]
print("sayılar")
print(lst)

print("bitti")
renkler = ["beyaz", "siyah", "sarı", "mavi", "yeşil"]
print(type(renkler))
print(renkler)
print(len(renkler))
print(renkler[1])
print(renkler[1:3:2])
print(renkler[1:4])

renkler = ["beyaz", "siyah", "sarı", "mavi", "yeşil"]
print(renkler)
renkler.append("gri")
print(renkler)

renkler = ["beyaz", "siyah", "sarı", "mavi", "yeşil"]
print(renkler)
renkler.insert(0,"mor")
print(renkler)

renkler = ["beyaz", "siyah", "sarı", "mavi", "yeşil"]
print(renkler)
renkler.remove("siyah")
print(renkler)
renkler2 = ["mor", "turuncu"]
renkler.extend(renkler2)
print(renkler)
renkler = ["beyaz", "siyah", "sarı", "mavi", "yeşil"]
print(renkler)
Silinen= renkler.pop()
print(Silinen)
print(renkler)
silinen = renkler.pop()
print(silinen)
renkler = ["beyaz", "siyah", "sarı", "mavi", "yeşil"]
print(renkler)
renkler.reverse()
print(renkler)
renkler.sort()
print(renkler)
renkler.sort(reverse = True)
print(renkler)
liste2 = sorted(renkler)
print(liste2)

print(renkler)

renkler = ["beyaz", "siyah", "sarı", "mavi", "yeşil"]
sayılar = [1,2,5,6,4,56,456,344]
print(min(renkler))
print(min(sayılar))
print(max(renkler))
print(max(sayılar))
print(sum(sayılar))

for renk in renkler:
    print(renk)
print(list(enumerate(renkler)))
print(list(enumerate(renkler,start=2)))
print("Beyaz" in renkler)
print("beyaz" in renkler)
stringrenkler = "".join(renkler)
print(stringrenkler)
stringrenkler = " ".join(renkler)
print(stringrenkler)
stringrenkler = ",".join(renkler)
print(stringrenkler)
print(type(stringrenkler))
renkler2 = stringrenkler.split(",")
print(renkler2)
print(type(renkler2))

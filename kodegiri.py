def lexicograpichally(kata,res):
    counter = len(kata)
    for i in range((counter * 2) - 1):
        if(i > counter - 1):
            res.append(kata[i - counter + 1: counter])
        else:
            res.append(kata[0: counter - (counter - i) + 1])
        
daftar = input("Masukkan daftar data dengan pemisah koma saja: ")
array_daftar = daftar.split(",")
res = []
for el in array_daftar:
    if not el.replace("'","").replace("`","").replace("’","").replace("‘","").isnumeric():
        kata = el.replace("'","").replace("`","").replace("’","").replace("‘","")
        lexicograpichally(kata,res)

print(res)

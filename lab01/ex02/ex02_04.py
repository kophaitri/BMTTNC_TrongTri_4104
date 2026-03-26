ket_qua = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        ket_qua.append(str(i))
print(",".join(ket_qua))

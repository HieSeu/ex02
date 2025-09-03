import random

print("=== GAME TAI XIU ===")

tien = int(input("Nhap so tien ban co: "))
thang = 0
thua = 0

while tien > 0:
    print("\nBan muon cuoc bao nhieu? (toi da", tien, "$ )")
    cuoc = int(input("Nhap tien cuoc: "))
    if cuoc > tien or cuoc <= 0:
        print("Tien cuoc khong hop le.")
        continue

    doan = input("Doan Tai hay Xiu? ")

    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)
    tong = x1 + x2

    if tong > 5:
        ketqua = "tai"
    else:
        ketqua = "xiu"

    print("Xuc xac:", x1, "+", x2, "=", tong, "=>", ketqua.upper())

    if doan == ketqua:
        print("Ban doan dung! +", cuoc, "$")
        tien += cuoc
        thang += 1
    else:
        print("Ban doan sai! -", cuoc, "$")
        tien -= cuoc
        thua += 1

    print("Tien hien tai:", tien, "$")

    if tien <= 0:
        print("Ban het tien roi!")
        break

    tiep = input("Choi tiep? (y/n): ")
    if tiep != "y":
        break

print("\n=== KET QUA CUOI ===")
print("So van thang:", thang)
print("So van thua:", thua)
print("Tien con lai:", tien, "$")
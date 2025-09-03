import random

tien = 100
thang = 0
thua = 0

print("=== GAME DOAN SO ===")
print("Ban co 100$ luc dau, moi van mat 5$.")
print("Neu thang se duoc +20$.")

while tien >= 5:
    print("\nChon muc do: easy(10), medium(6), hard(3)")
    level = input("Nhap easy/medium/hard: ")
    if level == "easy":
        so_luot = 10
    elif level == "medium":
        so_luot = 6
    else:
        so_luot = 3

    # tru 5$ moi van
    tien -= 5
    so_dap_an = random.randint(1, 100)
    print("Toi da sinh ra 1 so tu 1 den 100, hay doan!")

    win = False
    for i in range(so_luot):
        doan = int(input("Nhap so ban doan: "))
        if doan == so_dap_an:
            print("Chinh xac! Ban thang.")
            tien += 20
            thang += 1
            win = True
            break
        elif doan < so_dap_an:
            print("So cua ban nho hon.")
        else:
            print("So cua ban lon hon.")
    if not win:
        print("Ban thua, so dung la:", so_dap_an)
        thua += 1

    print("Tien hien tai:", tien, "$")

    # hoi choi tiep khong
    tiep = input("Ban muon choi tiep? (y/n): ")
    if tiep != "y":
        break

print("\n=== KET QUA CUOI ===")
print("So van thang:", thang)
print("So van thua:", thua)
print("Tien con lai:", tien, "$")
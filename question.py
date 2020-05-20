print("Kilograms\tPounds\t|\tPounds\tKilograms")

k = 1
p = 20

while True:
    if k >= 1 and k < 199:
        print("{:<3}\t\t{:.1f}\t|\t{:<3}\t{:.1f}".format(k, k * 2.2, p, p * 0.45))
        k += 2
        p += 5
    elif k >= 199 and p <= 515:
        print("{:<3}\t\t{:.1f}\t|\t{:<3}\t{:.1f}".format(k, k * 2.2, p, p * 0.45))
        p += 5
    else:
        break


J = 25799
if 9800<J<32000:
    J = float(J - J%200 + (0 if J%200<110 else 200))
    print(J)
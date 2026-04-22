import sys

num = input()

sign = -1 if num and num[0] == "-" else 1
num = num[1:] if num and num[0] in "-+" else num

if not num or num.count(".") > 1:
    print("incorrect input")
    sys.exit(1)

if not all(ch.isdigit() or ch == "." for ch in num):
    print("incorrect input")
    sys.exit(1)

if num.count(".") == 0:
    val = 0
    for ch in num:
        digit = ord(ch) - ord("0")
        val = val * 10 + digit
    num = sign * val

else:
    dot_idx = num.index(".")

    left = num[:dot_idx]
    val_left = 0
    if left:
        for ch in left:
            digit = ord(ch) - ord("0")
            val_left = val_left * 10 + digit

    right = num[dot_idx + 1 :]
    val_right = 0
    divisor = 1
    if right:
        for ch in right:
            digit = ord(ch) - ord("0")
            val_right = val_right * 10 + digit
            divisor *= 10

    num = sign * (val_left + (val_right / divisor if right else 0))

print(f"{num * 2:.3f}")


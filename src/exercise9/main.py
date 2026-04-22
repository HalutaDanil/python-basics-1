n, dot = input().split()
n = int(n)
dot = float(dot)

coeffs = [float(input()) for _ in range(n + 1)]

deriv = coeffs[0] * n

for i in range(1, n):
    deriv = deriv * dot + coeffs[i] * (n - i)

print(f"{deriv:.3f}")


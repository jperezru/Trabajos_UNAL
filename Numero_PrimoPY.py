n = 2
rango = int(input("Inserte el rango de valores a analizar: "))
lp = [0]

def is_prime(n, lp, rango):
    for _ in range(rango):
        for i in range(2, n):
            if (n%i) == 0:
                n += 1
                pass
        if lp[-1] <= rango:
            lp.append(n)
        else:
            break
        n += 1

is_prime(n, lp, rango)

print(f'los números primos de este rango son: {lp[1:-1]}')

def fibonacci():
    secuencia = (1, 1)
    while len(secuencia) < 20:
        secuencia += (secuencia[-1] + secuencia[-2],)
    impares = []
    for n in secuencia:
        if n % 2 != 0:
            impares.append(n)
    return secuencia, tuple(impares)

fib, impares = fibonacci()
print("Fibonacci:", fib)
print("Impares:", impares)

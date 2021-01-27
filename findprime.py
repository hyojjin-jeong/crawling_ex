import time
import random

def calPrimeFactors(n):
    pf = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            pf.append(d)
            n //= d
        d += 1
    if n > 1:
        pf.append(n)
    return pf

def main():
    print("Starting number crunching")
    t0 = time.time()
    for i in range(10000):
        rand = random.randint(20000, 100000000)
        print(calPrimeFactors(rand))
    t1 = time.time()
    totalTime = t1-t0
    print("Execution Time:{}".format(totalTime))

if __name__ == "__main__":
    main()
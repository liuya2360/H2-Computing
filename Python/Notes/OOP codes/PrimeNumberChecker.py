# OOP versions of WS3-S2 Solutions

# Prime Number Checker (modified)

class PrimeNumberChecker():

    def __init__(self):
        self.primes = {}
        fileHandle = open("primes.txt")
        for line in fileHandle:
            self.primes[int(line.strip())] = True
        fileHandle.close()

        fileHandle = open("threshold.txt")
        self.maxValue = int(fileHandle.read().strip())
        fileHandle.close()

    def isPrime(self, n):
        if n <= self.maxValue:
            if n in self.primes.keys():
                currentIsPrime = True
            else:
                currentIsPrime = False
        else:
            # compute new primes
            newPrimes = []
            for i in range(self.maxValue + 1, n + 1):
                currentHasFactor = False
                for factor in range(2, int(i ** 0.5) + 1):
                    if i % factor == 0:
                        currentHasFactor = True
                        break
                if not currentHasFactor:
                    newPrimes.append(i)
                    self.primes[i] = True

            self.maxValue = n

            if newPrimes[-1] == n:
                currentIsPrime = True
            else:
                currentIsPrime = False

            fileHandle = open("primes.txt", "a")
            for i in range(len(newPrimes)):
                fileHandle.write(str(newPrimes[i]) + "\n")
            fileHandle.close()

            fileHandle = open("threshold.txt", "w")
            fileHandle.write(str(self.maxValue) + "\n")
            fileHandle.close()
            
        print(str(n) + " is", end = " ")
        if currentIsPrime:
            print("a Prime Number.")
        else:
            print("not a Prime Number.")

PNC = PrimeNumberChecker()
PNC.isPrime(1000777)
PNC.isPrime(1000650)
PNC.isPrime(1000651)

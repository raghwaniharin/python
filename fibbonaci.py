"""
AUTHOR HARIN HARISH
"""
import time
start = time.time()
numfibcalls1 = 0
numfibcalls2 = 0


def fibonacci(x):
    global numfibcalls1
    numfibcalls1 += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


print(fibonacci(13))
print(numfibcalls1)
end = time.time()
timetaken = end-start
print("time taken for computation is " + str(timetaken) + "milliseconds")
start2 = time.time()


def fib_eff(n, d):
    global numfibcalls2
    numfibcalls2 += 1
    if n in d:
        return d[n]
    else:
        ans = fib_eff(n-1, d)+fib_eff(n-2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2}
print(fib_eff(13, d))
print(numfibcalls2)

end2 = time.time()
timetaken2 = end2-start2
print("time taken for computation is " + str(timetaken2) + "seconds")

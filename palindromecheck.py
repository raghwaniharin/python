import time
import tracemalloc
tracemalloc.start()
start_time = time.time()
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve'))

x=input("enter text which you want to check if is a palindrome or not")
print(isPalindrome(x))
end_time = time.time()
time_taken = end_time-start_time
print("time taken for code to run is " + str(time_taken) + "milliseconds")
print("malloc used is " + str(tracemalloc.get_traced_memory()))
tracemalloc.stop()

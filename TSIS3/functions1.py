# A recipe you are reading states how many grams you need for the ingredient. Unfortunately,
#     your store only sells items in ounces. Create a function to convert grams to ounces. \
#         ounces = 28.3495231 * grams

# 1
def gramsToOunces(grams):
    return 28.3495231 * grams

# print(gramsToOunces(100))


# 2
def farToCel(far):
    return  ((5 / 9) * (far-32))

# print(farToCel(32))

# 3
def solve(numheads, numlegs):

    # x + y = numheads (35)
    # 4x + 2y = numlegs (94)
    # 4x+70-2x=94
    rabbits=(numlegs-2*numheads)/2
    chicken= (4*numheads-numlegs)/2
    print("Chiken: " + str(int(chicken)) + " " + "Rabbits: " + str(int(rabbits)))

# solve(35, 94)

# 4
def isPrime(n):
    if n <= 1: return False
    for i in range(2, n):
        if n % i == 0:
            return False;

    return True


def returnPrime(stringg):
    primes = []
    listt = stringg.split(" ")
    for l in listt:
        if isPrime(int(l)):
            primes.append(l)
    return primes

# print(returnPrime("1 2 3 4 5 8"))

# 5
def permute(s, l, r):
    if l == r:
        print(''.join(s));
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]


string = "abc"
n = len(string)
s = list(string)
# permute(s, 0, n - 1)

# 6
def reversee(input):
    inp = input.split(" ")
    ans = ""
    for i in inp[::-1]:
        ans += i
        ans += " "
    return ans

# print(reversee("We are ready"))

# 7
def has_33(l):
    return any(l[i + 1] == l[i] == 3 for i in range(len(l) - 1))

# print(has_33([ 3, 1, 3]))

# 8
def spy_game(nums):
    spy = 0

    for x in range(0, len(nums) - 2):

        if nums[x] == 0 and nums[x + 1] == 0 and nums[x + 2] == 7:
            return True
    return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))

# 9
def volume(radius):
    return ((4/3)*3.14159*radius*radius*radius)

# print(volume(1))

# 10
def unique(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

# print(unique([1,2,3,3,3,3,4,5]))

# 11
def isPalindrome(s):
    return s == s[::-1]


inp = "madam"
ans = isPalindrome(inp)
# if ans:
#     print("Yes")
# else:
#     print("No")

# 12
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

# histogram([2, 3, 6, 5])


# 13
import random
name = input("Hello! What's your name?")
print("Well," + name + ", I am thinking of a number between 1 and 20.Take a guess.")
n = random.randrange(1,20)
count = 1
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Your guess is too low.")
        count+=1
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Your guess is too high.")
        count+=1
        guess = int(input("Enter number again: "))
    else:
      break
print("Good job," + name + "! You guessed my number in " +str(count)+ " guesses!")
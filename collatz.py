import sys
def collatz(n):
    numbersteps = 0
    biggestterm = n
    try:
        while n != 1:
            if n % 2 == 0:
                n = n / 2

            else:
                n = 3*n + 1

            if n > biggestterm:
                biggestterm = n

            numbersteps = numbersteps + 1
            print(n)
        print('Number of iterations = ' + str(numbersteps))
        print('Biggest term = ' + str(biggestterm))
    except n % 2 != 0 and n % 2 != 1:
        print('Error')
        sys.exit()

def collatzcounter(n):
    numbersteps = 0
    biggestterm = n
    print(str(n) + ' : ', end=' ')
    try:
        while n != 1:
            if n % 2 == 0:
                n = n / 2

            else:
                n = 3*n + 1

            if n > biggestterm:
                biggestterm = n

            numbersteps = numbersteps + 1

        print(str(numbersteps) + ', ' + str(biggestterm))
    except n % 2 != 0 and n % 2 != 1:
        print('Error')
        sys.exit()

print('Enter seed')
n = int(input())
collatz(n)

#for i in range(1,101):
  #collatzcounter(i)
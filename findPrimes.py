# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def checkPrimeBetter(num):
    i=2
    while (i**2) <= num :
        if num % i !=0:
            i+=1
        else:
            num=0
            break

    if num !=0:
        return num
    else:
        return num








def checkPrime(num):
    i = 2
    while i < num:
        if num % i != 0:
            i += 1
        else:
            # print('Not a Prime')
            break
    if i == num:
        return num
    else:
        return 0
        # print('{0} is prime'.format(num))


def checkPrimeWithin(number):
    number=int(number)
    prime_list = []
    while number > 1:
        # if (checkPrime(number) != 0):
        if (checkPrimeBetter(number) != 0):
            prime_list.append(number)
            # print(prime_list)
            number -= 1
        else:
            number -= 1
    return prime_list








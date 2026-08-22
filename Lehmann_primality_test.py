import random


def lehmann_test(p, t=5):

    # small numbers
    if p <= 1:
        return False

    if p == 2:
        return True


    for i in range(t):

        # choose random a
        a = random.randint(2, p-2)


        # calculate a^((p-1)/2) mod p

        r = pow(a, (p-1)//2, p)


        # if result is not 1 or -1(p-1)
        if r != 1 and r != p-1:
            return False


    return True



# Main Program

p = int(input("Enter number: "))


if lehmann_test(p):

    print(p, "is probably prime")

else:

    print(p, "is not prime")

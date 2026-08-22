import random



def miller_rabin(p, t=5):

    # Step 1: Handle small numbers

    if p == 2:
        return True

    if p < 2 or p % 2 == 0:
        return False



    # Step 2:
    # Find b and m such that
    # p-1 = 2^b * m

    m = p - 1
    b = 0

    while m % 2 == 0:
        m = m // 2
        b += 1



    # Repeat test t times

    for i in range(t):

        # Step 3:
        # Choose random a

        a = random.randint(2, p-2)



        # Step 4:
        # z = a^m mod p

        z = pow(a, m, p)



        # Step 5:
        # If z = 1 or p-1, pass

        if z == 1 or z == p-1:
            continue



        prime = False


        # Step 6:
        # Repeat squaring

        for j in range(b-1):

            z = pow(z, 2, p)


            if z == p-1:
                prime = True
                break


        if prime:
            continue
        else:
            return False



    return True




# Main Program

p = int(input("Enter number: "))


if miller_rabin(p):

    print(p, "is probably prime")

else:

    print(p, "is not prime")

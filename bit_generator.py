#PSEUDOCODE TOWARDS THE END


num = int(input("Enter your decimal whole number: "))
#num = 0b1010

cycles = int(input("How many generations do you want?: "))

#let generations = 0
generations = 0

#runs for the given number of cycles
while generations < cycles:

    #for the right shift issue

    #right shift number by 1 place
    shifted = num >> 1

    #xor-ing the right shifted number and original number
    xor = shifted^num

    #xor number in binary
    z = bin(xor)[2:]
    #z is a string

    #if right most digit of xor number is 1 or 0
    if z[-1] == "1":
        #it is converted into an n bit number
        r = 0b0001
    else:
        r = 0b0000

    #doing AND operation between r and z/xor (which is z in decimal)
    replacement = r & xor

    #left shifting replacement by 3 places
    lshift_replacement = replacement << 3

    #doing or operation between rshifted num and lshifted replacement
    or_number = shifted | lshift_replacement

    rand_num = bin(or_number)[2:]#result in binary in string type

    #selecting only the last digit as the random bit generated
    rand_num = rand_num[-1]
    print("random number: " + rand_num)
    generations+= 1

    #num is now an int? and not in binary as stored initially
    num = or_number


"""
PSEUDOCODE
Iti's amazing algorithm to generate a random bit - 1 or 0.


Take an n-bit number.
(say 4 bit)
let num = the 4 bit number
eg num = 1001

let generations = 0

while generations < 3 (or however many cycles you want):

    1.Before we begin, there will be a right shift crisis (trailing 0s on the left hand side of the number
    if we keep the algorithm running). So we will find the replacement number first. This will prevent
    every generation's newly generated number from turning into all 0s:

        1a. Do a right shift of num by 1 place.
            - 0100
            - let y = 0100

        1b. Apply XOR truth table to y and num.
            - numXORy = num ⊕ y
            - yields 1101
            - let z = 1101

        1c. Take rightmost digit of z.
            Convert it into an n-bit number.
            - take 1 at the ones place of 1101.
            - convert it into 0001 (4 bit number in this context)
            - let r = 0001

        1d. Take r (0001) and z (1101). Do the AND operation between them.
            - gives us 0001.
            - let replacement = 0001

        We have reached the end of finding the replacement number!
        and taken care of the right shift crisis.

        Let us now proceed with actually generating the random number.

    2. Remember num? Right shift num by 1.
        - num was 1001.
        - on right shifting by 1, we get 0100.
        - let shifted = 0100

    3. Now left-shift replacement by 3 places.
        - replacement is 0001.
        - shifted, it is 1000.
        - let replacement = 1000

    4. FINALLY, do the OR operation on shifted and replacement.
        - shifted OR replacement
        - 0100 OR 1000
        - this gives us 1100.
        - take the rightmost digit > 0.
        - Answer is 0.
        - Print answer.
        - generations++ (taking into account that a generation has passed)
        - the new 'num' is borrowed from the last OR operation:
            num = 1100
            (in the next iteration of the while loop, num will automatically
             start with a new value at hand)


"""
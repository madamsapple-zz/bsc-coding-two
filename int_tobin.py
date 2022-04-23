import math

num = input("Enter an integer: ")
orig_num = num

#func which adds 1 to a binary number (input is bits in a list)
def binary_adder(final):
    for x in range(len(final) - 1, 0, -1):
        #if 1 is added to a 1, then current number becomes a 0 and a '1' is carried over
        if final[x] == 1:
            final[x] = 0
        #if 1 is added to a 0, it becomes a 1 (applies anywhere in the process of carrying over/no carry over)
        elif final[x] == 0:
            final[x] = 1
            break
            #no further change in digits once a 0 is encountered

#main func that represents ints as signed 16 bit numbers
def int_tobin(num):

    #if simply 0 is entered
    if num == "0":
        print("Binary Representation: 0000000000000000")
    
    #for all other ints
    else:

        #if num  is not an int and there is a '-' sign,  remove it and extract the magnitude
        if isinstance(num, str):
            if num[0] == "-":
                num = num[1:]

        #num was originally a string due to input()
        num = int(num)

        #logarithm of num with base 2
        x = math.log(num, 2)
        #returns a float value
        
        #takes the first digit before decimal point, as the nearest power to 2, that can represent its binary number
        x = str(x)
        x = int(x[0])

        #adds '1' as the bit multiplied to that power of 2 (final is a list storing the binary representation)
        #1 is stored as the value at the index of its particular power
        #as a result, the current list stores all bits of the integer in a reverse order
        final[x] = 1

        # (num - (2^nearest power found)) => gives next num to be subjected through the same steps
        num = num - (2**x)

        #if the last power (2^0 = 1) has been reached while running the logarithms
        if num == 0:
            for x in range(len(final)):
                if final[x] == "":
                    final[x] = 0

            #since list was in opposite order, we reverse it to reveal correct order/appearance of binary digits
            final.reverse()

            #if number is negative
            if orig_num[0] == "-":

                #we'll find two's complement by using the +ve binary representation of the int
                
                #bit flip
                for x in range(len(final)):
                    if final[x] == 1:
                        final[x] = 0
                    elif final[x] == 0:
                        final[x]  = 1

                #adds 1 to the number after bit flip
                #for two's complement
                binary_adder(final)

                #prints answer
                print("Binary Representation: ", end = "")

                for x in range(len(final)):
                    print(final[x], end = '')

                print("")

                """
                #binary addition
                for x in range(len(final) - 1, 0, -1):
                    if final[x] == 1:
                        final[x] = 0
                    elif final[x] == 0:
                        final[x] = 1
                        break
                """    

            #else if number is positive
            else:
                print("Binary Representation: ", end = "")

                for x in range(len(final)):
                    print(final[x], end = '')

                print("")

        else:
            int_tobin(num)

#length of size 16 (0-15) to store signed 16 bit number
final = ["" for x in range(0, 16) if True]

int_tobin(num)

#works from -2994 till 2994 so far

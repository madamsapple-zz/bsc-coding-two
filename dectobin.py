import math

"""
pseudocode:


take number.

- if number is 0, then result is 0.

- else
    - make an empty array of length ( (digit just before decimal) + 1 )


A.find the logarithm of that number with base 2.

    - if str(logarithm) is of length 3 (aka ending with a .0/perfect power)
        
        - then, at the index of that logarithm, include a 1
        - fill the rest empty indexes with 0
        - reverse the array for answer
        - quit function

    - else (if logarithm isnt a perfect power)
        - take the first digit before decimal place as logarithm
        - at the index of that logarithm, include a 1
        - then subtract 2^log from orig number (= x)
            - if x is 0
                - fill empty indexes in the array with 0
                - reverse the array for answer
                - quit function
            - else (if x is not 0)
                - repeat function from A
        

print all numbers of array as is







"""

global final

num = int(input("Enter number: "))



def dectobin(num):

    #original power
    power = math.log(num,2)

    #rounded power value
    rounded = int(round(power))

    final[rounded] = 1

    #for performing check
    str_power = str(power)

    #if number is a perfect root
    if (len(str_power) == 3):

        if rounded == 0:

            for x in range(len(final)):
                if final[x] == "":
                    final[x] = 0


        for x in range(0, rounded):
            final[x] = 0

    #if number is not a perfect root
    else:

        if rounded > power:
            dectobin((2 ** rounded) - num)

        elif rounded < power:
            dectobin(num - (2 ** rounded))

        elif rounded == 0:
            final[-1] = 1
            

    #right to left correction for the numbers
    final.reverse()

    

    #answer = "Binary number is {}".format(x for y in final)
    answer = ""
    for x in range(len(final)):
        print(final[x], end = '')

    print("")

power = math.log(num,2)
rounded = int(round(power))

#make an empty array of size (nearest logarithm)
final = ["" for y in range(0, rounded + 1) if True]

#dectobin(num)

#log returns a float value 
# if a perfect log value 1.0 (to one decimal place)
# if log is not perfect then there are 11 places wow 

#print(math.log(8,2))

#IT WORKS!!!
#newlist = ["" for y in range(0, int(2.0)) if True]
#print(newlist[-1])
print(round(1.5))

#numberr = str(9.0)
#print(len(numberr))
#my program is fucked

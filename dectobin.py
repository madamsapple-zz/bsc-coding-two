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



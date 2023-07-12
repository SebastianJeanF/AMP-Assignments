#!/usr/bin/env python3

def validate(numbers_known):
    """

    You have been brought to a party at the house of a rich billionare along with some number of other guests.
    Each of them subtly confides their insecurity to you about how few people they know at the party, telling you 
    a number of people k that they know at the party.

    Being the greatest detective in the world, from their answers, you deduce that somone is lying,
    (and hence of course trying to kill you).

    How did you do this?

    ----

    In this programming task you will receive a list corresponding to the number of people that each person knows.
    That is, the ith element of the list `numbers_known` is the number of people known by person `i`.

    Your job is to return False, if it is possible to detect there at least one liar.
    

    validate([2, 2]) == False
    validate([1, 1]) == True
    validate([2,1,2,1]) == True
    validate([2,1,2,1, 0]) == True
    validate([3]) == False
    validate([2,0,2]) == False

    """

    numbers_known = [number for number in numbers_known if number != 0]
    
    length = len(numbers_known)
    if sum(numbers_known) % 2 == 1:
        return False
    for number in numbers_known:
        if number >= length:
            return False
      
    
        
    return True
assert not validate([2, 2]) 
assert validate([1, 1])
assert validate([2,1,2,1])
assert validate([2,1,2,1, 0]) 
assert not validate([3])
assert not validate([2,0,2])




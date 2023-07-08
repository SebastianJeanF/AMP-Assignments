"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""

def make_change(bills, target, sol = []):
    """
    Find the different ways to make change treating bills of the same denomination as identical.
    Make sure you dont repeat any ways! For instance [1,2,1] and [2,1,1] should be considered the same.

    Example:
    >>> make_smart_change([1, 2, 5], 6))
    [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 1, 2, 1], [1, 1, 2, 1, 1], \
        [1, 1, 2, 2], [1, 2, 1, 1, 1], [1, 2, 1, 2], [1, 2, 2, 1], [1, 5], \
        [2, 1, 1, 1, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1], [2, 2, 2], [5, 1]]
    """
    return

def make_smart_change_best(money, target, highest, sol=[], bestSol=[]):
    """
    Find the different ways to make change treating
    bills of the same denomination as identical, while respecting a limit to 
    coin usage.
    
    For example, money = [(1, 3), (2, 3), (5, 1)] means that there are 3 $1 bills,
    3 $2 bills, and 1 $5 bill. These limits need to respected during solution generation

    Return exactly one solution corresponding to the fewest number of
    bills used. Store only one solution -- the current best solution found.

    >>> make_smart_change_best([(1, 3), (2, 3), (5, 1)], 6, 1)
    [1,5]
    """
    return

def count_change(money, length, target, memo): 
    """
    Recursive code that counts the number of solutions without enumerating solutions.

    Example:
    >>> count_change(money, len(money), 6) 
    5
    >>> count_change(bills2, len(bills2), 16)
    25

    """
    return

if __name__=="__main__":
    print("Making Change!")

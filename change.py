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
   
    solution = []
    if target == 0:
        return [ [] ]
    
    for bill in bills:
        recursion_target = target - bill
        if recursion_target < 0:
            continue
        recursion_solutions = make_change(bills, recursion_target)
        
        for recursion_solution in recursion_solutions:
            recursion_solution.append(bill)
            solution.append(recursion_solution)


    return solution

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
    best_rec_solution = []
    if target == 0:
        return best_rec_solution
    
    for index, (bill, amount) in enumerate(money):
        
        rec_target = target - bill
        if rec_target < 0:
            continue
        
        rec_money = money[:]
        rec_money.pop(index)
        print(rec_money)
        if amount > 1:
          rec_money.append( (bill, amount-1))
      
        rec_solution = make_smart_change_best(rec_money, rec_target, 1)

        # Prevent invalidated solution from propagating
        if len(rec_solution):
            if rec_solution[0] == -1:
                continue
              
        if len(rec_solution) < len(best_rec_solution)-1 or not len(best_rec_solution):
            rec_solution.append(bill)
            best_rec_solution = rec_solution
    
    # Check if branch is invalidated
    if not len(best_rec_solution):
        best_rec_solution.append(-1)

    

    return best_rec_solution

def count_change(money, length, target, memo): 
    """
    Recursive code that counts the number of solutions without enumerating solutions.

    Example:
    >>> count_change([1,2,5], 3, 6) 
    5
    >>> count_change(bills2, len(bills2), 16)
    25

    """

    return

if __name__=="__main__":
    print("Making Change!")
    assert make_smart_change_best([(1, 3), (2, 3), (5, 1)], 6, 1) == [5,1]


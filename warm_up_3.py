def get_side_lengths():
    """Prompts the user to enter three side lengths of a triangle.

    Returns:
      Three float values reprsenting the side lengths of the triangle
    """
    side_1 = float(input("Side 1: "))
    side_2 = float(input("Side 2: "))
    side_3 = float(input("Side 3: "))
    return side_1, side_2, side_3

def classify_triangle(side_1, side_2, side_3):
    
    

    sides = [side_1, side_2, side_3]
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return "does not exist"
    elif sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return "does not exist"
    elif sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "right"
    elif sides[0]**2 + sides[1]**2 < sides[2]**2:
        return "obtuse"
    elif sides[0]**2 + sides[1]**2 > sides[2]**2:
        return "acute"

if __name__ == "__main__":
    side1, side2, side3 = get_side_lengths()
    print(classify_triangle(side1, side2, side3))
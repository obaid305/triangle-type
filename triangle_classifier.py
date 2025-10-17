def classify_triangle(s1, s2, s3):
    # 1. Check for valid triangle and positive sides
    if s1 <= 0 or s2 <= 0 or s3 <= 0 or s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
        return "Not a valid triangle."

    # 2. Classification
    if s1 == s2 and s2 == s3:
        # Equilateral is a type of acute triangle and scalene/isosceles are side classifications
        return "Equilateral (can also be classified as Acute)"
    elif s1 == s2 or s1 == s3 or s2 == s3:
        return "Isosceles triangle"
    else:
        return "Scalene triangle" # No sides are equal

# Test cases
print(classify_triangle(3, 4, 5)) # Scalene
print(classify_triangle(5, 5, 3)) # Isosceles
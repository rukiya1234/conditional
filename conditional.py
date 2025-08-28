 Conditional Exercises

# 1. Even or Odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 2. Largest of three
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# 3. Categorize age
def categorize_age(age):
    if age < 13: return "Child"
    elif age <= 19: return "Teen"
    elif age <= 20: return "Adult"
    else: return "Adult+"

# 4. Triangle type
def triangle_type(a, b, c):
    if a==b==c: return "Equilateral"
    elif a==b or b==c or a==c: return "Isosceles"
    else: return "Scalene"

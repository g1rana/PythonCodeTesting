'''
Given a list of employee object records with performance review scores and associated organization hierarchy,
 find the employee/manager with the highest average score.
'''
# class Employee:
#     def __init__(self, name,score):
#         self.name = name
#         self.score = score
#         self.subordinates = []
    

# def find_highest_average_scco

def find_max(a, b):
    diff = a - b
    sign = (diff >> 31) & 0x1  # Extract sign bit
    print("diff", diff, "sing", sign)
    max_val = a - sign * diff
    return max_val

def find_min(a, b):
    diff = a - b
    sign = (diff >> 31) & 0x1  # Extract sign bit
    print("diff", diff, "sing", sign)
    min_val = b + sign * diff
    return min_val

# Test the functions
num1 = 20
num2 = 10

max_result = find_max(num1, num2)
min_result = find_min(num1, num2)

print("Max:", max_result)
print("Min:", min_result)


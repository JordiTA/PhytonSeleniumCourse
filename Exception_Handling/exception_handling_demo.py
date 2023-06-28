print('-------------------------------------') # Separator

# # Example 1
# Simple try-catch
try:
    a = 5 / 0
except:
    print("DON'T DIVIDE BY 0 !!!")

print('-------------------------------------') # Separator

# # Example 2
# Catch specific exception
'''
try:
    a = 5 / 0
except KeyError:
    print("DON'T DIVIDE BY 0 !!!")
'''
    
print('-------------------------------------') # Separator

# # Example 3
# Print the actual error
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(f"Error has happened: {e}")

print('-------------------------------------') # Separator

# # Example 4
# Catch multiple exceptions in multiple blocks
try:
    a = 5 / 0
    b = {'name': 'foo', 'age': 26}
    x = b['school']
except (KeyError, ZeroDivisionError) as e:
    print(f"Error has happened: {e}")

print('-------------------------------------') # Separator

# # Example 5
# Raise an Exception
# try:
#     a = 5 / 0
#     print(foo)
# except Exception as e:
#     print(f"Error has happened: {e}")
#     raise Exception("Something went wrong.")

print('-------------------------------------') # Separator

# # Example 6
# Re-Raise
try:
    a = 5 / 0
except Exception as e:
    print(f"Error has happened: {e}")
    raise
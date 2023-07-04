print('-------------------------------------') # Separator

# # Example 1
# Function to add two numbers
def addTwoNumbers(a, b):
    sum = a + b
    return sum

total = addTwoNumbers(4,8)
print(total)

print('-------------------------------------') # Separator

# # Example 2
# Function to determine if given state has no sales tax
def hasNoSalesTax(state):

    states_with_no_sales_tax = ['AK', 'DE', 'MT', 'NH', 'OR']

    noTax = None
    if state.upper() in states_with_no_sales_tax:
        return True
    else:
        return False

userState = 'SP'
tax = hasNoSalesTax(userState)
print(tax)

print('-------------------------------------') # Separator
"""def collect_input(num_list):
    while True:
        user_input = input("Enter a number (or Q to quit): ")
        
        # Stop if user enters 'Q' or 'q'
        if user_input.lower() == 'q':
            break
        
        # Check if input is numeric
        if user_input.isnumeric():
            num_list.append(user_input)
        else:
            print("Invalid input. Please enter a number or 'Q' to quit.")
    
    return num_list


# Example usage
numbers = []
result = collect_input(numbers)
print("Final List:", result)

def char_occurrences(text):
    result = []
    for char in text:
        if char not in result:  # only process if not already added
            count = text.count(char)
            result.extend([char, count])
    return result


# Example usage
print(char_occurrences("Hello"))  
# Output: ['H', 1, 'e', 1, 'l', 2, 'o', 1]

def reverse_string_slicing(s):
  return s[::-1]

s="hello"
print(reverse_string_slicing(s))

def data_structure(ds_list, action, data=None, mode="FIFO"):
    if action.lower() == "push":
        ds_list.append(data)
        return ds_list
    
    elif action.lower() == "pop":
        if not ds_list:
            return "Error: Cannot pop from an empty structure."
        
        if mode.upper() == "FIFO":  # Queue behavior
            return ds_list.pop(0)
        elif mode.upper() == "LIFO":  # Stack behavior
            return ds_list.pop()
        else:
            return "Error: Mode must be 'FIFO' or 'LIFO'."
    
    else:
        return "Error: Action must be 'push' or 'pop'."
"""

def push_and_pop(l, s, data, f_l):

    if s.lower() == "push":

        l.append(data)

        return l




    elif s.lower() == "pop":

        if not l:

            print("Cannot pop empty list")

            if f_l.lower =="fifo":

                return l.pop(0)
            elif f_l.lower == "lifo":
                return l.pop()
            else:
                return "Error"
        else:
            return "Error in push or pop"

my_list = []

# FIFO example
push_and_pop(my_list, "push", 0, "FIFO")
push_and_pop(my_list, "push", 1, "FIFO")
push_and_pop(my_list, "push", 2, "FIFO")
print(push_and_pop(my_list, "pop", mode="FIFO"))  # 0
print(push_and_pop(my_list, "pop", mode="FIFO"))  # 1

# Reset for LIFO example
my_list = []
push_and_pop(my_list, "push", 0, "LIFO")
push_and_pop(my_list, "push", 1, "LIFO")
push_and_pop(my_list, "push", 2, "LIFO")
print(push_and_pop(my_list, "pop", mode="LIFO"))  # 2
print(push_and_pop(my_list, "pop", mode="LIFO"))  # 1

# Fizz buzz
for num in range (1,100):
    output = str(num)
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    
    # print(output)

# PASS STATEMENT
# The pass statement is used as a placeholder for future code
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements

# for i in range(10):
#     pass

# CONTINUE STATEMENT
# The continue statement is used to skip the current iteration of the loop
from datetime import datetime

def print_time():
    wait_time = datetime.timestamp(datetime.now()) + 2
    print(f'wait_time: {wait_time}')
    while True:
        if(datetime.timestamp(datetime.now())< wait_time):
            continue
        print(f'waited 2 seconds')
        break
    
print_time()
import time
def some_function():
    start = time.time()
    try:
        time.sleep(1) # 1 second delay
        return 10 / 0
    except Exception as error:
        print("Oops, invalid.")
        return print(error) #division by zero
    finally:
        print(f'''This line is always called.
               One of the use cases is to close a file.
               or to close a database connection.
               or to close a network connection.
               or data cleanup, etc.''')
        end = time.time()
        print(f"Execution time: {end - start}")


some_function()

# MULTIPLE EXCEPTIONS
def some_function_multiple_exception():
# the order of the except blocks is important
# the first exception that matches the error is the one that is executed
    try:
        # raise Exception("This is an exception") # we can raise an exception
        return 10 / "0"
    except ZeroDivisionError:
        print("Oops, ZeroDivisionError.")
    
    except TypeError:
        print("Oops, TYPE ERROR!!!")

    except Exception as error:
        print("Oops, MORE GENERAL EXCEPTION!!!")
    finally:
        print("This line is always called.")
some_function_multiple_exception()
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
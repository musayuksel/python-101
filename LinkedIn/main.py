# Define and call your own functions
def print_hi(name: str) -> None:
    print(f'Hi, {name}')


def square(number: int) -> int:
    return number ** 2


print(f'The square of 4 is {square(4)}')

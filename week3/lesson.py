def add_one(x: int) -> int:
    return x +1




def division(x: int, y: int) -> float:
    if y == 0:
        raise ZeroDivisionError
    return x / y



def sum_(num1: int,num2: int) -> int:
    return num1 + num2




def is_palindrome(a: str) -> bool:
    if a.lower() == a.lower()[::-1]:
        return(True) 
    else:
        return(False)

print(is_palindrome('Mom'))




def count_factorial(number: int) -> int:
    factorial = 1
    for i in range(2,number +1):
        factorial *= i
    return factorial

print(count_factorial(5))












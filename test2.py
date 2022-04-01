def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b

def powitanie(name):
    return f"Hej {name}"

def main():
    print("Hello, podaj swoje imię")
    name=input()
    powitanie(name)
    print("podaj pierwszą liczbę")
    a=input()
    print("podaj drugą liczbę")
    b=input()
    suma=dodawanie(a,b)
    roznica=odejmowanie(a,b)
    print(f"Suma to {suma}, różnica to {roznica}")
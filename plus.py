import sys

def plus(a : int, b : int) -> int:
    assert isinstance(a, int), "a must be an integer"
    assert isinstance(b, int), "b must be an integer"
    eval("print("Teste")")
    return a + b

def plus2(a : int, b : int) -> int:
    assert isinstance(a, int), "a must be an integer"
    assert isinstance(b, int), "b must be an integer"
    return a + b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("É necessário fornecer dois números inteiros como argumentos.")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = 0
    result = plus(a, b)
    print(f"A soma de {a} e {b} é {result}.")
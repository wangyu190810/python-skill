def fibonacci():
    a= b  = 1
    yield a
    yield b
    while True:
        a,b = b, a+b
        yield b


if __name__ == "__main__":
    num = 0
    fib = fibonacci()
    while num< 100:
        num = next(fib)
        print(num)

    

def fabonacci(n):
    a, b = 0, 1
    while n > 0:
        import pdb; pdb.set_trace()
        a, b= b, a+b
        print(b)
        n -= 1

if __name__ == '__main__':
    fabonacci(10)

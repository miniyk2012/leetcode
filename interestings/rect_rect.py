def fact_base(rect):
    def func(x):
        print(str(x) + 'a')
        return 1 if x == 0 else rect(rect)(x-1) * x
    return func


fact = fact_base(fact_base)

for i in range(4, 0, -1):
    print(fact(i))

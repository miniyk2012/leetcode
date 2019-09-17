# from module1 import function3  # 放在function2的内部可以避免循环引用导致的报错

print('function2')
def function2():
    from module1 import function3
    print('Hello, World!')
    function3()
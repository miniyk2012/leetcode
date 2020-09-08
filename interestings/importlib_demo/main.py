from importlib import resources

if __name__ == '__main__':
    print(resources.read_text('data', 'sample.txt'))
    for x in resources.contents('data'):
        print(x)
        if resources.is_resource('data', x):
            print(x)

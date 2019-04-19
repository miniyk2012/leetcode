import math

MULTIPLE_NUM = 707829217


def cross_multiple(un_crossed_list, num):
    multi = 2 * num
    while multi < len(un_crossed_list):
        un_crossed_list[multi] = True
        multi += num


def cross_value(un_crossed_list, need_iter_value):
    for num in range(2, need_iter_value):
        if not un_crossed_list[num]:
            cross_multiple(un_crossed_list, num)


def pick_primes(un_crossed_list):
    primes = []
    for num, crossed in enumerate(un_crossed_list[2:], 2):
        if not crossed:
            primes.append(num)
    return primes


def generate_primes(max_value: int):
    un_crossed_list = [False for _ in range(max_value + 1)]
    need_iter_value = int(math.sqrt(max_value))
    cross_value(un_crossed_list, need_iter_value)
    return pick_primes(un_crossed_list)


def find_two_prime(multi_num):
    min_prime_upper = int(math.sqrt(multi_num))
    prime_list = generate_primes(min_prime_upper)
    for proper_small_prime in prime_list[::-1]:
        if multi_num % proper_small_prime == 0:
            return int(multi_num / proper_small_prime), proper_small_prime
    print('not exist')


def check_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes_test():
    print(generate_primes(20))
    print(generate_primes(100))


def cal_three_num(num):
    total_num = 0
    percent = 0
    for i in range(3, num + 1, 2):
        if i > percent / 100 * num:
            print(f'%{percent}')
            percent += 1
        str_i = str(i)
        total_num += str_i.count("3")
    return total_num


if __name__ == '__main__':
    large, small = find_two_prime(MULTIPLE_NUM)
    print(large, small)
    assert check_prime(large)
    assert check_prime(small)

    total_num = cal_three_num(int(f'{large}{small}'))
    print(total_num)
    'lynn121355'

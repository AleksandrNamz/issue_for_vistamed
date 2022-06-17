# Задание 1.
# print #1 выведет 6, print #2 выведет 67.


# Задание 2.
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
def sort_dict(d):
    # descending sort by values.
    # сортировка словаря по значению в убывающем порядке.
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_dict)
print(sort_dict(d))


# Задание 3.
def find_points(n):
    # first solution using dynamic programming.
    # первое решение с помощью динамического программирования.
    n += 1
    total_spheres = [1, 6, 16] + [0] * (n-3)
    for i in range(3, n):
        total = total_spheres[i-1] + 5 * i
        total_spheres[i] = total
    return total_spheres[n-1]

def spheres(n):
    # mathematical solution.
    # второе решение с помощью математики.
    n += 1
    return int(1 + (5/2 * n * (n-1)))

print(spheres(n), find_points(n))

# Задание 4.
# На мой взгляд код плох:
# 1)если все три числа одинаковые то вернет None.
# 2)если добавить еще числа для выявления максимума, это превратиться в бесконечную простыню кода.
# 3)если речь идет конкретно об этих трех значениях, не нужно использовать 3 if подряд, можно короче

my_dict = {'1': 1, '2': 2, '3': 3}
a, b, c = my_dict['1'], my_dict['2'], my_dict['3']

def myupgratedfunc(a, b, c):
    """return max"""
    if a > b and a > c:
        return a
    elif b > c:
        return b
    return c

def findmax(l):
    """ return maximum from the list"""
    max_num = l[0]
    for i in l:
        if i > max_num:
            max_num = i
    return max_num

print(myupgratedfunc(a, b, c))
print(findmax(list((a, b, c))))

# Задание 5.
# Вы / программа вызывала функцию isTypeOMS, в файле F025Dialog
# интерпритатор не нашел переменную isTypeOMS
# 1) либо опечатались
# 2) либо isTypeOMS не объявлена

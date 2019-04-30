# -*- coding: utf-8 -*-
import random


def check_repeat(a):
    for i in range(len(a)):
        target = a[i]
        for j in range(len(a)):
            if target == a[j] and i != j:
                print(str(i) + " = " + str(j) + " "+ target + " repeated")
    print("checked")


def read_txt(a):
    file = open(a)
    content = file.read()
    file.close()
    arr = content.splitlines()
    check_repeat(arr)
    return arr


def get_new_random(a):
    r = random.randint(0, len(a)-1)
    return r


def join_new(a,b):
    random_a = get_new_random(a)
    random_b = get_new_random(b)
    return a[random_a] + b[random_b] + '\n'


arr_family = read_txt('family.txt')
arr_first = read_txt('first.txt')


family_num = len(arr_family)
first_num = len(arr_first)

combine_array = []

need = 5000
while len(combine_array) < need:
    new_name = join_new(arr_family, arr_first)
    if new_name in combine_array:
        continue
    else:
        combine_array.append(new_name)

file = open('result.txt', 'w')
file.writelines(combine_array)
file.close()

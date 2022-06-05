# Задача заключается в преобразовании случайной строки в строку, введенную с консоли пользователем
# В мутации происходит замена одного случайного гена
# Потомки имеют 50% от родительского генетического кода
# если потомков больше 4, то выживает лишь наиболее приспособленая к жизни
# (наиболее похожая на введенную пользователем) половина популяции
import random
import string


def generate_random_string(length):
    letters = string.ascii_letters + "' .,-!123456789"
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Рандомная строка из", length, "знаков:", rand_string)
    return rand_string


def reproduce(offsprings):  # делаем потомков
    new_off = []
    middle = int(len(offsprings[0]) / 2)
    i = 0
    while i < len(offsprings):
        member1 = list(offsprings[i])
        member2 = list(offsprings[i + 1])
        for j in range(middle, len(member1)):
            a = member2[j]
            member2[j] = member1[j]
            member1[j] = a
        new_off.append(member1)
        new_off.append(member2)
        i += 2
    return new_off


# смотрим насколько различаются строки для отбора популяции
def match(member, str):
    # member = list()
    i = len(str) - 1
    differences = 0
    while i >= 0:
        if str[i] != member[i]:
            differences += 1
        i -= 1
    return differences


# сортировка потомков по важности для эволюции
def select(offsprings, str):
    # вычисляем несхожесть потомков с идеалом
    survival_value = map(lambda x: (match(x, str), x), offsprings)
    selection = list(map(lambda xy: xy[1], sorted(
        survival_value)[:len(offsprings)]))
    return selection


# заменяем рандомный эелемент строки на рандомный символ
def mutation(offspring):
    mut_count = random.randint(0, len(offspring) - 1)
    temp = list(offspring)
    # print(temp)
    letters = string.ascii_letters + "' .,-!123456789"
    temp[mut_count] = random.choice(letters)
    offspring = "".join(temp)
    return offspring


# проделываем мутацию всех потомков
def mutations(offsprings):
    new_generation = []
    for member in offsprings:
        new_generation.append(mutation(member))
    return new_generation


# если в популяции более 4-х потомков, то выживает половина
def survival(offsprings, str):
    off = select(offsprings, str)
    if len(off) > 4:
        print(off[:int(len(off) / 2)])
        return off[:int(len(off) / 2)]
    return off


def the_evolution_of_a_string(str):
    # str = input()
    if len(str) == 0:
        return 'введена пустая строка'
    first_gen1 = generate_random_string(len(str))
    offsprings = []
    offsprings.append(first_gen1)
    offsprings.append(mutation(first_gen1))
    i = 0
    while True:
        new_gen = reproduce(offsprings)
        offsprings += mutations(new_gen)
        offsprings = survival(offsprings, str)
        if offsprings[0] == str:
            # print('эволюция: строка', offsprings[0], 'нашлась на ', i, 'итерации')
            # break
            return i
        if i > 100000:
            # print('эволюции не случилось :(')
            # print('возможно программа пока не умеет работать в введенными символами...')
            # break
            return -1
        i += 1


# if __name__ == "__main__":
#     the_evolution_of_a_string()

import random
from collections import Counter


def door_game(num, change: bool):
    doors_variants = [1, 2, 3]
    doors_in_game = doors_variants.copy()
    random.shuffle(doors_in_game)
    win_door = doors_in_game.pop()
    if win_door != num:
        doors_in_game.remove(num)
    open_door = doors_in_game[0]
    change_variant = [door for door in doors_variants if (door != open_door and door != num)][0]
    if change:
        user_choice = change_variant
    else:
        user_choice = num
    return user_choice == win_door

counting = 10000

#игрок меняет дверь
change_results = []
for i in range(counting):
    change_results.append(door_game(random.randint(1, 3), True))
change_cnt = Counter(change_results)
change_percents = [(i, change_cnt[i] / len(change_results) * 100) for i, count in change_cnt.most_common()]
print(f'При количестве измерений {counting}')
print(f'Результаты при смене двери игроком: {change_cnt}')
print(f'Процентное соотношение: {change_percents}')

#игрок не меняет дверь
no_change_results = []
for i in range(counting):
    no_change_results.append(door_game(random.randint(1, 3), False))
no_change_cnt = Counter(no_change_results)
no_change_percents = [(i, no_change_cnt[i] / len(no_change_results) * 100) for i, count in no_change_cnt.most_common()]
print(f'При количестве измерений {counting}')
print(f'Результаты при смене двери игроком: {no_change_cnt}')
print(f'Процентное соотношение: {no_change_percents}')

print(f'При количестве изменений: {counting}')
print(f'При смене решения шансы выиграть увеличиваются на:'
      f' {(change_cnt[True] - no_change_cnt[True])/ no_change_cnt[True] * 100} %')

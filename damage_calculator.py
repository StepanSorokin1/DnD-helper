def math_expect(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa/n

def hit_probability(kd, bonus, mode = None):
    kd = kd - bonus
    if kd < 1:
        return 1
    if mode == 'adv':
        return min(1 - ((kd-1)/20)**2, 399/400)
    elif mode == 'dis':
        return min((20 - kd + 1)/20, 19/20)**2
    else:
        return min((20 - kd + 1)/20, 19/20)

kd, bonus= map(int, input('Kd and hit bonus: ').split())
mode = input('Mode(adv/dis/no): ')
damage = input('Damage: ')
cube, bonus_damage = damage.split('+')
count, cube = cube.split('k')
bonus_damage, count, cube = map(int, [bonus_damage, count, cube])
expect_damage = count*math_expect(cube) + bonus_damage

hit = hit_probability(kd, bonus, mode)

print(hit*(expect_damage))
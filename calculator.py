def math_expect(n):
    return ((1+n)/2)

def calculate_probability(ac, hit_bonus, mode):
    ac = ac - hit_bonus
    if ac <= 2:
        if mode == 'adv':
            hit_probability = 9/10
            crit_probability = 39/400 
        elif mode == 'dis':
            hit_probability = 9/10 
            crit_probability = 1/400 
        else:
            hit_probability = 18/20 
            crit_probability = 1/20 
    else:
        if mode == 'adv':
            hit_probability = 1 - ((ac - 1)/20)**2 - 39/400 #+
            crit_probability = 39/400 #+
        elif mode == 'dis':
            hit_probability = ((20 - ac)/20)**2 + 2 * (1/20) * (20 - ac)/20
            crit_probability = 1/400 #+
        else:
            hit_probability = (20 - ac)/20 #+
            crit_probability = 1/20 #+
    if ac > 19: hit_probability = 0
    return hit_probability, crit_probability

def expected_damage(ac, hit_bonus, dice_str, dmg_bonus, mode = "no"):
    count, sides = map(int, dice_str.split("k"))

    dice_math_expect = math_expect(sides)
    hit_probability, crit_probability = calculate_probability(ac, hit_bonus, mode)

    dmg = hit_probability * (dice_math_expect) * count
    crit_dmg = crit_probability * dice_math_expect * count * 2
    dpr = dmg + crit_dmg + dmg_bonus
    return dpr


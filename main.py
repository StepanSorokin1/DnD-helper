from utils import *
from dice import *
from calculator import expected_damage
from visualizer import *

while True:
    print("\n=== D&D Helper ===")
    print("1. Быстрый расчет DPR")
    print("2. График DPR")
    print("3. Симуляция костей")
    print("0. Выход")
    choice = input_choice("Выберите режим (Например, '1'): ", ["0", "1", "2", "3"])

    if choice == "1":
        print("\n=== Бытрый расчет DPR ===")
        while True:
            dpr = expected_damage(*input_attack())
            print(f"Ваш DPR = {dpr}")

            if not prompt_choice("Повторить? (y/n): "):
                break

    elif choice == "2":
        print("\n=== График DPR ===")
        while True:
            user_ac, hit_bonus, dice_str, dmg_bonus, mode = input_attack()
            ac_list = [ac for ac in range(1, 31)]
            dmg_list = [round(expected_damage(ac, hit_bonus, dice_str, dmg_bonus, mode), 2) for ac in range(1, 31)]
            
            if prompt_choice("Добавить еще одно оружие для сравнения? (y/n): "):
                _, an_hit_bonus, an_dice_str, an_dmg_bonus, an_mode = input_attack() # an = another
                an_dmg_list = [round(expected_damage(ac, an_hit_bonus, an_dice_str, an_dmg_bonus, an_mode), 2) for ac in range(1, 31)]
                plot_dpr_comparison_graph(ac_list, dmg_list, an_dmg_list, user_ac)
            else:
                plot_dpr_graph(ac_list, dmg_list, user_ac)

            if not prompt_choice("Повторить? (y/n): "):
                break

    elif choice == "3":
        print("\n=== Симуляция костей ===")
        while True:
            dice_str = input_dice("Введите бросок костей в формате 'количествоkгранность', например '2k6': ")
            bonus = input_bonus("Введите бонус к броску, например '0', '+1' или '-2': ")
            rolls = roll_dice(dice_str)
            rolls_sum = sum(rolls) + bonus
            print(f"Значения: {" ".join(list(map(str, rolls)))}")
            print(f"Сумма: {rolls_sum}")

            if not prompt_choice("Повторить? (y/n): "):
                break

    elif choice == "0":
        print("До свидания!")
        break

from utils import *
from dice import *

while True:
    print("\n=== D&D Helper ===")
    print("1. Рассчитать урон")
    print("2. Симуляция костей")
    print("3. Выход")
    choice = input_choice("Выберите режим (Например, '1'): ", ["1", "2", "3"])
    if choice == "1":
        break
    elif choice == "2":
        print("\n=== Симуляция костей ===")
        while True:
            dice_str = input_dice("Введите бросок костей в формате 'количествоkгранность', например '2k6': ")
            bonus = input_bonus("Введите бонус к броску, например '0', '+1' или '-2': ")
            rolls = roll_dice(dice_str)
            rolls_sum = sum(rolls) + bonus
            print(f"Значения: {" ".join(list(map(str, rolls)))}")
            print(f"Сумма: {rolls_sum}")
            if not is_repeat():
                break

    elif choice == "3":
        print("До свидания!")
        break

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
            dice_str = input_dice("Введите кости в формате 'количествоkгранность', например '2k6': ")
            rolls = roll_dice(dice_str)
            print(rolls)
            if not is_repeat():
                break

        
    elif choice == "3":
        break

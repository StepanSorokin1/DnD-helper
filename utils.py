def input_choice(prompt, valid_options):
    while True:
        value = input(prompt).strip().lower()
        if value in valid_options:
            return value
        else:
            print(f"Неправильный формат ввода")

def input_dice(prompt):
    while True:
        value = input(prompt).strip().lower()
        if 'k' in value:
            parts = value.split('k')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                count, sides = int(parts[0]), int(parts[1])
                if count > 0 and sides > 0:
                    return value
        print("Неправильный формат ввода!")

def input_bonus(prompt):
    while True:
        value = input(prompt).strip()
        if value[0] in ["+", "-"] or value == "0":
            if value == "0":
                return int(value)
            if value[0] == "-" and value[1:].isdigit():
                return int(value)
            if value[0] == "+" and value[1:].isdigit():
                return int(value[1:])
        print("Неправильный формат ввода!")

def input_ac(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
            else:
                print("КД должно быть больше 0!")
                continue
        print("Неправильный формат ввода!")

def input_attack():
    ac = input_ac("Введите КД: ")
    hit_bonus = input_bonus("Введите бонус к попаданию, например '0', '+1' или '-2': ")
    dice_str = input_dice("Введите бросок костей в формате 'количествоkгранность', например '2k6': ")
    dmg_bonus = input_bonus("Введите бонус к урону, например '0', '+1' или '-2': ")
    mode = input("Режим (adv/dis/no): ").strip().lower()
    return ac, hit_bonus, dice_str, dmg_bonus, mode
        
def prompt_choice(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Неправильный формат ввода!")
    

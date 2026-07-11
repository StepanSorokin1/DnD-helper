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

def is_repeat():
    while True:
        answer = input("Повторить? (y/n): ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Неправильный формат ввода!")
    

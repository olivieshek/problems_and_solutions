with open("items.txt", "r") as file:
    src = file.read()

item_list = src.splitlines()

pistol = item_list.count('пистолетные')
riffle = item_list.count('ружейные')
tommy = item_list.count('автоматные')
armor = item_list.count('броня')
aid_kit = item_list.count('аптечка')

user_inventory = {
    'пистолетные': pistol,
    'ружейные': riffle,
    'автоматные': tommy,
    'броня': armor,
    'аптечка': aid_kit
}

for name, count in user_inventory.items():
    percent = round(count / len(item_list) * 100, 2)
    print(f"{name}: {percent}%")

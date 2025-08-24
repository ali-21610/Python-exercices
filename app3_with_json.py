# Import JSON data

import json

read_json = "./Miro_menu.json"

with open(read_json, "r") as json_file:
    MENU_LIST=json.load(json_file)



# Empty variables
present_menu_ids = []
client_choice_ids = []
total_quittance = []



# Greetings
print("\n\nWilkommen bei Miro restaurant\n=============================")
    #FIXME How to automatically underline this text ?



# Menu
print("\nPizzen\n======")

for menu in MENU_LIST:
    if menu["menu_type"] == 1:
        print(f"{menu["menu_id"]}. {menu ["menu_name"]} {menu["menu_price"]}€")
    present_menu_ids.append(menu["menu_id"])

print("\n\nAuflauf\n=======")

for menu in MENU_LIST:
    if menu["menu_type"] == 2:
        print(f"{menu["menu_id"]}. {menu ["menu_name"]} {menu["menu_price"]}€")
#FIXME Redondance with Pizzen menu display?



# Client order
print("\n\nWas möchsten Sie bestellen?\n============================")
    #FIXME 1 more "=" in exercise statement, underline not automatically done ?

while True:
    client_choice = int(input("> "))
    if client_choice == 0:
        break
    if client_choice not in present_menu_ids:
        print("Leider bieten wir das nicht an")
    else:
        client_choice_ids.append(client_choice)


# Receipt
print("\n\nQuittung\n========")

for menu in MENU_LIST:
    for each_client_choice in client_choice_ids:
        if each_client_choice == menu["menu_id"]:
            print(f"{menu["menu_id"]}. {menu ["menu_name"]} {menu["menu_price"]}€")
            total_quittance.append(menu["menu_price"])

print(f"\nDie Summe beträgt: {sum(total_quittance)}€")



# Thanks
print("\nVielen Dank für Ihren Besuch!\n")
# Import JSON data
import json

read_json = "./Miro_menu.json"
with open(read_json, "r") as json_file:
    MENU_LIST=json.load(json_file)


# Empty variables
present_menu_ids = []
client_choice_ids = []
total_quittance = []


# Fonctions
def available_menu(menu_type):
    for menu in MENU_LIST:
        if menu["menu_type"] == menu_type:
            print(f"\033[0;33m{menu["menu_id"]}.\033[0m {menu ["menu_name"]} \033[0;33m{menu["menu_price"]}\033[0m€")
        present_menu_ids.append(menu["menu_id"])

def client_decision():
    while True:
        client_choice = int(input("\033[0m> \033[0;33m"))
        if client_choice == 0:
            break
        if client_choice not in present_menu_ids:
            print("\033[0mLeider bieten wir das nicht an")
        else:
            client_choice_ids.append(client_choice)

def quittung():
    for menu in MENU_LIST:
        for each_client_choice in client_choice_ids:
            if each_client_choice == menu["menu_id"]:
                print(f"\033[0;33m{menu["menu_id"]}.\033[0m {menu ["menu_name"]} \033[0;33m{menu["menu_price"]}\033[0m€")
                total_quittance.append(menu["menu_price"])
    print(f"\nDie Summe beträgt: \033[0;33m{sum(total_quittance)}\033[0m€")

#FIXME client_decision & quittung fonctions: What is the interest of fonctions without arguments and called only once in the code? 



# Greetings
print("\n\nWilkommen bei Miro restaurant\n=============================")


# Menu
print("\nPizzen\n======")
available_menu(1)

print("\n\nAuflauf\n=======")
available_menu(2)


# Client order
print("\n\nWas möchsten Sie bestellen?\n============================")
client_decision()


# Receipt
print("\n\n\033[0m Quittung\n========")
quittung()


# Thanks
print("\nVielen Dank für Ihren Besuch!\n")
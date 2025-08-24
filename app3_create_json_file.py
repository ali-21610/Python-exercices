import json
write_json = "C:/Users/admin/Desktop/Exercices_Python/Ex3/Miro_menu.json"


# Constants
MENU_LIST= [
    {"menu_id": 100, "menu_type": 1, "menu_name": "Pizza Margeritta", "menu_price": 5},
    {"menu_id": 101, "menu_type": 1, "menu_name": "Pizza Tunfisch", "menu_price": 6},
    {"menu_id": 102, "menu_type": 1, "menu_name": "Pizza Fungi", "menu_price": 7},
    {"menu_id": 200, "menu_type": 2, "menu_name": "Auflauf Nudeln", "menu_price": 8},
    {"menu_id": 201, "menu_type": 2, "menu_name": "Auflauf Kartoffeln", "menu_price": 9},
]

with open(write_json, "w") as json_file:
    json.dump(MENU_LIST, json_file, indent=4)
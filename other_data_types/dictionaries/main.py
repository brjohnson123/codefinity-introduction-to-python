grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}
bread_details = grocery_inventory["Bread"]
grocery_inventory.update({"Cookies": (143, "Bakery")})
removed_item = grocery_inventory.pop("Eggs")
print ("Details of Bread:", bread_details)
print ("Inventory after adding Cookies:", grocery_inventory)
print ("Inventory after removing Eggs:", removed_item)
                         
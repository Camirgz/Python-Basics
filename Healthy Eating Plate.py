import random

#Lists Initialization
protein_list = []
grains_list = []
fruits_list = []
vegetables_list = []
dish_list = []

#Booleans Initialization
final_boolean = True
protein_boolean = True
grains_boolean = True
fruits_boolean = True
vegetables_boolean = True

while final_boolean:
    while protein_boolean:
        add_protein = str(input("Add a protein, type done, when you've entered all your proteins: "))
        if add_protein.lower() != "done":
            protein_list.append(add_protein)
        else:
            protein_boolean = False
    while grains_boolean:
        add_grains = str(input("Add a grain, type done, when you've entered all your grains: "))
        if add_grains.lower() != "done":
            grains_list.append(add_grains)
        else:
            grains_boolean = False
    while fruits_boolean:
        add_fruits = str(input("Add a fruits, type done, when you've entered all your fruits: "))
        if add_fruits.lower() != "done":
            fruits_list.append(add_fruits)
        else:
            fruits_boolean = False
    while vegetables_boolean:
        add_vegetables = str(input("Add a vegetables, type done, when you've entered all your vegetables: "))
        if add_vegetables.lower() != "done":
            vegetables_list.append(add_vegetables)
        else:
            vegetables_boolean = False
            final_boolean = False

#Random Picking
protein_pick = random.choice(protein_list)
grain_pick = random.choice(grains_list)
fruit_pick = random.choice(fruits_list)

#Make picked vegetables different
first_vegetable_pick = random.choice(vegetables_list)
if len(vegetables_list) > 1:
    vegetables_list.remove(first_vegetable_pick)
    second_vegetable_pick = random.choice(vegetables_list)
    print(f"\nYour healthy plate should contain {protein_pick}, {grain_pick}, {first_vegetable_pick}, {second_vegetable_pick} and {fruit_pick}!")
else:
    print(f"\n Your healthy plate should contain {protein_pick}, {grain_pick}, {first_vegetable_pick} and {fruit_pick}!")

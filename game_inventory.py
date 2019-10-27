def display_inventory(inventory):
        for i, s in inventory.items():
            print(i + ": " + str(s))


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1


def print_table(inventory, order=None):

    if order == None:
        tmp = list(inventory.items())
        Lenght = [len(i) for i in inventory] 
        x = max(Lenght)
        if x < 9:
            x = 9
        print("-" * (x + 8))
        print("item name".rjust(x), "|", "count".rjust(5))
        print("-" * (x + 8))
        for i in range(len(tmp)):
            print((tmp[i][0]).rjust(x), "|", (str(tmp[i][1])).rjust(5) )
        print("-" * (x + 8))
    elif order == "count,desc":
        tmp = list(inventory.items())
        inv_tmp = sorted(tmp, key=lambda thing: thing[1], reverse = True)
        Lenght = [len(i) for i in inventory] 
        x = max(Lenght)
        if x < 9:
            x = 9
        print("-" * (x + 8))
        print("item name".rjust(x), "|", "count".rjust(5))
        print("-" * (x + 8))
        for i in range(len(inv_tmp)):
            print((inv_tmp[i][0]).rjust(x), "|", (str(inv_tmp[i][1])).rjust(5))
        print("-" * (x + 8))
    elif order == "count,asc":
        tmp = list(inventory.items())
        inv_tmp = sorted(tmp, key=lambda thing: thing[1])
        Lenght = [len(i) for i in inventory]  ##   Itt tartok 
        x = max(Lenght)
        if x < 9:
            x = 9       
        print("-" * (x + 8))
        print("item name".rjust(x), "|", "count".rjust(5))
        print("-" * (x + 8))
        for i in range(len(inv_tmp)):
            print((inv_tmp[i][0]).rjust(x), "|", (str(inv_tmp[i][1])).rjust(5))
        print("-" * (x + 8))


def import_inventory(inventory, filename="import_inventory.csv"):

    try:
        inv_temp = []
        tmp = []
        with open (filename, "r") as f:
            inv_temp.append(f.readline())

        for i in inv_temp:
            tmp.append(i.split(",",-1))

        for i in tmp[0]:
            if i in inventory:
                inventory[i] = inventory[i] + 1
            else:
                inventory[i] = 1
    except:
        print(f"File '{filename}' not found!")


def export_inventory(inventory, filename="export_inventory.csv"):

    try:
        tmp = []
        for key, value in inventory.items():
            for x in range(value):
                tmp.append(key)

        with open(filename, "w") as f:
            for item in tmp:
                if x != len(tmp)-1:
                    f.write("%s," % item)
                    x+=1
                else:
                    f.write(item)
    except:
        print(f"You don't have permission creating file '{filename}'!")

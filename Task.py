def get_through():
    res = []
    cook_book = {}
    with open("recipes.txt", "r", encoding="UTF-8") as recipes:
        for lines in recipes:
            res.append(lines)
            if res[-1][-1] == "\n":
                res[-1] = res[-1][:-1]
            else:
                get_book(res, cook_book)
                res.clear()
                break
            if res[-1] == "":
                res = res[:-1]
                get_book(res, cook_book)
                res.clear()
    return cook_book


def get_book(res, cook_book):
    cook_book[res[0]] = []
    for i in range(int(res[1])):
        res[i + 2] = res[i + 2][:res[i + 2].find("|") - 1] + res[i + 2][res[i + 2].find("|") - 1:res[i + 2].rfind("|") + 2].replace(" ", "") + res[i + 2][res[i + 2].rfind("|") + 2:]
        a = res[i + 2].split("|")
        cook_book[res[0]].append({})
        cook_book[res[0]][-1]["ingredient_name:"] = a[0]
        cook_book[res[0]][-1]["quantity:"] = int(a[1])
        cook_book[res[0]][-1]["measure:"] = a[2]


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_through()
    order = {}
    for position in dishes:
        for ingr in cook_book[position]:
            if ingr["ingredient_name:"] in order.keys():
                order[ingr["ingredient_name:"]]["quantity:"] = ingr["quantity:"] * person_count + order[ingr["ingredient_name:"]]["quantity:"]
            else:
                order[ingr["ingredient_name:"]] = {"measure:": ingr["measure:"], "quantity:": ingr["quantity:"]*person_count}

    return order


print(get_shop_list_by_dishes(["Утка по-пекински", "Омлет"], 100))
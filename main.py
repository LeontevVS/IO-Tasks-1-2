from pprint import pprint

def get_cook_boock():
    path = r'files/file.txt'
    with open(path, 'r', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            ingredients_count = int(file.readline())
            cook_book[dish] = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, mesure = file.readline().split(" | ")
                cook_book[dish] += [{'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity), 'measure': mesure.strip()}]
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_key, dish_ingredients in get_cook_boock().items():
        if dish_key in dishes:
            for ingredient in dish_ingredients:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity']
                measure = ingredient['measure']
                if shop_list.get(name) is None:
                    shop_list[name] = {'measure': measure, 'quantity': quantity * person_count}
                else:
                    shop_list[name]['quantity'] += quantity * person_count
    return shop_list

if __name__ == '__main__':
    print("Кулинарная книга:")
    pprint(get_cook_boock())
    print("\nСписок ингредиентов:")
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
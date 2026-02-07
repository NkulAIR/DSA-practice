import itertools
# ============================
# TODO:Question 1
# ============================
def split_coords(coordinates: list) -> tuple:

    side_1, side_2 = [],[]
    for i in coordinates:
        if len(i) % 2 != 0:
            raise ValueError
        side_2.append(i[1])
    for i in coordinates:
        side_1.append(i[0])
    
    return (side_1, side_2)


# print(split_coords([(1, 2), (3, 4), (5, 6)])) # [1, 3, 5], [2, 4, 6]
# print(split_coords([(10, 20), (30, 40), (50, 60), (70, 80)])) # ([10, 30, 50, 70], [20, 40, 60, 80])

# ============================
# TODO:Question 2
# ============================
def create_id_lookup(user_data: list) -> dict:
    runners = {}
    for i, j in enumerate(user_data):
        if i not in runners:
            runners[j] = i
        else:
            runners[j] = i + i
    return runners


# print(create_id_lookup(["Alice", "Bob", "Alice"]))



# ============================
# TODO:Question 3
# ============================
def extract_unique_tags(posts: list) -> set:
    new_dict = {}

    for i in posts:
        if i.lower() not in new_dict:
            new_dict[i.lower()] = 0
    

    new_data = [j for j in new_dict.keys()] # --> {'python', 'data', 'code'}
    return set(new_data)



# print(extract_unique_tags(['Python', 'python', 'Data', 'data', 'DATA', 'Code']))



# ============================
# TODO:Question 4
# ============================
def group_by_category(items: list) -> dict:
    categories = {}
    
    for item in items:
        for i in item:
            categories[item['type']] = []
        
            for food in items:
                if food['type'] in categories:
                    if food['name'] not in categories[food['type']]:
                        categories[food['type']].append(food['name'])

    return categories



itms = [
    {'name': 'Salmon', 'type': 'Fish'},
    {'name': 'Tuna', 'type': 'Fish'},
    {'name': 'Lettuce', 'type': 'Vegetable'}
]

# print(group_by_category(itms))
# print(group_by_category([{"name": "Boerewors", "type": "Meat"}, {"name": "Charcoal", "type": "Hardware"}, {"name": "Lamb Chops", "type": "Meat"},{"name": "Chakalaka", "type": "Canned Goods"}]))

# ============================
# TODO:Question 5
# ============================
def batch_api_dispatcher(user_ids: list | tuple) -> list:
    count = 0
    groups = []

    l = 0
    r = 5

    if user_ids == []:
        return
    
    count = 0
    # mid = l + r // 2

    # while r <= len(user_ids):
    #     # l = 0
    #     for i in range(5):
    #         print(user_ids[l:])
    #     l += 5

    return groups


print(batch_api_dispatcher(['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7','ID8', 'ID9', 'ID10', 'ID11', 'ID12', 'ID13', 'ID14', 'ID15']))
# ============================
# TODO:Question 6
# ============================
def social_graph_inverter(following_list: dict) -> dict:
    
    return {}


# ============================
# TODO:Question 7
# ============================
def fibonacci_generator(n: int) -> list:
    fib_list = []
    for i in range(n):
        fib_list.append(fibo(i))
    
    return fib_list

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)


print(fibonacci_generator(100))


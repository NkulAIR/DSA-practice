
def main():
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    recipe =  {"flour": 500, "sugar": 200, "eggs": 1}
    print(cakes(recipe, available))

def cakes(recipe, available):
    return min(map(lambda x: available.get(x,0) // recipe[x],recipe))
    # return available[key] // recipe[key]
    rec_ = set(recipe)
    ava_ = set(available)
    cost_of_one = recipe.values()


    no_of_cakes = 0

    if len(rec_.difference(ava_)) == 0:
        for a in recipe.keys():
            if available[a] >= recipe[a]:
                print(int(available[a] // recipe[a]))
            else:
                return no_of_cakes
 
    else:
        return no_of_cakes


main()
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicey_food =[f["name"] for f in spicy_foods]
    return spicey_food

def get_spiciest_foods(spicy_foods):
    spacey = [sp for sp in spicy_foods if sp["heat_level"] > 5]
    return spacey

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for meal in spicy_foods:
        mlo = meal["cuisine"]
        if cuisine == mlo:
            return meal

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat = "🌶" * food["heat_level"]
        if food["heat_level"] > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat}")
def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        heat = food["heat_level"]
        count = len(spicy_foods)
        total = total+ food["heat_level"]
        average = total/count
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


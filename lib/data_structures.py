# lib/data_structures.py

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

# Function to return the names of each spicy food
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# Function to return foods with heat level greater than 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# Function to print each spicy food in the specified format
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")

# Function to find a spicy food by cuisine type
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

# Function to print only the spiciest foods
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# Function to calculate the average heat level of all spicy foods
def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods) if spicy_foods else 0

# Function to add a new spicy food to the list
def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods

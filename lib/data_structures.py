# data_structures.py

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

# 1. Function to get names of spicy foods
def get_names(foods):
    return [food["name"] for food in foods]

# 2. Function to get spiciest foods
def get_spiciest_foods(foods):
    return [food for food in foods if food["heat_level"] > 5]

# 3. Function to print spicy foods
def print_spicy_foods(foods):
    for food in foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# 4. Function to get spicy food by cuisine
def get_spicy_food_by_cuisine(foods, cuisine):
    for food in foods:
        if food["cuisine"] == cuisine:
            return food
    return None

# 5. Function to print spiciest foods
def print_spiciest_foods(foods):
    spiciest_foods = get_spiciest_foods(foods)
    print_spicy_foods(spiciest_foods)

# 6. Function to calculate average heat level
def average_heat_level(foods):
    total_heat = sum(food["heat_level"] for food in foods)
    return total_heat // len(foods)  # Integer division

# 7. Function to create a new spicy food
def create_spicy_food(foods, new_food):
    foods.append(new_food)
    return foods

# Example usage (uncomment to test)
if __name__ == "__main__":
    print(get_names(spicy_foods))  # ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
    print(get_spiciest_foods(spicy_foods))  # [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]
    print_spicy_foods(spicy_foods)  # Prints all spicy foods
    print(get_spicy_food_by_cuisine(spicy_foods, "American"))  # {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}
    print_spicy_foods(spicy_foods)  # Prints foods with heat level > 5
    print(average_heat_level(spicy_foods))  # 6
    new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    create_spicy_food(spicy_foods, new_food)
    print(spicy_foods)  # New food added

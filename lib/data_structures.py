#!/usr/bin/env python3

# Sample data for testing (this is provided in the lab)
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
    """
    Returns a list of strings with the names of each spicy food.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
        
    Returns:
        list: List of food names as strings
        
    Example:
        get_names(spicy_foods) -> ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
    """
    # Use list comprehension to extract the "name" key from each dictionary
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """
    Returns a list of dictionaries where the heat level is greater than 5.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
        
    Returns:
        list: List of dictionaries with heat_level > 5
    """
    # Use list comprehension with condition to filter foods with heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """
    Prints each spicy food in the format: "Name (Cuisine) | Heat Level: 🌶🌶🌶"
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
    """
    # Loop through each food and print in the required format
    for food in spicy_foods:
        # Create the pepper emoji string by multiplying "🌶" by heat_level
        peppers = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns a single dictionary for the spicy food that matches the given cuisine.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
        cuisine: String representing the cuisine to search for
        
    Returns:
        dict: Dictionary of the food that matches the cuisine
    """
    # Loop through foods and return the first one that matches the cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    # Return None if no match is found (though the lab assumes there will always be a match)
    return None


def print_spiciest_foods(spicy_foods):
    """
    Prints only the spicy foods that have a heat level greater than 5,
    in the same format as print_spicy_foods().
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
    """
    # First get the spiciest foods, then print them
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)


def get_average_heat_level(spicy_foods):
    """
    Returns the average heat level of all spicy foods.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
        
    Returns:
        int: Average heat level (rounded down to integer)
    """
    # Calculate total heat level
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    # Calculate average and return as integer
    return total_heat // len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    """
    Returns the original list with the new spicy_food added.
    
    Args:
        spicy_foods: List of dictionaries containing spicy food data
        spicy_food: Dictionary representing the new spicy food to add
        
    Returns:
        list: New list with the additional spicy food
    """
    # Create a new list by adding the new food to the existing list
    return spicy_foods + [spicy_food]


# Test the functions (you can run this to verify your solutions)
if __name__ == "__main__":
    print("Testing get_names():")
    print(get_names(spicy_foods))
    
    print("\nTesting get_spiciest_foods():")
    print(get_spiciest_foods(spicy_foods))
    
    print("\nTesting print_spicy_foods():")
    print_spicy_foods(spicy_foods)
    
    print("\nTesting get_spicy_food_by_cuisine():")
    print(get_spicy_food_by_cuisine(spicy_foods, "American"))
    
    print("\nTesting print_spiciest_foods():")
    print_spiciest_foods(spicy_foods)
    
    print("\nTesting get_average_heat_level():")
    print(get_average_heat_level(spicy_foods))
    
    print("\nTesting create_spicy_food():")
    new_food = {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}
    print(create_spicy_food(spicy_foods, new_food))
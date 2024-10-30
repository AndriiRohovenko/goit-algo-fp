items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Greedy approach
def greedy_algorithm(items, budget):
    # Sort items by the ratio of calories to cost in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for item, details in sorted_items:
        if details["cost"] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]

    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    
    for i in range(1, len(items) + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]["cost"]
        item_calories = items[item_name]["calories"]

        for w in range(budget + 1):
            if item_cost <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], dp_table[i - 1][w - item_cost] + item_calories)
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    chosen_items = []
    temp_budget = budget
    for i in range(len(items), 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            temp_budget -= items[item_name]["cost"]

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


# Example usage
budget = 150

# Run the greedy algorithm
greedy_result = greedy_algorithm(items, budget)
print("Greedy Result:")
print("Total Calories:", greedy_result[0])
print("Remaining Budget:", greedy_result[1])
print("Chosen Items:", greedy_result[2])

# Run the dynamic programming algorithm
dp_result = dynamic_programming(items, budget)
print("\nDynamic Programming Result:")
print("Total Calories:", dp_result[0])
print("Remaining Budget:", dp_result[1])
print("Chosen Items:", dp_result[2])

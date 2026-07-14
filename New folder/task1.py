# Example: Student Marks Management

def list_operations():
    print("\n--- LIST OPERATIONS ---")

    marks = [78, 85, 90, 66]
    print("Initial marks:", marks)

    marks.append(88)               # Add mark
    marks.insert(1, 80)            # Insert at index
    marks.remove(66)               # Remove value
    marks.sort(reverse=True)       # Sort descending

    avg = sum(marks) / len(marks)

    print("Updated marks:", marks)
    print("Average marks:", avg)

def tuple_operations():
    print("\n--- TUPLE OPERATIONS ---")

    server_config = ("localhost", 8080, "HTTPS")
    print("Server config:", server_config)

    host, port, protocol = server_config
    print("Host:", host, "Port:", port, "Protocol:", protocol)


# SET (Unique, Unordered)
# Example: Unique User IDs

def set_operations():
    print("\n--- SET OPERATIONS ---")

    users = {"u1", "u2", "u3"}
    new_users = {"u3", "u4"}

    users.add("u5")
    common = users.intersection(new_users)
    all_users = users.union(new_users)

    print("Users:", users)
    print("Common users:", common)
    print("All users:", all_users)


# DICTIONARY (Key-Value)
# Example: Product Inventory

def dict_operations():
    print("\n--- DICTIONARY OPERATIONS ---")

    inventory = {
        "Laptop": 10,
        "Mouse": 50,
        "Keyboard": 30
    }

    inventory["Mouse"] += 10
    inventory["Monitor"] = 15

    for item, qty in inventory.items():
        print(item, ":", qty)


# COMPREHENSIONS
def comprehension_operations():
    print("\n--- COMPREHENSIONS ---")

    numbers = [1, 2, 3, 4, 5, 6]

    squares = [x**2 for x in numbers]
    even_set = {x for x in numbers if x % 2 == 0}
    square_dict = {x: x**2 for x in numbers}

    print("Squares:", squares)
    print("Even numbers set:", even_set)
    print("Square dictionary:", square_dict)

if __name__ == "__main__":
    list_operations()
    tuple_operations()
    set_operations()
    dict_operations()
    comprehension_operations()

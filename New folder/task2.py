def list_training():
    print("\n--- LIST TRAINING ---")
    marks = [70, 85, 90, 60]

    marks.append(88)
    marks.insert(1, 75)
    marks.remove(60)
    marks.sort(reverse=True)

    print("Marks:", marks)
    print("Average:", sum(marks) / len(marks))


def tuple_training():
   t1=(1,2)
   t2=(3,4)
   t3=t1+t2
   print(t3)

   numbers=(1,2,3,34,44,3)
   print(numbers.count(3))

   print(t2*3)



def set_training():
    print("\n--- SET TRAINING ---")
    users = {"user1", "user2", "user3"}
    new_users = {"user3", "user4"}

    print("All Users:", users | new_users)
    print("Common Users:", users & new_users)


# ------------------------------------------
# 4. DICTIONARY – Inventory System
# ------------------------------------------
def dict_training():
    print("\n--- DICTIONARY TRAINING ---")
    inventory = {
        "Laptop": 10,
        "Mouse": 50,
        "Keyboard": 30
    }

    inventory["Mouse"] += 10
    inventory["Monitor"] = 15

    for item, qty in inventory.items():
        print(item, ":", qty)




# STRING BASICS
def string_basics():
    print("\n--- STRING BASICS ---")
    s = "  Python Programming  "
    print("Lower:", s.lower())
    print("Upper:", s.upper())
    print("Stripped:", s.strip())
    print("Replace:", s.replace("Python", "Java"))


#  STRING REVERSAL & PALINDROME
def reverse_and_palindrome():
    print("\n--- REVERSE & PALINDROME ---")
    s = "madam"
    reversed_s = s[::-1]

    print("Reversed:", reversed_s)
    print("Palindrome:", s == reversed_s)


if __name__ == "__main__":
    list_training()
    tuple_training()
    set_training()
    dict_training()

    string_basics()
    reverse_and_palindrome()
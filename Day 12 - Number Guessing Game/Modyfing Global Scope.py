#Modifying Global Scope

enemies = 1 # Global Scope

def increase_enemies():
    print(f"enemies inside the function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies out of the function are: {enemies}")

# Global Constants

PI = 3.14159
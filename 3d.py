import random

random_numbers = "*".join(f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}" for _ in range(10))
print(random_numbers)

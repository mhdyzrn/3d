import random

def generate_random_numbers(digit_count, amount=10):
    return "*".join("".join(str(random.randint(0, 9)) for _ in range(digit_count)) for _ in range(amount))

# Pilih jumlah digit (2, 3, atau 4)
digit_choice = int(input("Masukkan jumlah digit (2, 3, atau 4): "))

if digit_choice in [2, 3, 4]:
    print(generate_random_numbers(digit_choice))
else:
    print("Pilihan tidak valid. Masukkan 2, 3, atau 4.")

roles = {
    "admin": 'Markus',
    "maintainer": 'Bobby',
    "manager": 'Garry',
    "developer": 'Carlos'}

name = input("My name is, ")
for role, names in roles.items():
    if name in names:
        print(f"Hello, {role}")
        break
else:
    print("Hello, Guess")
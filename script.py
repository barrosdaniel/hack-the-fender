import csv

compromised_users = []

with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for row in password_csv:
        password_row = row
        compromised_users.append(password_row['Username'])

print(compromised_users)

with open('compromised_users.txt', 'w') as compromised_user_file:
    for username in compromised_users:
        compromised_user_file.write(f"\n{username}")
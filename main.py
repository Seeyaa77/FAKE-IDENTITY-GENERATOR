#follow ig @rapleeeyyy
from faker import Faker

fake = Faker()

a = int(input('Enter how many names you want to generate: '))
b = int(input('Enter how many ADDRESS you want to generate?: '))

name_output = []  # List to store generated names
address_output = []  # List to store generated addresses

for _ in range(a):
    name_output.append('Fake name: ' + fake.name())

for _ in range(b):
    address_output.append('Address: ' + fake.address())

asw = input('want to use fake IP?(yes/no): ')

ip_output = []  # List to store generated IP addresses

if asw == 'yes':
    banyak = int(input('how much u want to gen?: '))
    
    for _ in range(banyak):
        ip_output.append('Fake IP: ' + fake.ipv4_private())

with open('fake_names.txt', 'w') as name_file:
    name_file.write('\n'.join(name_output))

with open('fake_addresses.txt', 'w') as address_file:
    address_file.write('\n'.join(address_output))

if asw == 'yes':
    with open('fake_ips.txt', 'w') as ip_file:
        ip_file.write('\n'.join(ip_output))

print('Output saved to text files.')

from faker import Faker

fake = Faker()

print("Случайное имя:", fake.name())
print("Случайный адрес:", fake.address())
print("Случайный город:", fake.city())
print("Случайная страна:", fake.country())
from faker import Faker

d = {'ismi': ['Erica']}
print(d.items())
# d = {key: value[0] for key, value in d.items()}
print(d)


def f(ismi=None, n=None):
    print(ismi, n)


k = ['ismi', 'Erica']
f(**{key: value[0] for key, value in d.items()})

fake = Faker()
print(fake.name())
print(fake.first_name())
print(fake.file_name())

rows = 74
for num in range(rows):
    for i in range(num):
        print(num, end=" ")
    print(' ')


person1 = input("введите количество учеников:")
person2 = input("введите количество учеников:")
person3 = input("введите количество учеников:")

tables1 = int(person1)//2 if int(person1)%2 == 0 else int(person1) //2 +1
tables2 = int(person2)//2 if int(person2)%2 == 0 else int(person2) //2 +1
tables3 = int(person3)//2 if int(person3)%2 == 0 else int(person3) //2 +1

print(tables1, tables2, tables3)
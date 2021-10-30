# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician + '\n')

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

# 创建数值列表
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)

# 打印1~10内的偶数
print("打印1~10内的偶数")
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print()

print("打印1~10的平方")
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print()

# 最小值
print("数字列表中最小值")
print(min(squares))
# 最大值
print("数字列表中最大值")
print(max(squares))
# 和
print("数字列表中值的和")
print(sum(squares))
print()

# 列表解析
print("列表解析")
squares = [value**2 for value in range(1,11)]
print(squares)
print()

# 3的倍数
print("3的倍数")
three = []
for i in range(3, 31, 3):
    three.append(i)
print(three)
for a in three:
    print(a)

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:3])
print(players[:4])
print(players[3:])
print(players[-3:])

for player in players[-3:]:
    print(player.title())

# 复制列表
print("复制列表")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# friend_foods = my_foods 这个不行，两个变量指向同一个列表

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print()

# 验证确实是两个列表
print("验证确实是两个列表")
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print()

# 元组  Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组
print("元组")
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
print()

# 我们首先定义了一个元组，并将其存储的尺寸打印了出来；
# 接下来，将一个新元组存储到变量dimensions中；
# 然后，打印新的尺寸。
# 这次Python不会报告任何错误，因为给元组变量赋值是合法的：
print("修改元组变量")
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
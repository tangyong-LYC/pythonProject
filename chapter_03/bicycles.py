# 打印列表中数据
print("打印列表中数据")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1].title())
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print()

# 修改列表元素
print("修改列表元素")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
print()

# 添加列表元素
print("添加列表元素")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
print()

# 在列表中插入元素
print("在列表中插入元素")
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
print()

# 在列表中删除元素
print("在列表中删除元素")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)
print()

# 使用方法pop() 删除元素
print("使用方法pop() 删除元素")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 弹出末尾的元素
print("弹出末尾的元素")
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 弹出任意位置的元素
print("弹出任意位置的元素")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)
print()

# 根据值删除元素
# 注意 　方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
print("根据值删除元素")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
print()

# 修改列表排序
print("修改列表排序(永久性)")
print("按字母顺序排序")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print("正向: " + str(cars))
cars.sort(reverse=True)
print("倒排: " + str(cars) + "\n")

print("修改列表排序(保留原有排序)")
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("倒排: " + str(sorted(cars,reverse=True)))

print("\nHere is the original list again:")
print(str(cars) + "\n")

# 倒着打印列表
print("倒着打印列表")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
print()

# 确定列表的长度
# 注意 　Python计算列表元素数时从1开始，因此确定列表长度时，你应该不会遇到差一错误。
print("确定列表的长度")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
print()

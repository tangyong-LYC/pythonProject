print("Hello Python world!")

a = "This is a string."
print(a)

b = 'This is a string.'
print(b)

c = '''Alia say "I'm Alia"'''
print(c)

d = "tang"
# 首字母大写
print(d.title())
# 全部大写
print(d.upper())
# 全部小写
f = "YoNg"
print(f.lower())

print(d.lower() + " " + f.lower())
# 制表符
print("\tPython")
# 换行符
print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Python能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白
favorite_language = ' python '
print(favorite_language)
# 清除末尾的空白
print(favorite_language.rstrip())
# 清除开头的空白
print(favorite_language.lstrip())
# 清除开头和末尾的空白
print(favorite_language.strip())

print(3-4)
print(3*4)
print(3/4)
print(3+4)
print(3**4)
print(0.33+4)
print(0.33*4)
print(0.2+0.1)
print(3*0.1)
print(0.2+0.3)
c = 18
print(d.lower() + " " + f.lower() + str(c))

# Напишите функцию, которая проверяет: является ли слово палиндромом
def Palindrome(s):
    return s == s[::-1]

s = "арозаупаланалапуазора"
a = Palindrome(s)
if a:
    print("Да")
else:
    print("Нет")
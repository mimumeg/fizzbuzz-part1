number = int(input("1つ目の自然数を入れてね:"))

if number % 3 == 0:
    output = "Fizz"
else:
    # 整数型から文字列型に変換
    output = str(number)

print(output)

sum = 100
number = 1
operator = int(input("어떤 연산할 것인지: "))

while True:
    if operator == 1:
        number = int(input("숫자 입력: "))
        sum += number
        if number <= 100:
            continue
        print("100 미만을 적으시오")
    elif operator == 2:
        number = int(input("숫자 입력: "))
        sum -= number
        if number <= 100:
            continue
        print("100 미만을 적으시오")
    elif operator == 3:
        number = int(input("숫자 입력: "))
        sum *= number
        if number <= 100:
            continue
        print("100 미만을 적으시오")
    elif operator == 4:
        number = int(input("숫자 입력: "))
        sum /= number
        if number <= 100:
            continue
        print("100 미만을 적으시오")
        if number == 1:
          break
num = sum
print(f"{num:.2f}")

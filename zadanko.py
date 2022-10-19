# 1. Napisz funkcję, która przyjmie rok urodzenia, a następnie zwróci informację o tym, czy jest pełnoletni czy nie.
def check_adult(age):
    if int(age) >= 18:
        print("adult")
    else:
        print("non adult")


check_adult(34) # Pełnoletni
check_adult(17) # Niepełnoletni


# 2. Napisz funkcję, która zwraca listę wszystkich podzielnych przez n liczb z zakresu [1, 100].
def divisible(n):
    for i in range(1, 101):
        if i % n == 0:
            print(i)


divisible(3) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
divisible(5) # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
divisible(8) # [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]


# 3. Napisz funkcję, która przyjmuje kwotę (value) i jej walutę (currency), a następnie zwróci ile wart jest dana kwota w danej walucie w złotówkach.
[
    {
        "currency": "USD",
        "value": 4.56
    }, {
    "currency": "CHF",
    "value": 5.03
}, {
    "currency": "EUR",
    "value": 4.9
}
]


def check_currency(value, currency):
    if currency == "USD":
       z = (4.56 * value)
       print("%.0f" % z)
    elif currency == "CHF":
        z = (5.03 * value)
        print("%.2f" % z)
    elif currency == "EUR":
        z = (4.9 * value)
        print("%.1f" % z)




check_currency(745, "CHF")  # 3747,35 zł
check_currency(812.5, "USD")  # 3705 zł
check_currency(18, "EUR")  # 88,2 zł

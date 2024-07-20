import re

def generator_numbers(text: str):
    pattern = r"\d+\.\d+|\d+"
    for match in re.findall(pattern, text):
        yield float(match)




def sum_profit(text: str, func: callable):
    total_income = 0
    for number in generator_numbers(text):
        total_income += number
    return total_income

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


# Очікуване виведення: Загальний дохід: 1351.46
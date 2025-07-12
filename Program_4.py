def count_multiples(input_list):
    output_counts = {}
    divisors = range(1, 10)

    for divisor in divisors:
        count = 0
        for number in input_list:
            if number % divisor == 0:
                count += 1
        output_counts[divisor] = count
    return output_counts

input_data = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = count_multiples(input_data)
print(result)

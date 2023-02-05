file = 'foods.txt'

daily_intake = {
    "Vitamin A": 3000.0,
    "Vitamin B1": 1.5,
    "Vitamin B2": 1.3,
    "Vitamin B3": 16.0,
    "Vitamin B6": 11.7,
    "Vitamin B12": 2.4,
    "Vitamin C": 90.0,
    "Vitamin D": 15.0,
    "Vitamin E": 15.0,
    "Vitamin K": 120.0
}
foods = {}

with open(file) as f:
    for line in f.readlines():
        item = line.split(', ')
        food_name = item[0]

        vitamin = []
        for i in range(1, len(item)):
            vitamin.append(item[i].strip())

        foods[food_name.lower()] = vitamin

food = {'breakfast': None, 'lunch': None, 'dinner': None}

for meal in food.keys():
    ate = input(f'What did you eat for {meal}: ')

    while ate.lower() not in foods.keys():
        print('Error: Food not in database')
        ate = input(f'What did you eat for {meal}: ')

    food[meal] = ate

print('--------------------------')

vitamin_taken = {}

for meal in food.values():
    if meal in foods:
        for vitamin in foods[meal]:
            vitamin_pair = vitamin.split(': ')
            vitamin_name = vitamin_pair[0]
            vitamin_count = vitamin_pair[1]

            if vitamin_name not in vitamin_taken:
                vitamin_taken[vitamin_name] = vitamin_count
            else:
                unit = vitamin_taken[vitamin_name].split(' ')[1]
                curr = float(vitamin_taken[vitamin_name].split(' ')[0])
                new_amount = float(vitamin_count.split(' ')[0])

                total = curr + new_amount
                total = str(total) + ' ' + unit
                vitamin_taken[vitamin_name] = total

for vitamin, amount in vitamin_taken.items():
    #print(f'{vitamin}: {amount}')

    num_amount = amount.split(' ')[0]
    unit = amount.split(' ')[1]

    amount_needed = daily_intake[vitamin] - float(num_amount)

    if amount_needed > 0:
        print(f'You need {amount_needed} more {unit} of {vitamin} today')
    else:
        print(f'You took too much {vitamin} today.')
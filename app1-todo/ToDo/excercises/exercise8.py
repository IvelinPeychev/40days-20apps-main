while True:
    coin_result = input('Throw the coin and enter the result here: ') + '\n'

    with open('heads_result.txt', 'r') as file:
        result = file.readlines()

    result.append(coin_result)

    with open('heads_result.txt', 'w') as file:
        file.writelines(result)

    heads = result.count('head\n')
    percentage = (heads / len(result)) * 100
    print(f'Heads: {percentage}%')

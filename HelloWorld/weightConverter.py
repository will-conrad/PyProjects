weight = input("Enter weight: ")
if weight.lower().__contains__('kg'):
    weight = weight.removesuffix('kg')
    weight = int(weight) * 2.205
    weight *= 10
    weight = weight.__ceil__()
    weight /= 10
    print(f'You weigh {weight} pounds')
elif weight.lower().__contains__('lbs'):
    weight = weight.removesuffix('lbs')
    weight = int(weight) / 2.205
    weight *= 10
    weight = weight.__ceil__()
    weight /= 10
    print(f'You weigh {weight} kilos')


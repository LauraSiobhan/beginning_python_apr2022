for age in range(6):
    # these two lines do the same thing:
    age += 17
    age = age + 17

    if age >= 21:
        print(f'at {age} you can drink')
    elif age >= 18:
        print(f'at {age} you can vote, but not drink')
    else:
        print(f'at {age} you are a minor, no drinking, no voting')

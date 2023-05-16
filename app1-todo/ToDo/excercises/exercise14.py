def water_state(temperature):
    if temperature <=0:
        state = 'Solid'
    elif 0 < temperature <= 99:
        state = 'Liquid'
    else:
        state = 'Gas'

    return state


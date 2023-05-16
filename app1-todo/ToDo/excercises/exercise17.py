import PySimpleGUI as sg

sg.theme("Black")
text_row1 = sg.Text('Enter feet:')
field1 = sg.InputText(tooltip='Enter feet', key='feet')

text_row2 = sg.Text('Enter inches:')
field2 = sg.InputText(tooltip='Enter inches', key='inches')

convert_button = sg.Button('Convert')
exit_button = sg.Button('Exit')
# final_result = 0
result = sg.Text('', key='result')

window = sg.Window(title='Convertor',
                   layout=[[text_row1, field1],
                           [text_row2, field2],
                           [convert_button, exit_button, result]
                           ])

while True:
    event, value = window.read()
    print(event)
    print(value)
    try:
        match event:
            case 'Convert':
                foot_to_meter = float(value['feet']) * 0.3048
                inch_to_meter = float(value['inches']) * 0.0254
                final_result = float(foot_to_meter+inch_to_meter)
                window['result'].update(value=f'{"%.2f" % final_result} m')
            case 'Exit':
                break
            case sg.WIN_CLOSED:
                break
    except ValueError:
        sg.popup("Please provide two numbers", font=('Helvetica', 20))



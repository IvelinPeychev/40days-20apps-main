import PySimpleGUI as sg


row1_text = sg.Text("Enter feet")
row1_field = sg.InputText()

row2_text = sg.Text("Enter inches")
row2_field = sg.InputText()

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[row1_text, row1_field],
                                        [row2_text, row2_field],
                                        [button]])
window.read()
window.close()

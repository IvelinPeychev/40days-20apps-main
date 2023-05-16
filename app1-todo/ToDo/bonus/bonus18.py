import PySimpleGUI as sg
from zip_extracter_b18 import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")


label2 = sg.Text("Select destination dir: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")


window = sg.Window("Archive Extractor",
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [extract_button, output_label]
                        ])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    destination = values["folder"]
    extract_archive(archivepath, destination)
    window['output'].update(value='Extraction completed')
    window.close()


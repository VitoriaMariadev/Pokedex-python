import PySimpleGUI as sg

sg.theme('Default')

layout = [
    [sg.Text('Pokedex')],
    [sg.Button('Ver pokemons')]
]

janela = sg.Window('Menu Inicial', layout, element_justification='c')

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED: 
        break
    
janela.close()
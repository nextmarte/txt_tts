import os
import pyttsx3
import PySimpleGUI as sg

# Define o tema da interface gráfica
sg.theme('DarkBlue3')

# Define o layout da janela
layout = [
    [sg.Text('Selecione o arquivo de texto:', font=('Arial', 14))],
    [sg.Input(key='input_file'), sg.FileBrowse()],
    [sg.Text('Selecione o local para salvar o arquivo de áudio:', font=('Arial', 14))],
    [sg.Input(key='output_file'), sg.FileSaveAs()],
    [sg.Button('Converter para áudio', size=(20, 2))],
    [sg.Text('', size=(20, 2), font=('Arial', 10), key='status')]
]

# Cria a janela
window = sg.Window('Text to Speech', layout)

# Loop para processar os eventos da janela
while True:
    event, values = window.read()

    # Verifica se o usuário fechou a janela
    if event == sg.WIN_CLOSED:
        break

    # Verifica se o usuário clicou no botão "Converter para áudio"
    if event == 'Converter para áudio':

        # Obtém o nome do arquivo de entrada
        input_file = values['input_file']

        # Verifica se o arquivo de entrada foi selecionado
        if not input_file:
            sg.popup_error('Selecione um arquivo de texto para converter em áudio.')
            continue

        # Obtém o caminho do arquivo de saída
        output_file = values['output_file']

        # Verifica se o caminho do arquivo de saída foi selecionado
        if not output_file:
            sg.popup_error('Selecione o local para salvar o arquivo de áudio.')
            continue

        # Inicia o módulo de voz
        engine = pyttsx3.init()

        # Configura a voz em português
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) # voice[0] é a voz feminina em português

        # Define a velocidade
        engine.setProperty('rate', 250) # 200 é a velocidade normal, valores acima disso aumentam a velocidade

        # Abre o arquivo de texto
        with open(input_file, 'r', encoding='utf-8') as file:
            texto = file.read().replace('\n', '')

        # Gera o arquivo de áudio
        engine.save_to_file(texto, output_file)

        # Executa a conversão
        engine.runAndWait()

        # Exibe uma mensagem de conclusão
        sg.popup('Arquivo de áudio criado com sucesso!', title='Conversão concluída')

# Fecha a janela
window.close()

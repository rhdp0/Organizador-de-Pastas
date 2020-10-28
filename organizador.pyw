import os
import PySimpleGUI as sg

audios_ext = ['.mp3', '.wav', '.wma']
videos_ext = ['.mp4', '.mov', '.avi', '.wmv', '.flv', '.rmvb', '.mpeg', '.3gp', '.mkv']
imagem_ext = ['.jpg', '.jpeg', '.png', '.gif', '.exif', '.bmp', '.png', '.psd', '.webp']
docs_ext = ['.txt', '.pdf', '.docx', '.log', '.doc', '.xls', '.xlsx']
exe_ext = ['.exe']

sg.theme('BlueMono')
# Interface gráfica
layout = [  [sg.Text('Escolha o Diretório'), sg.FolderBrowse(key='diretorio')],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Output(size=(100,20))]
         ]

# Cria a janela
window = sg.Window('Organiza aí', layout) 

# Manipulação e organização daspastas e arquivos
def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]


def organizar(diretorio):
    AUDIOS_DIR = os.path.join(diretorio, "Audios")
    IMAGENS_DIR = os.path.join(diretorio, "Imagens")
    DOCS_DIR = os.path.join(diretorio, "Documentos")
    VIDEOS_DIR = os.path.join(diretorio, "Videos")
    EXE_DIR = os.path.join(diretorio, "Executáveis")
    OUTROS_DIR = os.path.join(diretorio, "Outros")

    if not os.path.isdir(AUDIOS_DIR):
        os.mkdir(AUDIOS_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(EXE_DIR):
        os.mkdir(EXE_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)

    nomes_arquivos = os.listdir(diretorio)

    nova_pasta = ''
    for arquivo in nomes_arquivos:
        try:
            if os.path.isfile(os.path.join(diretorio, arquivo)):
                extensao = str.lower(pegar_extensao(arquivo))
                if extensao in audios_ext:
                    nova_pasta = AUDIOS_DIR
                elif extensao in imagem_ext:
                    nova_pasta = IMAGENS_DIR
                elif extensao in videos_ext:
                    nova_pasta = VIDEOS_DIR
                elif extensao in docs_ext:
                    nova_pasta = DOCS_DIR
                elif extensao in exe_ext:
                    nova_pasta = EXE_DIR
                else:
                    nova_pasta = OUTROS_DIR

                #move o arquivo
                velho = os.path.join(diretorio, arquivo)
                novo = os.path.join(nova_pasta, arquivo)
                os.rename(velho, novo)
                print(f"Moveu: {velho} \nPara: {novo}")
        except:
            pass

if __name__ == '__main__':
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        diretorio_alvo = values['diretorio']
        if event == 'Ok':
            organizar(diretorio_alvo)   
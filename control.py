import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        # Janela
        self.janela = sg.Window('Dados  do Usuário').layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            
            print(f'Nome:{nome}')
            print(f'Idade:{idade}')
            

tela = TelaPython()
tela.Iniciar() 
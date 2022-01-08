from ntpath import join
import random
import string
from PyQt5 import uic, QtWidgets

class caracteres_all():
    def __init__(self):
        self.letras_maiusculas= string.ascii_uppercase
        self.letras_minusculas = string.ascii_lowercase
        self.numeros = '123456789'
        self.simbolos = '!@#$&%?~'
caracteres_all()

juntar = caracteres_all()

def gera_senha():
    Senha = ""
    quantidade = 0
    if (interface_piloto.check_maiuscula.isChecked()):
        max = juntar.letras_maiusculas 
        Senha += "".join(random.sample(max, 3))
        quantidade += 3
    
    if (interface_piloto.check_minuscula.isChecked()):
        min = juntar.letras_minusculas 
        Senha += "".join(random.sample(min, 2))
        quantidade += 2
    
    if (interface_piloto.check_numero.isChecked()):
        num = juntar.numeros
        Senha += "".join(random.sample(num, 2))
        quantidade += 2
    
    if (interface_piloto.check_simbolo.isChecked()):
        sin = juntar.simbolos
        Senha += "".join(random.sample(sin, 2))
        quantidade += 2
       
    fimSenha = ''.join(random.sample(Senha, quantidade))
    interface_piloto.label_senha.setText(str(fimSenha))
    

app = QtWidgets.QApplication([])
interface_piloto = uic.loadUi("gerador_senhas.ui")
interface_piloto.botao_gerar.clicked.connect(gera_senha)
interface_piloto.show()
app.exec()



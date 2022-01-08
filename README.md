## Programa que gera senhas 

* #### *Contexto da aplicação:*

*Programa que gera senhas Fortes aleatorias*

* #### *Mapa do código:*

2. **Bibliotecas Python/ Comandos**

```Python
from ntpath import join
import random
import string
from PyQt5 import uic, QtWidgets

#Caso não tenha as bibliotecas intale digitando no terminal
#A biblioteca OS já vem instalada por padrão no Python
pip install PyQt5
pip install glob
```

2. **Classe que define os valos das letras maisculas, minusculas, simbolos e números**
```Python
class caracteres_all():
    def __init__(self):
        self.letras_maiusculas= string.ascii_uppercase
        self.letras_minusculas = string.ascii_lowercase
        self.numeros = '123456789'
        self.simbolos = '!@#$&%?~'
caracteres_all()

juntar = caracteres_all()
```

3. **Função com estrutua de IFs para cada check box, no final imprime o resultado na tela do programa**
```Python
def gera_senha():
    Senha = "" #Inicia a senha em branco
    quantidade = 0 #Para quando tirar a opção de uma check box não da erro
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
```

4. **Inicia o programa**
```Python
app = QtWidgets.QApplication([])
interface_piloto = uic.loadUi("gerador_senhas.ui")
interface_piloto.botao_gerar.clicked.connect(gera_senha)
interface_piloto.show()
app.exec()
```

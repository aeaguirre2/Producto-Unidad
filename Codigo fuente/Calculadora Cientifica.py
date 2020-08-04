#Importacion de librerias
import RPi.GPIO as GPIO
import math
#Creacion de Clases
class Calculadora:

#No hubo necesidad de un constructor ya que no usamos el mismo atributo para demas funciones
 
  #MENU
  def menu(self):
      print("---------CALCULADORA CASIO---------")
      print("\nPIN #3) Sumar\t\t PIN #15) Tangente\t\t PIN #26) ArcCosenoHiperbolico")
      print("\nPIN #5) Restar\t\t PIN #16) ArcoSeno\t\t PIN #27) ArcTangenteHiperbolica")
      print("\nPIN #7) Multiplicar\t PIN #18) ArcoCoseno\t\t PIN #28) Logaritmo Natural")
      print("\nPIN #8) Dividir\t\t PIN #19) ArcoTangente\t\t PIN #29) Logaritmo Decimal")
      print("\nPIN #10) Radicacion\t PIN #21) SenoHiperbolico")
      print("\nPIN #11) Potenciacion\t PIN #22) CosenoHiperbolico")
      print("\nPIN #12) Seno\t\t PIN #23) TangenteHiperbolica")
      print("\nPIN #13) Coseno\t\t PIN #24) ArcSenoHiperbolico")
  
      #ORDEN PARA SELECCIONAR UN PIN
      selec=input("Marque la casilla del PIN a realizar ")
    
    #PINES A SELECCIONAR
      if GPIO.input(3):
            self.sumar()
      elif GPIO.input(5):
            self.restar()
      elif GPIO.input(7):
            self.multiplicar()
      elif GPIO.input(8):
            self.dividir()
      elif GPIO.input(10):
            self.raiz()
      elif GPIO.input(11):
            self.potencia()
      elif GPIO.input(12):
            self.seno()
      elif GPIO.input(13):
            self.coseno()
      elif GPIO.input(15):
            self.tangente()
      elif GPIO.input(16):
            self.ArcSen()
      elif GPIO.input(18):
            self.ArcCos()
      elif GPIO.input(19):
            self.ArcTan()
      elif GPIO.input(21):
            self.SenH()
      elif GPIO.input(22):
            self.CosH()
      elif GPIO.input(23):
            self.TanH()
      elif GPIO.input(24):
            self.ASenH()
      elif GPIO.input(26):
            self.ACosH()
      elif GPIO.input(27):
            self.ATanH()
      elif GPIO.input(28):
            self.LNatural()
      elif GPIO.input(29):
            self.LDecimal()
      else:
            print("No a marcado un PIN valido!")
            self.menu()
            
  #OPERACIONES DE NUESTRA CASIO
  def sumar(self):
        resultado=0
        print("Ingrese el primer numero")
        num1=int(input())
        print("Ingrese el segundo numero")
        num2=int(input())
        resultado=num1+num2
        print(num1,'+',num2,'=',resultado)
  def restar(self):
        resultado=0
        print("Ingrese el primer numero")
        num1=int(input())
        print("Ingrese el segundo numero")
        num2=int(input())
        resultado=num1-num2
        print(num1,'-',num2,'=',resultado)
  def multiplicar(self):
        print("Ingrese el primer numero")
        num1=int(input())
        print("Ingrese el segundo numero")
        num2=int(input())
        resultado=num1*num2
        print(num1,'*',num2,'=',resultado)
  def dividir(self):
        print("Ingrese el primer numero")
        num1=int(input())
        print("Ingrese el segundo numero")
        num2=int(input())
        resultado=num1/num2
        print(num1,'/',num2,'=',resultado)
  def raiz(self):
        print("Ingrese el indice de la raiz")
        ind=int(input())
        print("Ingrese el valor aplicar raiz")
        valor=float(input())
        resultado=valor**(1/ind)
        print("El resultado es: ",resultado)
  def potencia(self):
        print("Ingrese el valor a elevar")
        valor=int(input())
        print("Ingrese el exponente")
        exp=int(input())
        resultado=valor**exp
        print("El resultado es: ",resultado)
  def seno(self):
        print("Ingrese el angulo en RAD")
        sen=float(input())
        resultado=math.sin(sen)
        print("El Seno es: ",resultado)
  def coseno(self):
        print("Ingrese el angulo en RAD")
        cose=float(input())
        resultado=math.cos(cose)
        print("El Coseno es: ",resultado)
  def tangente(self):
        print("Ingrese el angulo en RAD")
        tange=float(input())
        resultado=math.tan(tange)
        print("La Tangente es: ",resultado)
  def arcSen(self):
        print("Ingrese el angulo en RAD")
        arcsen=float(input())
        resultado=math.asin(arcsen)
        print("El ArcSeno es: ",resultado)
  def arcCos(self):
        print("Ingrese el angulo en RAD")
        arccos=float(input())
        resultado=math.acos(arccos)
        print("El ArcCoseno es: ",resultado)
  def arcTan(self):
        print("Ingrese el angulo en RAD")
        arctan=float(input())
        resultado=math.atan(arctan)
        print("El ArcoTan es: ",resultado)
  def SenH(self):
        print("Ingrese el angulo en RAD")
        senh=float(input())
        resultado=math.sinh(senh)
        print("El Seno hiperbolico es: ",resultado)
  def CosH(self):
        print("Ingrese el angulo en RAD")
        coshi=float(input())
        resultado=math.cosh(coshi)
        print("El Coseno hiperbolico es: ",resultado)
  def TanH(self):
        print("Ingrese el angulo en RAD")
        tanhi=float(input())
        resultado=math.tanh(tanhi)
        print("La Tangente hiperbolica es: ",resultado)
  def ASenH(self):
        print("Ingrese el angulo en RAD")
        asenh=float(input())
        resultado=math.asinh(asenh)
        print("El ArcSen hiperbolico es: ",resultado)
  def ACosH(self):
        print("Ingrese el angulo en RAD")
        acoshi=float(input())
        resultado=math.acosh(acoshi)
        print("El ArcCos hiperbolico es: ",resultado)
  def ATanH(self):
        print("Ingrese el angulo en RAD")
        atanhi=float(input())
        resultado=math.atanh(atanhi)
        print("La ArcTan hiperbolica es: ",resultado)
  def LNatural(self):
        print("Ingrese el valor")
        valor=float(input())
        resultado=math.log(valor,math.e)
        print("El Logaritmo Natural es: ",resultado)
  def LDecimal(self):
        print("Ingrese el valor")
        valor=int(input())
        print("Ingrese el valor de Logaritmo")
        logarit=float(input())
        resultado=math.log(logarit,valor)
        print("El Logaritmo Decimal es: ",resultado)

#CREACION DE OBJETOS
calcu=Calculadora()
opcionMenu=calcu.menu()

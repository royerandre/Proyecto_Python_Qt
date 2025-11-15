import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load("interfaz.ui", None)
        self.ui.show()
        self.ui.calcular.clicked.connect(self.realizar_calculo)
        self.ui.predecir.clicked.connect(self.predecir_nota)

    def hay_formula_seleccionada(self):
        if self.ui.radio1.isChecked() or self.ui.radio2.isChecked() or self.ui.radio3.isChecked():
            return True
        return False

    def realizar_calculo(self):
        if not self.hay_formula_seleccionada():
            self.ui.txtResultado.setText("¡ERROR: Selecciona un formato!")
            self.ui.txtResultado.setStyleSheet("color: purple; font-weight: bold;")
            return

        try:
            n1 = float(self.ui.inputNota1.text())
            n2 = float(self.ui.inputNota2.text())
            n3 = float(self.ui.inputNota3.text())
            
            promedio = 0

            if self.ui.radio1.isChecked():
                promedio = (n1*1 + n2*2 + n3*2) / 5
            elif self.ui.radio2.isChecked():
                promedio = (n1*2 + n2*2 + n3*1) / 5
            elif self.ui.radio3.isChecked():
                promedio = (n1*1 + n2*2 + n3*3) / 6

            if promedio >= 13.5:
                mensaje = f"Nota final: {promedio:.2f} ¡Aprobaste! Felicidades"
                self.ui.txtResultado.setStyleSheet("color: green; font-weight: bold;")
            else:
                mensaje = f"Nota final: {promedio:.2f}. ¡Sigue esforzándote!"
                self.ui.txtResultado.setStyleSheet("color: red; font-weight: bold;")

            self.ui.txtResultado.setText(mensaje)

        except ValueError:
            self.ui.txtResultado.setText("Error: Faltan notas o hay letras")
            self.ui.txtResultado.setStyleSheet("color: orange;")

    def predecir_nota(self):
        if not self.hay_formula_seleccionada():
            self.ui.prediccion_1.setText("¡Elige formato!")
            self.ui.prediccion_1.setStyleSheet("color: purple; font-weight: bold;")
            return

        try:
            n1 = float(self.ui.inputNota1.text())
            n2 = float(self.ui.inputNota2.text())
            
            meta = 13.5
            necesaria = 0

            if self.ui.radio1.isChecked():   
                necesaria = (meta * 5 - n1 - 2*n2) / 2
            elif self.ui.radio2.isChecked(): 
                necesaria = (meta * 5 - 2*n1 - 2*n2) / 1
            elif self.ui.radio3.isChecked(): 
                necesaria = (meta * 6 - n1 - 2*n2) / 3

            if necesaria <= 0:
                self.ui.prediccion_1.setText("¡Ya aprobaste!")
                self.ui.prediccion_1.setStyleSheet("color: green; font-weight: bold;")
            elif necesaria > 20:
                self.ui.prediccion_1.setText(f"Imposible ({necesaria:.2f})")
                self.ui.prediccion_1.setStyleSheet("color: red; font-weight: bold;")
            else:
                self.ui.prediccion_1.setText(f"Necesitas: {necesaria:.2f}")
                self.ui.prediccion_1.setStyleSheet("color: blue; font-weight: bold;")

        except ValueError:
            self.ui.prediccion_1.setText("Faltan Nota 1 y 2")
            self.ui.prediccion_1.setStyleSheet("color: orange;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiApp()
    sys.exit(app.exec())
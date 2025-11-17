import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load("interfaz.ui", None)
        self.ui.show()
        
        # Conectamos con TUS nombres de botones
        self.ui.calcular.clicked.connect(self.realizar_calculo)
        self.ui.predecir.clicked.connect(self.predecir_nota)

    def hay_formula_seleccionada(self):
        # CORREGIDO: Buscamos "formula1", "formula2", "formula3"
        if self.ui.formula1.isChecked() or self.ui.formula2.isChecked() or self.ui.formula3.isChecked():
            return True
        return False

    def realizar_calculo(self):
        # 1. Portero (Usando la función corregida)
        if not self.hay_formula_seleccionada():
            self.ui.resultado.setText("¡ERROR: Selecciona un formato!")
            self.ui.resultado.setStyleSheet("color: purple; font-weight: bold;")
            return

        try:
            # CORREGIDO: Buscamos "nota1", "nota2", "nota3"
            n1 = float(self.ui.nota1.text())
            n2 = float(self.ui.nota2.text())
            n3 = float(self.ui.nota3.text())
            
            promedio = 0

            # CORREGIDO: Buscamos "formula1", "formula2", "formula3"
            if self.ui.formula1.isChecked():
                promedio = (n1*1 + n2*2 + n3*2) / 5
            elif self.ui.formula2.isChecked():
                promedio = (n1*2 + n2*2 + n3*1) / 5
            elif self.ui.formula3.isChecked():
                promedio = (n1*1 + n2*2 + n3*3) / 6

            if promedio >= 13.5:
                mensaje = f"Nota final: {promedio:.2f} ¡Aprobaste! Felicidades"
                self.ui.resultado.setStyleSheet("color: green; font-weight: bold;")
            else:
                mensaje = f"Nota final: {promedio:.2f}. ¡Sigue esforzándote!"
                self.ui.resultado.setStyleSheet("color: red; font-weight: bold;")

            # CORREGIDO: Buscamos "resultado"
            self.ui.resultado.setText(mensaje)

        except ValueError:
            self.ui.resultado.setText("Error: Faltan notas o hay letras")
            self.ui.resultado.setStyleSheet("color: orange;")

    def predecir_nota(self):
        if not self.hay_formula_seleccionada():
            # CORREGIDO: Buscamos "prediccion_1" (si así lo llamaste)
            self.ui.prediccion_1.setText("¡Elige formato!")
            self.ui.prediccion_1.setStyleSheet("color: purple; font-weight: bold;")
            return

        try:
            n1 = float(self.ui.nota1.text())
            n2 = float(self.ui.nota2.text())
            
            meta = 13.5
            necesaria = 0

            if self.ui.formula1.isChecked():   
                necesaria = (meta * 5 - n1 - 2*n2) / 2
            elif self.ui.formula2.isChecked(): 
                necesaria = (meta * 5 - 2*n1 - 2*n2) / 1
            elif self.ui.formula3.isChecked(): 
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
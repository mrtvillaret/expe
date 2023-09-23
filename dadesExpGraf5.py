#!/usr/bin/env python3
import subprocess
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QScrollArea

class ExpedientApp(QWidget):
    def __init__(self):
        super().__init__()

        # Crear els widgets
        label_gen_alumne = QLabel("Escriu alumne o alumna:")
        self.input_gen_alumne = QLineEdit("alumne")
        label_nom_alumne = QLabel("Escriu el nom de l'alumne:")
        self.input_nom_alumne = QLineEdit("Nom Cognom1 Cognom2")
        label_anys_alumne = QLabel("Escriu els anys de l'alumne: XX anys ")
        self.input_anys_alumne = QLineEdit("14 anys")
        label_curs_alumne = QLabel("Escriu el curs de l'alumne: 1r d'ESO o 1r de batxillerat... ")
        self.input_curs_alumne = QLineEdit("1r d'ESO")
        label_gen_instructor = QLabel("Escriu instructor o instructora:")
        self.input_gen_instructor = QLineEdit("instructora")
        label_nom_instructor = QLabel("Escriu el nom de l'instructor/a:")
        self.input_nom_instructor = QLineEdit("Nom Cognom1 Cognom2")
        label_nom_tutor = QLabel("Escriu el nom del tutor/a: (si s'escau)")
        self.input_nom_tutor = QLineEdit("NomTutor Cognom1 Cognom2")
        label_data = QLabel("Escriu la data (format: dia de mes de any, ex: 14 de març de 2023):")
        self.input_data = QLineEdit("14 de març de 2023")
        label_informacio = QLabel("ha tingut coneixement propi i per informació...(predefinit:de la Directora pedagògica d’ESO, del coordinador d´ESO... )")
        self.input_informacio = QTextEdit("de la Directora pedagògica d’ESO, del coordinador d´ESO, de la tutora i d’altres membres de la comunitat educativa")
        label_articles = QLabel("Fets que poden constituir una falta de les previstes (articles)")
        self.input_articles = QTextEdit(" a l’article 37.1 de la Llei 12/2009, del 10 de juliol, d’educació, i a l’article 76 a) i b) de les Normes de Funcionament i Organització del Centre")
        label_dies_prov = QLabel("la mesura provisional de .... ")
     #   self.input_dies_prov = QTextEdit("suspensió d’assistència a l’aula de 2 dies lectius i suspensió d’assistència al centre pel termini de 5 dies lectius \n suspensió d’assistència al centre pel termini de 3 dies lectius." )
        self.input_dies_prov = QTextEdit()
        self.input_dies_prov.setText("suspensió d’assistència a l’aula de 2 dies lectius i suspensió d’assistència al centre pel termini de 5 dies lectius \nsuspensió d’assistència al centre pel termini de 3 dies lectius.") #suspensió d’assistència a l’aula de 2 dies lectius i suspensió d’assistència al centre pel termini de 5 dies lectius \n suspensió d’assistència al centre pel termini de 3 dies lectius.
        label_dies_def = QLabel("la decisió d’aplicar una suspensió cautelar de... \ la sanció de... \ com a sanció la...\...")
        self.input_dies_def = QTextEdit("suspensió d’assistència a l’aula per un període de 2 dies lectius, que ja ha complert i \n suspensió d’assistència al centre per un període de 5 dies lectius")
        label_dataInici = QLabel("Escriu la data d'inici de la suspensió (format: dia de mes de any): ")
        self.input_dataInici = QLineEdit("18 de març de 2023")
        label_dataFinal = QLabel("Escriu la data de fi de la suspensió  (format: dia de mes de any): ")
        self.input_dataFinal = QLineEdit("20 de març de 2023")
        label_dataIniciExp = QLabel("Escriu la data d'inici de l'expedient  (format: dia de mes de any): ")
        self.input_dataIniciExp = QLineEdit("13 de març de 2023")
        label_fets = QLabel("Escriu els fets:")
        self.input_fets = QTextEdit()
        self.input_fets.setFixedHeight(300)




        self.button = QPushButton("Generar expedient")
        self.button.clicked.connect(self.generate_expedient)

        # Crear el layout i afegir els widgets
        layout = QVBoxLayout()
        layout.addWidget(label_gen_alumne)
        layout.addWidget(self.input_gen_alumne)
        layout.addWidget(label_nom_alumne)
        layout.addWidget(self.input_nom_alumne)
        layout.addWidget(label_anys_alumne)
        layout.addWidget(self.input_anys_alumne)
        layout.addWidget(label_curs_alumne)
        layout.addWidget(self.input_curs_alumne)
        layout.addWidget(label_gen_instructor)
        layout.addWidget(self.input_gen_instructor)
        layout.addWidget(label_nom_instructor)
        layout.addWidget(self.input_nom_instructor)
        layout.addWidget(label_nom_tutor)
        layout.addWidget(self.input_nom_tutor)
        layout.addWidget(label_data)
        layout.addWidget(self.input_data)
        layout.addWidget(label_informacio)
        layout.addWidget(self.input_informacio)
        layout.addWidget(label_articles)
        layout.addWidget(self.input_articles)
        layout.addWidget(label_dies_prov)
        layout.addWidget(self.input_dies_prov)
        layout.addWidget(label_dies_def)
        layout.addWidget(self.input_dies_def)
        layout.addWidget(label_dataInici)
        layout.addWidget(self.input_dataInici)
        layout.addWidget(label_dataFinal)
        layout.addWidget(self.input_dataFinal)
        layout.addWidget(label_dataIniciExp)
        layout.addWidget(self.input_dataIniciExp)
        layout.addWidget(label_fets)
        layout.addWidget(self.input_fets)

        layout.addWidget(self.button)

        # Crear el widget de desplaçament i establir el layout
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)
        scrollLayout = QVBoxLayout(scrollContent)
        scrollLayout.addLayout(layout)
        scroll.setWidget(scrollContent)

        # Establir el layout del widget principal
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(scroll)
        
    def replace_newline(self):
        text = self.input_fets.toPlainText()
        text = text.replace('\n', '\\'+' '+'\\linebreak\n')
        self.input_fets.setPlainText(text)

    def generate_expedient(self):
        # Obtenir les dades dels widgets
        gen_alumne = self.input_gen_alumne.text() or ""
        nom_alumne = self.input_nom_alumne.text() or ""
        anys_alumne = self.input_anys_alumne.text() or ""
        curs_alumne = self.input_curs_alumne.text() or ""
        gen_instructor = self.input_gen_instructor.text()
        nom_instructor = self.input_nom_instructor.text()
        nom_tutor = self.input_nom_tutor.text()
        data = self.input_data.text()
        informacio = self.input_informacio.toPlainText()
        articles = self.input_articles.toPlainText()
        dies_prov = self.input_dies_prov.toPlainText()
        dies_def = self.input_dies_def.toPlainText()
        dataInici = self.input_dataInici.text()
        dataFinal = self.input_dataFinal.text()
        dataIniciExp  = self.input_dataIniciExp.text()
        fets = self.input_fets.toPlainText()
        text = fets.replace('\n',  '\\'+'\\'+' '+'\linebreak\n') #'\\linebreak

        # Crear el contingut del fitxer de text amb les variables definides
        contingut = (f"\\newcommand{{\\genAlumne}}{{{gen_alumne}}}\n"
                     f"\\newcommand{{\\nomAlumne}}{{{nom_alumne}}}\n"
                     f"\\newcommand{{\\anysAlumne}}{{{anys_alumne}}}\n"
		     f"\\newcommand{{\\cursAlumne}}{{{curs_alumne}}}\n"
            	     f"\\newcommand{{\\nomInstructor}}{{{nom_instructor}}}\n"
            	     f"\\newcommand{{\\nomTutor}}{{{nom_tutor}}}\n"
	             f"\\newcommand{{\\data}}{{{data}}}\n"
           	     f"\\newcommand{{\\informacio}}{{{informacio}}}\n"
  	             f"\\newcommand{{\\fets}}{{{text}}}\n"
             	     f"\\newcommand{{\\articles}}{{{articles}}}\n"
             	     f"\\newcommand{{\\diesprov}}{{{dies_prov}}}\n"
             	     f"\\newcommand{{\\diesdef}}{{{dies_def}}}\n"
             	     f"\\newcommand{{\\dataInici}}{{{dataInici}}}\n"
              	     f"\\newcommand{{\\dataFinal}}{{{dataFinal}}}\n"
             	     f"\\newcommand{{\\dataIniciExp}}{{{dataIniciExp}}}")

        # Escriure el contingut al fitxer de text
        nom_fitxer = f"exp_{nom_alumne.replace(' ', '_')}_{data.replace(' ', '_')}.txt"
        print ("nomfitxer", nom_fitxer)
        with open("fitxer_de_text.tex", "w", encoding="UTF-8") as f:
            f.write(contingut)
        with open(nom_fitxer, "w", encoding="UTF-8") as f:
            f.write(contingut)
        # Compilar el fitxer LaTeX amb LuaLaTeX per obtenir un PDF
        if gen_instructor == "instructor":
       		subprocess.run(['lualatex', '-jobname=' + nom_fitxer[:-4], 'expedienT5instructor.tex'])
#        subprocess.run(['pandoc', '-s', '-o', nom_fitxer[:-4] + '.odt', 'expedienT5.tex'])
        elif gen_instructor == "instructora":
        		subprocess.run(['lualatex', '-jobname=' + nom_fitxer[:-4], 'expedienT5instructora.tex'])
#        subprocess.run(['pandoc', '-s', '-o', nom_fitxer[:-4] + '.odt', 'expedienT5.tex'])
        else:
        		subprocess.run(['lualatex', '-jobname=' + nom_fitxer[:-4], 'expedienT5.tex'])
#        subprocess.run(['pandoc', '-s', '-o', nom_fitxer[:-4] + '.odt', 'expedienT5.tex'])


if __name__ == "__main__":
    app = QApplication([])
    window = ExpedientApp()
    window.show()
    window.setMinimumWidth(1000)
#    window.showMaximized()  # Obre la finestra a pantalla sencera
    app.exec_()

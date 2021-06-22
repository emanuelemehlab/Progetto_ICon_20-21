import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap
import GeneralFunction as gf
import Graph as gr
import Bayes as ba
from PIL import Image
from pyswip import Prolog #usata per interrogare la kb
import re


class MainWindow(QDialog):



    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("InterfaceFolder\mainPage.ui",self)
        self.setWindowTitle("MainWindow")
        self.pushButtonBayes.clicked.connect(self.goBayesInterface)
        self.pushButtonBayes.setStyleSheet(open('CSSFolder\PushButtonMain.css').read())
        self.pushButtonGrafo.clicked.connect(self.goGraphInterface)
        self.pushButtonGrafo.setStyleSheet(open('CSSFolder\PushButtonMain.css').read())
        self.pushButtonKB.clicked.connect(self.goKbInterface)
        self.pushButtonKB.setStyleSheet(open('CSSFolder\PushButtonMain.css').read())



    def goGraphInterface(self):
        widget.setCurrentIndex(dictPosition["GraphFW"])

    #funzioni del main per BaYes e Kb
    def goBayesInterface(self):
        widget.setCurrentIndex(dictPosition["BayesFW"])
    
    def goKbInterface(selfself):
        widget.setCurrentIndex(dictPosition["KbFW"])



class GraphFW(QDialog):
    def __init__(self):
        super(GraphFW, self).__init__()
        loadUi("InterfaceFolder\GraphInterface.ui", self)
        self.pushButtonIndietro.clicked.connect(self.back)
        self.pushButtonIndietro.setStyleSheet(open('CSSFolder\PushButtonIndietro.css').read())
        self.pushButtonOk.clicked.connect(self.ok)
        self.pushButtonOk.setStyleSheet(open('CSSFolder\PushButtonOkSearch.css').read())
        self.pushButtonOk_2.clicked.connect(self.ok_2)
        self.pushButtonOk_2.setStyleSheet(open('CSSFolder\PushButtonOkSearch.css').read())
        self.pushButtonSearch.clicked.connect(self.search)
        self.pushButtonSearch.setStyleSheet(open('CSSFolder\PushButtonOkSearch.css').read())  #comboBoxCitta
        self.pushButtonCleanAll.clicked.connect(self.cleanAll)
        self.pushButtonCleanAll.setStyleSheet(open('CSSFolder\PushButtonCleanButton.css').read())
        self.pushButtonGoGraph.clicked.connect(self.goGraphImage)
        self.pushButtonGoGraph.setStyleSheet(open('CSSFolder\PushButtonOkSearch.css').read())
        self.comboBoxCitta.setStyleSheet(open('CSSFolder\ComboBox.css').read())
        self.comboBoxPartenza.setStyleSheet(open('CSSFolder\ComboBox.css').read())
        self.comboBoxArrivo.setStyleSheet(open('CSSFolder\ComboBox.css').read())


        city = gf.getCityName()
        i = 0
        while i < len(city):
            if city[i] == "mosca":
                i = i + 1
            else:
                self.comboBoxCitta.addItem(city[i])
                i = i + 1

        self.pushButtonSearch.setEnabled(False)
        self.pushButtonCleanAll.setEnabled(False)
        self.pushButtonOk_2.setEnabled(False)
        self.pushButtonGoGraph.setEnabled(False)

    def back(selfself): #funzione per tornare al main
        widget.setCurrentIndex(dictPosition["MainWindow"])

    def ok(self):
        j = 0
        i = 0
        self.pushButtonOk.setEnabled(False)
        self.pushButtonOk_2.setEnabled(True)
        self.pushButtonCleanAll.setEnabled(True)
        citySelected = self.comboBoxCitta.currentText()
        location = gf.getLocationName(citySelected)
        station = gf.getStationName(citySelected)

        while j < len(location):
            self.comboBoxPartenza.addItem(location[j])
            j = j + 1

        while i < len(station):
            self.comboBoxPartenza.addItem(station[i])
            i = i + 1

    def ok_2(self):
        j = 0
        i = 0
        self.pushButtonSearch.setEnabled(True)
        self.pushButtonOk_2.setEnabled(False)
        citySelected = self.comboBoxCitta.currentText()
        location = gf.getLocationName(citySelected)
        station = gf.getStationName(citySelected)

        while j < len(location):
            self.comboBoxArrivo.addItem(location[j])
            j = j + 1

        while i < len(station):
            self.comboBoxArrivo.addItem(station[i])
            i = i + 1


    def search(self):
        self.pushButtonGoGraph.setEnabled(True)
        start = self.comboBoxPartenza.currentText()
        arrival = self.comboBoxArrivo.currentText()
        city = self.comboBoxCitta.currentText()
        numKm, shortPath = gr.SearchPath(start, arrival, city)
        numKm = numKm / 10
        self.labelKmShow.setText(str(numKm)+" "+"KM")
        self.labelCamminoBreveShow.setText(str(shortPath))








    def cleanAll(self):
        self.comboBoxPartenza.clear()
        self.comboBoxArrivo.clear()
        self.labelCamminoBreveShow.clear()
        self.labelKmShow.clear()
        self.pushButtonSearch.setEnabled(False)
        self.pushButtonCleanAll.setEnabled(False)
        self.pushButtonOk_2.setEnabled(False)
        self.pushButtonOk.setEnabled(True)
        self.pushButtonGoGraph.setEnabled(False)


    def goGraphImage(self):
        city = self.comboBoxCitta.currentText()
        f = Image.open("CityMap\\" + city + ".png").show()
        #widget.setCurrentIndex(dictPosition["GraphSW"])


class BayesFW(QDialog):
    def __init__(self):
        super(BayesFW, self).__init__()
        loadUi("InterfaceFolder\Bayes1.ui", self)
        self.secondWindow = BayesSW()
        self.INDIETRO.setStyleSheet(open("CSSFolder\PushButtonIndietro.css").read())
        self.OK.setStyleSheet(open("CSSFolder\PushButtonIndietro.css").read())
        self.OK.clicked.connect(self.clickok)
        self.INDIETRO.clicked.connect(self.clickclose)
        #self.scrollArea.setStyleSheet(open("CSSFolder\ScrollArea.css").read())
        #self.frame.setStyleSheet(open("CSSFolder\Frame.css").read())

    def clickok(self):

        if self.radioButton_scienza_1.isChecked():
            scienza = 0
        elif self.radioButton_scienza_2.isChecked():
            scienza = 1
        elif self.radioButton_scienza_3.isChecked():
            scienza = 2
        else:
            scienza = 2

        if self.radioButton_relax_1.isChecked():
            relax = 0
        elif self.radioButton_relax_2.isChecked():
            relax = 1
        elif self.radioButton_relax_3.isChecked():
            relax = 2
        else:
            relax = 2

        if self.radioButton_avventura_1.isChecked():
            avventura = 0
        elif self.radioButton_avventura_2.isChecked():
            avventura = 1
        elif self.radioButton_avventura_3.isChecked():
            avventura = 2
        else:
            avventura = 2

        if self.radioButton_cultura_1.isChecked():
            cultura = 0
        elif self.radioButton_cultura_2.isChecked():
            cultura = 1
        elif self.radioButton_cultura_3.isChecked():
            cultura = 2
        else:
            cultura = 2

        if self.radioButton_religione_1.isChecked():
            religione = 0
        elif self.radioButton_religione_2.isChecked():
            religione = 1
        elif self.radioButton_religione_3.isChecked():
            religione = 2
        else:
            religione = 2

        if self.radioButton_sacri_1.isChecked():
            sacri = 0
        elif self.radioButton_sacri_2.isChecked():
            sacri = 1
        elif self.radioButton_sacri_3.isChecked():
            sacri = 2
        else:
            sacri = 2

        if self.radioButton_antica_1.isChecked():
            arte_antica = 0
        elif self.radioButton_antica_2.isChecked():
            arte_antica = 1
        elif self.radioButton_antica_3.isChecked():
            arte_antica = 2
        else:
            arte_antica = 2

        if self.radioButton_moderna_1.isChecked():
            arte_moderna = 0
        elif self.radioButton_moderna_2.isChecked():
            arte_moderna = 1
        elif self.radioButton_moderna_3.isChecked():
            arte_moderna = 2
        else:
            arte_moderna = 2

        if self.radioButton_musei_1.isChecked():
            musei = 0
        elif self.radioButton_musei_2.isChecked():
            musei = 1
        elif self.radioButton_musei_3.isChecked():
            musei = 2
        else:
            musei = 2

        if self.radioButton_natura_1.isChecked():
            natura = 0
        elif self.radioButton_natura_2.isChecked():
            natura = 1
        elif self.radioButton_natura_3.isChecked():
            natura = 2
        else:
            natura = 2

        if self.radioButton_panorami_1.isChecked():
            panorama = 0
        elif self.radioButton_panorami_2.isChecked():
            panorama = 1
        elif self.radioButton_panorami_3.isChecked():
            panorama = 2
        else:
            panorama = 2

        if self.radioButton_divertimento_1.isChecked():
            divertimento = 0
        elif self.radioButton_divertimento_2.isChecked():
            divertimento = 1
        elif self.radioButton_divertimento_3.isChecked():
            divertimento = 2
        else:
            divertimento = 2

        if self.radioButton_sport_1.isChecked():
            sport = 0
        elif self.radioButton_sport_2.isChecked():
            sport = 1
        elif self.radioButton_sport_3.isChecked():
            sport = 2
        else:
            sport = 2

        resultListOfList=list()
        pamsterdam = ba.pamsterdam(arte_antica, musei, panorama)
        #tAmsterdam=(pamsterdam,Am'sterdam')
        tAmsterdam = list()
        tAmsterdam.append(pamsterdam)
        tAmsterdam.append('Amsterdam')
        resultListOfList.append(tAmsterdam)
        pbuenosaires = ba.pbuenosaires(natura, sport, scienza)
        #tBuenos=(pbuenosaires,'Buenos')
        tBuenos=list()
        tBuenos.append(pbuenosaires)
        tBuenos.append('Buenos Aires')
        resultListOfList.append(tBuenos)
        pberlino = ba.pberino(arte_antica, arte_moderna, panorama)
        tBerlin=list()
        tBerlin.append(pberlino)
        tBerlin.append('Berlino')
        resultListOfList.append(tBerlin)
        plondra = ba.plondra(arte_antica, sport, panorama)
        tlondon = list()
        tlondon.append(plondra)
        tlondon.append('Londra')
        resultListOfList.append(tlondon)
        ptokyo = ba.ptokyo(arte_antica, religione, panorama)
        ttokyo = list()
        ttokyo.append(ptokyo)
        ttokyo.append('Tokyo')
        resultListOfList.append(ttokyo)
        pparigi = ba.pparigi(panorama, arte_antica, religione, musei)
        tparis = list()
        tparis.append(pparigi)
        tparis.append('Parigi')
        resultListOfList.append(tparis)
        pnewyork = ba.pnewyork(arte_moderna, musei, natura, panorama)
        tnewYork = list()
        tnewYork.append(pnewyork)
        tnewYork.append('New york')
        resultListOfList.append(tnewYork)
        pmosca = ba.pmosca(scienza, natura, sacri, arte_moderna)
        tmoska = list()
        tmoska.append(pmosca)
        tmoska.append('Mosca')
        resultListOfList.append(tmoska)
        pmadrid = ba.pmadrid(musei, sacri, arte_moderna, divertimento)
        tmadrid = list()
        tmadrid.append(pmadrid)
        tmadrid.append('Madrid')
        resultListOfList.append(tmadrid)
        pinstabul = ba.pinstabul(religione, arte_antica, scienza, panorama)
        tistanbull = list()
        tistanbull.append(pinstabul)
        tistanbull.append('Istanbul')
        resultListOfList.append(tistanbull)
        resultListOfList.sort()

        for value in resultListOfList: #stampa delle probabilità con relativi nomi
            number=round(float(value[0]),2) #arrotondamento della probabilità
            stringa="-  "+str(value[1])+"  ->  "+str(number) #value[0]=probabilità, value[1]=nome della città
            self.secondWindow.input1.append(stringa)
            self.secondWindow.input1.append("\n")

        self.secondWindow.show()


    def clickclose(self):
        widget.setCurrentIndex(dictPosition["MainWindow"])

class BayesSW(QDialog):
    def __init__(self):
        super(BayesSW, self).__init__()
        loadUi("InterfaceFolder\Bayes2.ui",self)
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.input1 = self.textEdit
        self.IND.setStyleSheet(open("CSSFolder\PushButtonIndietro.css").read())
        self.IND.clicked.connect(self.clickclose)

    def clickclose(self):
        self.close()

    def display(self):
        self.show()

class KbFW(QDialog):
    def __init__(self):
        super(KbFW, self).__init__()
        loadUi("InterfaceFolder\KBInterface.ui",self)
        self.pushButtonIndietro.clicked.connect(self.back)
        self.pushButtonIndietro.setStyleSheet(open("CSSFolder\PushButtonIndietro.css").read())
        self.comboBoxeEsempi.setStyleSheet(open("CSSFolder\ComboBox.css").read())
        self.pushButtonSearch.setStyleSheet(open("CSSFolder\PushButtonOkSearch.css").read())
        self.pushButtonCleanAll.setStyleSheet(open("CSSFolder\PushButtonCleanButton.css").read())
        self.lineEdit.setStyleSheet(open("CSSFolder\LineEdit.css").read())
        self.lineEdit_7.setStyleSheet(open("CSSFolder\LineEdit.css").read())
        self.lineEdit_2.setStyleSheet(open("CSSFolder\LineEdit.css").read())
        self.lineEdit_3.setStyleSheet(open("CSSFolder\LineEdit.css").read())
        self.lineEdit_4.setStyleSheet(open("CSSFolder\LineEdit.css").read())
        self.lineEdit_5.setStyleSheet(open("CSSFolder\LineEdit.css").read())
        self.lineEdit_6.setStyleSheet(open("CSSFolder\LineEdit.css").read())
        self.lineEdit.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.textEditRisultati.setStyleSheet(open("CSSFolder\TextEdit.css").read())
        self.pushButtonCleanAll.clicked.connect(self.cleanAll)
        self.textEditRisultati.append("     !!ATTENZIONE!!  ")
        self.textEditRisultati.append("Al momento non è possibile:")
        self.textEditRisultati.append("- Inserire piu di 4 variabili")
        self.textEditRisultati.append("- inserire giorni e ora come variabile")
        self.textEditRisultati.append("- inserire giorni e ora come variabile in isOpen()\n")
        self.textEditRisultati.append("Ci scusiamo per il disagio!!")

        i = 0
        while i < len(listQueryEx):
            self.comboBoxeEsempi.addItem(listQueryEx[i])
            i = i + 1
        self.pushButtonOk.clicked.connect(self.okPress)
        self.pushButtonOk.setStyleSheet(open("CSSFolder\PushButtonOkSearch.css").read())
        self.pushButtonSearch.clicked.connect(self.search)
        self.pushButtonSearch.setEnabled(False)
        self.pushButtonCleanAll.setEnabled(False)


    def back(self):
        widget.setCurrentIndex(dictPosition["MainWindow"])

    def okPress(self):
        query=self.comboBoxeEsempi.currentText()
        num=dictQueryEx[query]

        if num==1:
            self.lineEdit.setEnabled(True)
            self.labelArrow.setText("->")
        elif num==2:
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.labelArrow.setText("->")
            self.labelArrow_2.setText("->")
        elif num==3:
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.labelArrow.setText("->")
            self.labelArrow_2.setText("->")
            self.labelArrow_3.setText("->")
        elif num==4:
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.labelArrow.setText("->")
            self.labelArrow_2.setText("->")
            self.labelArrow_3.setText("->")
            self.labelArrow_4.setText("->")
        elif num==5:
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.labelArrow.setText("->")
            self.labelArrow_2.setText("->")
            self.labelArrow_3.setText("->")
            self.labelArrow_4.setText("->")
            self.labelArrow_5.setText("->")
        elif num==6:
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.labelArrow.setText("->")
            self.labelArrow_2.setText("->")
            self.labelArrow_3.setText("->")
            self.labelArrow_4.setText("->")
            self.labelArrow_5.setText("->")
            self.labelArrow_6.setText("->")
        elif num==7:
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.lineEdit_7.setEnabled(True)
            self.labelArrow.setText("->")
            self.labelArrow_2.setText("->")
            self.labelArrow_3.setText("->")
            self.labelArrow_4.setText("->")
            self.labelArrow_5.setText("->")
            self.labelArrow_6.setText("->")
            self.labelArrow_7.setText("->")

        lista = query.split("(")
        lista[0]=lista[0]+"("
        self.labelInserireQuery.setText(lista[0])
        self.labelInserireQuery_2.setText(")")
        self.pushButtonSearch.setEnabled(True)
        self.pushButtonCleanAll.setEnabled(True)



    def search(self):
        self.textEditRisultati.clear()
        prolog=Prolog()
        query = self.comboBoxeEsempi.currentText()
        num = dictQueryEx[query]
        #print(num)
        split=query.split("(")
        var = list()
        giorniSet=["lunedi","martedi","mercoledi","giovedi""venerdi","sabato","domenica"]

        string = str(dictMesiGiorni[str(split[0])])
        posMesiGiorni = string.split(",")


        if num == 1:
            var.append(self.lineEdit.text())
            if posMesiGiorni[1] != "n":
                giorno = str(var[int(posMesiGiorni[1])])
                if giorno in giorniSet:
                    var[int(posMesiGiorni[1])] = str(dictGiorni[giorno])
            query=str(split[0])+"("+str(var[0])+")"

        elif num == 2:
            var.append(self.lineEdit.text())
            var.append(self.lineEdit_2.text())
            if posMesiGiorni[1] != "n":
                giorno = str(var[int(posMesiGiorni[1])])
                if giorno in giorniSet:
                    var[int(posMesiGiorni[1])] = str(dictGiorni[giorno])
            query = str(split[0]) + "(" + str(var[0])+","+str(var[1]) + ")"

        elif num == 3:
            var.append(self.lineEdit.text())
            var.append(self.lineEdit_2.text())
            var.append(self.lineEdit_3.text())
            if posMesiGiorni[1] != "n":
                giorno = str(var[int(posMesiGiorni[1])])
                if giorno in giorniSet:
                    var[int(posMesiGiorni[1])] = str(dictGiorni[giorno])
                #var[int(posMesiGiorni[1])] = str(dictGiorni[giorno])
            query = str(split[0]) + "(" + str(var[0])+","+str(var[1])+","+str(var[2]) + ")"

        elif num == 4:
            var.append(self.lineEdit.text())
            var.append(self.lineEdit_2.text())
            var.append(self.lineEdit_3.text())
            var.append(self.lineEdit_4.text())
            if posMesiGiorni[1] != "n":
                giorno = str(var[int(posMesiGiorni[1])])
                if giorno in giorniSet:
                    var[int(posMesiGiorni[1])] = str(dictGiorni[giorno])
            query = str(split[0]) + "(" + str(var[0])+","+str(var[1])+","+str(var[2])+","+str(var[3]) + ")"
            print(var)

        elif num == 5:
            var.append(self.lineEdit.text())
            var.append(self.lineEdit_2.text())
            var.append(self.lineEdit_3.text())
            var.append(self.lineEdit_4.text())
            var.append(self.lineEdit_5.text())
            if posMesiGiorni[1] != "n":
                giorno = str(var[int(posMesiGiorni[1])])
                if giorno in giorniSet:
                    var[int(posMesiGiorni[1])] = str(dictGiorni[giorno])
            query = str(split[0]) + "(" + str(var[0])+","+str(var[1])+","+str(var[2])+","+str(var[3])+","+str(var[4]) + ")"

        elif num == 6:
            var.append(self.lineEdit.text())
            var.append(self.lineEdit_2.text())
            var.append(self.lineEdit_3.text())
            var.append(self.lineEdit_4.text())
            var.append(self.lineEdit_5.text())
            var.append(self.lineEdit_6.text())
            if posMesiGiorni[1] != "n":
                giorno = str(var[int(posMesiGiorni[1])])
                if giorno in giorniSet:
                    var[int(posMesiGiorni[1])] = str(dictGiorni[giorno])
            query = str(split[0]) + "(" + str(var[0])+","+str(var[1])+","+str(var[2])+","+str(var[3])+","+str(var[4])+","+str(var[5])+ ")"

        elif num == 7:
            var.append(self.lineEdit.text())
            var.append(self.lineEdit_2.text())
            var.append(self.lineEdit_3.text())
            var.append(self.lineEdit_4.text())
            var.append(self.lineEdit_5.text())
            var.append(self.lineEdit_6.text())
            var.append(self.lineEdit_7.text())
            if posMesiGiorni[1] != "n":
                giorno = str(var[int(posMesiGiorni[1])])
                if giorno in giorniSet:
                    var[int(posMesiGiorni[1])] = str(dictGiorni[giorno])
            query = str(split[0]) + "(" + str(var[0])+","+str(var[1])+","+str(var[2])+","+str(var[3])+","+str(var[4])+","+str(var[5])+","+str(var[6])+ ")"
        #print(query)

        flag=False
        index=0
        indexList=list()
        i=0
        while i < num:
            objUno = re.match(r'^[A-Z][a-z]*', var[i])
            objDue = re.match(r'^[A-Z]', var[i])

            if objDue != None:
                index=i
                indexList.append(i)
                flag = True
            elif objUno != None:
                index=i
                indexList.append(i)
                flag = True
            i = i + 1


        if (flag == False):
            q = prolog.query(query)
            try: #usato per print di True of False
                self.textEditRisultati.setText("  " + str(bool(dict(q))))
            except:
                self.textEditRisultati.setText("  " + str(bool(q)))
        else:

            '''
                        for valore in prolog.query(query):
                self.textEditRisultati.append("  "+valore[var[index]])
            '''
            if len(indexList)==1:
                for valore in prolog.query(query):
                    self.textEditRisultati.append("1- " + valore[var[indexList[0]]])

            elif len(indexList)==2:

                for valore in prolog.query(query):
                    self.textEditRisultati.append("1- " + valore[var[indexList[0]]])
                    self.textEditRisultati.append("2- " + valore[var[indexList[1]]])
                    self.textEditRisultati.append("_____________________")

                #for valore in prolog.query(query):
                    #self.textEditRisultati.append("  " + valore[var[indexList[0]]])
            elif len(indexList)==3:
                for valore in prolog.query(query):
                    self.textEditRisultati.append("1- " + valore[var[indexList[0]]])
                    self.textEditRisultati.append("2- " + valore[var[indexList[1]]])
                    self.textEditRisultati.append("3- " + valore[var[indexList[2]]])
                    self.textEditRisultati.append("_____________________")

            elif len(indexList)==4:
                for valore in prolog.query(query):
                    self.textEditRisultati.append("1- " + valore[var[indexList[0]]])
                    self.textEditRisultati.append("2- " + valore[var[indexList[1]]])
                    self.textEditRisultati.append("3- " + valore[var[indexList[2]]])
                    self.textEditRisultati.append("4- " + valore[var[indexList[3]]])
                    self.textEditRisultati.append("_____________________")




    def cleanAll(self):
        #self.lineEditQuery.clear()
        self.textEditRisultati.clear()
        self.pushButtonSearch.setEnabled(False)
        self.pushButtonCleanAll.setEnabled(False)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.labelArrow.clear()
        self.labelArrow_2.clear()
        self.labelArrow_3.clear()
        self.labelArrow_4.clear()
        self.labelArrow_5.clear()
        self.labelArrow_6.clear()
        self.labelArrow_7.clear()
        self.labelInserireQuery.clear()
        self.labelInserireQuery_2.clear()






#dizionario che possiede come chiavi i nomi delle classi e come ogg i relativi indici nello stack
listQueryEx=["e_nel_continente(Citta',Continente).","boreale(Continente).","australe(Continente).","mese_estivo_boreale(Mese).",
           "mese_primaverile_boreale(Mese).","mese_autunnale_boreale(Mese).","mese_invernale_boreale(Mese).","mese_estivo_australe(Mese).",
           "mese_primaverile_australe(Mese).","mese_autunnale_australe(Mese).","mese_invernale_australe(Mese).","estate(City , Mese , Giorno).",
           "autunno(City , Mese , Giorno).","primavera(City , Mese , Giorno).","inverno(City , Mese , Giorno).","estate_boreale(Continente ,Mese, Giorno).",
           "primavera_boreale(Continente , Mese , Giorno).","autunno_boreale(Continente , Mese , Giorno).","inverno_boreale(Continente , Mese , Giorno).",
           "estate_australe(Continente  ,Mese, Giorno).","primavera_australe(Continente , Mese , Giorno).","autunno_australe(Continente , Mese , Giorno).",
           "inverno_australe(Continente , Mese , Giorno).","station(Citta', Nome, Nodo).","city(Citta' , Continente, Nazione, Fuso_Orario ).",
           "currency(Citta' , Valuta).","showplace(Citta' , Posto , Categoria_Posto , Apertura , Orari , Costo ,Nodo).",
           "is_open(Citta,Posto,Giorno,Ora)."]

dictQueryEx={"e_nel_continente(Citta',Continente).":2,"boreale(Continente).":1,"australe(Continente).":1,"mese_estivo_boreale(Mese).":1,
           "mese_primaverile_boreale(Mese).":1,"mese_autunnale_boreale(Mese).":1,"mese_invernale_boreale(Mese).":1,"mese_estivo_australe(Mese).":1,
           "mese_primaverile_australe(Mese).":1,"mese_autunnale_australe(Mese).":1,"mese_invernale_australe(Mese).":1,"estate(City , Mese , Giorno).":3,
           "autunno(City , Mese , Giorno).":3,"primavera(City , Mese , Giorno)":3,"inverno(City , Mese , Giorno).":3,"estate_boreale(Continente ,Mese, Giorno).":3,
           "primavera_boreale(Continente , Mese , Giorno).":3,"autunno_boreale(Continente , Mese , Giorno).":3,"inverno_boreale(Continente , Mese , Giorno).":3,
           "estate_australe(Continente  ,Mese, Giorno).":3,"primavera_australe(Continente , Mese , Giorno).":3,"autunno_australe(Continente , Mese , Giorno).":3,
           "inverno_australe(Continente , Mese , Giorno).":3,"station(Citta', Nome, Nodo).":3,"city(Citta' , Continente, Nazione, Fuso_Orario ).":4,
           "currency(Citta' , Valuta).":2,"showplace(Citta' , Posto , Categoria_Posto , Apertura , Orari , Costo ,Nodo).":7,
           "is_open(Citta,Posto,Giorno,Ora).":4}

dictMesiGiorni={"e_nel_continente":"n,n","boreale":"n,n","australe":"n,n","mese_estivo_boreale":"0,n",
           "mese_primaverile_boreale":"0,n","mese_autunnale_boreale":"0,n","mese_invernale_boreale":"0,n","mese_estivo_australe":"0,n",
           "mese_primaverile_australe":"0,n","mese_autunnale_australe":"0,n","mese_invernale_australe":"0,n","estate":"1,2",
           "autunno":"1,2","primavera":"1,2","inverno":"1,2","estate_boreale":"1,2",
           "primavera_boreale":"1,2","autunno_boreale":"1,2","inverno_boreale":"1,2",
           "estate_australe":"1,2","primavera_australe":"1,2","autunno_australe":"1,2",
           "inverno_australe":"1,2","station":"n,n","city":"n,n",
           "currency":"n,n","showplace":"n,n",
           "is_open":"n,2"}


dictGiorni={"lunedi":1,"martedi":2,"mercoledi":3,"giovedi":4,"venerdi":5,"sabato":6,"domenica":7}



dictPosition ={"MainWindow":0,"GraphFW":1,"BayesFW":3,"BayesSW":4,"KbFW":2}
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
main=MainWindow()
graphFW=GraphFW()
#graphSW=GraphSW()
#variabili per bayes e kb-----
bayesFW=BayesFW()
bayesSW=BayesSW()
kbFW=KbFW()
widget.addWidget(main)
widget.addWidget(graphFW)
#widget.addWidget(graphSW)
#aggiunta allo stack-----
widget.addWidget(kbFW)
widget.addWidget(bayesFW)
widget.addWidget(bayesSW)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()



try:
    sys.exit(app.exec_())
except:
    print("Null")

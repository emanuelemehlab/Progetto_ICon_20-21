# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bayes1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination




def pamsterdam(arte_antica, musei, panorama):
    if (arte_antica != 2) and (musei != 2) and (panorama != 2):
         return infer.query(['Amsterdam'], evidence={'Arte_antica': arte_antica, 'Panorama': panorama, 'Musei': musei}).values[0]
    elif (arte_antica == 2) and (musei == 2) and (panorama == 2):
         return infer.query(['Amsterdam']).values[0]
    elif (arte_antica == 2) and (musei == 2):
         return infer.query(['Amsterdam'], evidence={'Panorama': panorama}).values[0]
    elif (arte_antica == 2) and (panorama == 2):
        return infer.query(['Amsterdam'], evidence={'Musei': musei}).values[0]
    elif (musei == 2) and (panorama == 2):
        return infer.query(['Amsterdam'], evidence={'Arte_antica': arte_antica}).values[0]
    elif arte_antica == 2:
        return infer.query(['Amsterdam'], evidence={'Panorama': panorama, 'Musei': musei}).values[0]
    elif musei == 2:
        return infer.query(['Amsterdam'], evidence={'Arte_antica': arte_antica, 'Panorama': panorama}).values[0]
    elif panorama == 2:
        return infer.query(['Amsterdam'], evidence={'Arte_antica': arte_antica, 'Musei': musei}).values[0]

def pbuenosaires(natura, sport, scienze):
    if (natura != 2) and (scienze != 2) and (sport != 2):
         return infer.query(['BuenosAires'], evidence={'Natura': natura, 'Sport': sport, 'Scienza': scienze}).values[0]
    elif (natura == 2) and (scienze == 2) and (sport == 2):
         return infer.query(['BuenosAires']).values[0]
    elif (natura == 2) and (scienze == 2):
         return infer.query(['BuenosAires'], evidence={'Sport': sport}).values[0]
    elif (natura == 2) and (sport == 2):
        return infer.query(['BuenosAires'], evidence={'Scienza': scienze}).values[0]
    elif (scienze == 2) and (sport == 2):
        return infer.query(['BuenosAires'], evidence={'Natura': natura}).values[0]
    elif natura == 2:
        return infer.query(['BuenosAires'], evidence={'Sport': sport, 'Scienza': scienze}).values[0]
    elif scienze == 2:
        return infer.query(['BuenosAires'], evidence={'Natura': natura, 'Sport': sport}).values[0]
    elif sport == 2:
        return infer.query(['BuenosAires'], evidence={'Natura': natura, 'Scienza': scienze}).values[0]

def pberino(arte_antica, arte_moderna, panorama):
    if (panorama != 2) and (arte_moderna != 2) and (arte_antica != 2):
         return infer.query(['Berlino'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica, 'Arte_moderna': arte_moderna}).values[0]
    elif (panorama == 2) and (arte_moderna == 2) and (arte_antica == 2):
         return infer.query(['Berlino']).values[0]
    elif (panorama == 2) and (arte_moderna == 2):
         return infer.query(['Berlino'], evidence={'Arte_antica': arte_antica}).values[0]
    elif (panorama == 2) and (arte_antica == 2):
        return infer.query(['Berlino'], evidence={'Arte_moderna': arte_moderna}).values[0]
    elif (arte_moderna == 2) and (arte_antica == 2):
        return infer.query(['Berlino'], evidence={'Panorama': panorama}).values[0]
    elif panorama == 2:
        return infer.query(['Berlino'], evidence={'Arte_antica': arte_antica, 'Arte_moderna': arte_moderna}).values[0]
    elif arte_moderna == 2:
        return infer.query(['Berlino'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica}).values[0]
    elif arte_antica == 2:
        return infer.query(['Berlino'], evidence={'Panorama': panorama, 'Arte_moderna': arte_moderna}).values[0]

def plondra(arte_antica, sport, panorama):
    if (panorama != 2) and (sport != 2) and (arte_antica != 2):
         return infer.query(['Londra'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica, 'Sport': sport}).values[0]
    elif (panorama == 2) and (sport == 2) and (arte_antica == 2):
         return infer.query(['Londra']).values[0]
    elif (panorama == 2) and (sport == 2):
         return infer.query(['Londra'], evidence={'Arte_antica': arte_antica}).values[0]
    elif (panorama == 2) and (arte_antica == 2):
        return infer.query(['Londra'], evidence={'Sport': sport}).values[0]
    elif (sport == 2) and (arte_antica == 2):
        return infer.query(['Londra'], evidence={'Panorama': panorama}).values[0]
    elif panorama == 2:
        return infer.query(['Londra'], evidence={'Arte_antica': arte_antica, 'Sport': sport}).values[0]
    elif sport == 2:
        return infer.query(['Londra'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica}).values[0]
    elif arte_antica == 2:
        return infer.query(['Londra'], evidence={'Panorama': panorama, 'Sport': sport}).values[0]

def ptokyo(arte_antica, religione, panorama):
    if (panorama != 2) and (religione != 2) and (arte_antica != 2):
         return infer.query(['Tokyo'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica, 'Religione': religione}).values[0]
    elif (panorama == 2) and (religione == 2) and (arte_antica == 2):
         return infer.query(['Tokyo']).values[0]
    elif (panorama == 2) and (religione == 2):
         return infer.query(['Tokyo'], evidence={'Arte_antica': arte_antica}).values[0]
    elif (panorama == 2) and (arte_antica == 2):
        return infer.query(['Tokyo'], evidence={'Religione': religione}).values[0]
    elif (religione == 2) and (arte_antica == 2):
        return infer.query(['Tokyo'], evidence={'Panorama': panorama}).values[0]
    elif panorama == 2:
        return infer.query(['Tokyo'], evidence={'Arte_antica': arte_antica, 'Religione': religione}).values[0]
    elif religione == 2:
        return infer.query(['Tokyo'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica}).values[0]
    elif arte_antica == 2:
        return infer.query(['Tokyo'], evidence={'Panorama': panorama, 'Religione': religione}).values[0]

def pparigi(panorama, divertimento, sport, musei):

    if (panorama != 2) and (divertimento != 2) and (sport != 2) and (musei != 2):
         return infer.query(['Parigi'], evidence={'Panorama': panorama, 'Divertimento': divertimento, 'Sport': sport, 'Musei': musei}).values[0]
    elif (panorama == 2) and (sport == 2) and (divertimento == 2) and (musei == 2):
         return infer.query(['Parigi']).values[0]
    elif (panorama == 2) and (sport == 2) and (musei == 2):
         return infer.query(['Parigi'], evidence={'Divertimento': divertimento}).values[0]
    elif (panorama == 2) and (divertimento == 2) and (musei == 2):
        return infer.query(['Parigi'], evidence={'Sport': sport}).values[0]
    elif (panorama == 2) and (sport == 2) and (divertimento == 2):
        return infer.query(['Parigi'], evidence={'Musei': musei}).values[0]
    elif (musei == 2) and (sport == 2) and (divertimento == 2):
        return infer.query(['Parigi'], evidence={'Panorama': panorama}).values[0]
    elif (panorama == 2) and (divertimento == 2):
        return infer.query(['Parigi'], evidence={'Sport': sport, 'Musei': musei}).values[0]
    elif (panorama == 2) and (sport == 2):
        return infer.query(['Parigi'], evidence={'Divertimento': divertimento, 'Musei': musei}).values[0]
    elif (panorama == 2) and (musei == 2):
        return infer.query(['Parigi'], evidence={'Divertimento': divertimento, 'Sport': sport}).values[0]
    elif (musei == 2) and (sport == 2):
        return infer.query(['Parigi'], evidence={'Panorama': panorama, 'Divertimento': divertimento}).values[0]
    elif (divertimento == 2) and (sport == 2):
        return infer.query(['Parigi'], evidence={'Panorama': panorama, 'Musei': musei}).values[0]
    elif (divertimento == 2) and (musei == 2):
        return infer.query(['Parigi'], evidence={'Panorama': panorama, 'Sport': sport}).values[0]
    elif divertimento == 2:
        return infer.query(['Parigi'], evidence={'Panorama': panorama, 'Sport': sport, 'Musei': musei}).values[0]
    elif sport == 2:
        return infer.query(['Parigi'], evidence={'Panorama': panorama, 'Divertimento': divertimento,'Musei': musei}).values[0]
    elif panorama == 2:
        return infer.query(['Parigi'], evidence={'Divertimento': divertimento, 'Sport': sport, 'Musei': musei}).values[0]
    elif musei == 2:
        return infer.query(['Parigi'], evidence={'Panorama': panorama, 'Divertimento': divertimento, 'Sport': sport}).values[0]

def pinstabul(religione, arte_antica, scienza, panorama):
    if (panorama != 2) and (arte_antica != 2) and (religione != 2) and (scienza != 2):
         return infer.query(['Istanbul'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica, 'Religione': religione, 'Scienza': scienza}).values[0]
    elif (panorama == 2) and (religione == 2) and (arte_antica == 2) and (scienza == 2):
         return infer.query(['Istanbul']).values[0]
    elif (panorama == 2) and (religione == 2) and (scienza == 2):
         return infer.query(['Istanbul'], evidence={'Arte_antica': arte_antica}).values[0]
    elif (panorama == 2) and (arte_antica == 2) and (scienza == 2):
        return infer.query(['Istanbul'], evidence={'Religione': religione}).values[0]
    elif (panorama == 2) and (religione == 2) and (arte_antica == 2):
        return infer.query(['Istanbul'], evidence={'Scienza': scienza}).values[0]
    elif (scienza == 2) and (religione == 2) and (arte_antica == 2):
        return infer.query(['Istanbul'], evidence={'Panorama': panorama}).values[0]
    elif (panorama == 2) and (arte_antica == 2):
        return infer.query(['Istanbul'], evidence={'Religione': religione, 'Scienza': scienza}).values[0]
    elif (panorama == 2) and (religione == 2):
        return infer.query(['Istanbul'], evidence={'Arte_antica': arte_antica, 'Scienza': scienza}).values[0]
    elif (panorama == 2) and (scienza == 2):
        return infer.query(['Istanbul'], evidence={'Arte_antica': arte_antica, 'Religione': religione}).values[0]
    elif (scienza == 2) and (religione == 2):
        return infer.query(['Istanbul'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica}).values[0]
    elif (arte_antica == 2) and (religione == 2):
        return infer.query(['Istanbul'], evidence={'Panorama': panorama, 'Scienza': scienza}).values[0]
    elif (arte_antica == 2) and (scienza == 2):
        return infer.query(['Istanbul'], evidence={'Panorama': panorama, 'Religione': religione}).values[0]
    elif arte_antica == 2:
        return infer.query(['Istanbul'], evidence={'Panorama': panorama, 'Religione': religione, 'Scienza': scienza}).values[0]
    elif religione == 2:
        return infer.query(['Istanbul'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica, 'Scienza': scienza}).values[0]
    elif panorama == 2:
        return infer.query(['Istanbul'], evidence={'Arte_antica': arte_antica, 'Religione': religione, 'Scienza': scienza}).values[0]
    elif scienza == 2:
        return infer.query(['Istanbul'], evidence={'Panorama': panorama, 'Arte_antica': arte_antica, 'Religione': religione}).values[0]

def pmosca(scienza, natura, cattedrali, arte_moderna):
    if (natura != 2) and (arte_moderna != 2) and (cattedrali != 2) and (scienza != 2):
        return infer.query(['Mosca'], evidence={'Scienza': scienza, 'Natura': natura, 'Cattedrali': cattedrali, 'Arte_moderna': arte_moderna}).values[0]
    elif (natura == 2) and (cattedrali == 2) and (arte_moderna == 2) and (scienza == 2):
         return infer.query(['Mosca']).values[0]
    elif (natura == 2) and (cattedrali == 2) and (scienza == 2):
         return infer.query(['Mosca'], evidence={'Arte_moderna': arte_moderna}).values[0]
    elif (natura == 2) and (arte_moderna == 2) and (scienza == 2):
        return infer.query(['Mosca'], evidence={'Cattedrali': cattedrali}).values[0]
    elif (natura == 2) and (cattedrali == 2) and (arte_moderna == 2):
        return infer.query(['Mosca'], evidence={'Scienza': scienza}).values[0]
    elif (scienza == 2) and (cattedrali == 2) and (arte_moderna == 2):
        return infer.query(['Mosca'], evidence={'Natura': natura}).values[0]
    elif (natura == 2) and (arte_moderna == 2):
        return infer.query(['Mosca'], evidence={'Cattedrali': cattedrali, 'Scienza': scienza}).values[0]
    elif (natura == 2) and (cattedrali == 2):
        return infer.query(['Mosca'], evidence={'Arte_moderna': arte_moderna, 'Scienza': scienza}).values[0]
    elif (natura == 2) and (scienza == 2):
        return infer.query(['Mosca'], evidence={'Arte_moderna': arte_moderna, 'Cattedrali': cattedrali}).values[0]
    elif (scienza == 2) and (cattedrali == 2):
        return infer.query(['Mosca'], evidence={'Natura': natura, 'Arte_moderna': arte_moderna}).values[0]
    elif (arte_moderna == 2) and (cattedrali == 2):
        return infer.query(['Mosca'], evidence={'Natura': natura, 'Scienza': scienza}).values[0]
    elif (arte_moderna == 2) and (scienza == 2):
        return infer.query(['Mosca'], evidence={'Natura': natura, 'Cattedrali': cattedrali}).values[0]
    elif arte_moderna == 2:
        return infer.query(['Mosca'], evidence={'Natura': natura, 'Cattedrali': cattedrali, 'Scienza': scienza}).values[0]
    elif cattedrali == 2:
        return infer.query(['Mosca'], evidence={'Natura': natura, 'Arte_moderna': arte_moderna, 'Scienza': scienza}).values[0]
    elif natura == 2:
        return infer.query(['Mosca'], evidence={'Arte_moderna': arte_moderna, 'Cattedrali': cattedrali, 'Scienza': scienza}).values[0]
    elif scienza == 2:
        return infer.query(['Mosca'], evidence={'Natura': natura,'Arte_moderna': arte_moderna, 'Cattedrali': cattedrali}).values[0]

def pmadrid(musei, cattedrali, arte_moderna, divertimento):

    if (musei != 2) and (arte_moderna != 2) and (cattedrali != 2) and (divertimento != 2):
        return infer.query(['Madrid'], evidence={'Musei': musei, 'Cattedrali': cattedrali, 'Arte_moderna': arte_moderna,
                                                 'Divertimento': divertimento
                                                 }).values[0]
    elif (musei == 2) and (cattedrali == 2) and (arte_moderna == 2) and (divertimento == 2):
         return infer.query(['Madrid']).values[0]
    elif (musei == 2) and (cattedrali == 2) and (divertimento == 2):
         return infer.query(['Madrid'], evidence={'Arte_moderna': arte_moderna}).values[0]
    elif (musei == 2) and (arte_moderna == 2) and (divertimento == 2):
        return infer.query(['Madrid'], evidence={'Cattedrali': cattedrali}).values[0]
    elif (musei == 2) and (cattedrali == 2) and (arte_moderna == 2):
        return infer.query(['Madrid'], evidence={'Divertimento': divertimento}).values[0]
    elif (divertimento == 2) and (cattedrali == 2) and (arte_moderna == 2):
        return infer.query(['Madrid'], evidence={'Musei': musei}).values[0]
    elif (musei == 2) and (arte_moderna == 2):
        return infer.query(['Madrid'], evidence={'Cattedrali': cattedrali, 'Divertimento': divertimento}).values[0]
    elif (musei == 2) and (cattedrali == 2):
        return infer.query(['Madrid'], evidence={'Arte_moderna': arte_moderna, 'Divertimento': divertimento}).values[0]
    elif (musei == 2) and (divertimento == 2):
        return infer.query(['Madrid'], evidence={'Arte_moderna': arte_moderna, 'Cattedrali': cattedrali}).values[0]
    elif (divertimento == 2) and (cattedrali == 2):
        return infer.query(['Madrid'], evidence={'Musei': musei, 'Arte_moderna': arte_moderna}).values[0]
    elif (arte_moderna == 2) and (cattedrali == 2):
        return infer.query(['Madrid'], evidence={'Musei': musei, 'Divertimento': divertimento}).values[0]
    elif (arte_moderna == 2) and (divertimento == 2):
        return infer.query(['Madrid'], evidence={'Musei': musei, 'Cattedrali': cattedrali}).values[0]
    elif arte_moderna == 2:
        return infer.query(['Madrid'], evidence={'Musei': musei, 'Cattedrali': cattedrali, 'Divertimento': divertimento}).values[0]
    elif cattedrali == 2:
        return infer.query(['Madrid'], evidence={'Musei': musei, 'Arte_moderna': arte_moderna, 'Divertimento': divertimento}).values[0]
    elif musei == 2:
        return infer.query(['Madrid'], evidence={'Arte_moderna': arte_moderna, 'Cattedrali': cattedrali, 'Divertimento': divertimento}).values[0]
    elif divertimento == 2:
        return infer.query(['Madrid'], evidence={'Musei': musei, 'Arte_moderna': arte_moderna, 'Cattedrali': cattedrali}).values[0]

def pnewyork(arte_moderna, musei, natura, panorama):

    if (musei != 2) and (arte_moderna != 2) and (natura != 2) and (panorama != 2):
        return infer.query(['NewYork'], evidence={'Arte_moderna': arte_moderna, 'Musei': musei, 'Natura': natura,
                                                  'Panorama': panorama}).values[0]
    elif (musei == 2) and (natura == 2) and (arte_moderna == 2) and (panorama == 2):
         return infer.query(['NewYork']).values[0]
    elif (musei == 2) and (natura == 2) and (panorama == 2):
         return infer.query(['NewYork'], evidence={'Arte_moderna': arte_moderna}).values[0]
    elif (musei == 2) and (arte_moderna == 2) and (panorama == 2):
        return infer.query(['NewYork'], evidence={'Natura': natura}).values[0]
    elif (musei == 2) and (natura == 2) and (arte_moderna == 2):
        return infer.query(['NewYork'], evidence={'Panorama': panorama}).values[0]
    elif (panorama == 2) and (natura == 2) and (arte_moderna == 2):
        return infer.query(['NewYork'], evidence={'Musei': musei}).values[0]
    elif (musei == 2) and (arte_moderna == 2):
        return infer.query(['NewYork'], evidence={'Natura': natura, 'Panorama': panorama}).values[0]
    elif (musei == 2) and (natura == 2):
        return infer.query(['NewYork'], evidence={'Arte_moderna': arte_moderna, 'Panorama': panorama}).values[0]
    elif (musei == 2) and (panorama == 2):
        return infer.query(['NewYork'], evidence={'Arte_moderna': arte_moderna, 'Natura': natura}).values[0]
    elif (panorama == 2) and (natura == 2):
        return infer.query(['NewYork'], evidence={'Musei': musei, 'Arte_moderna': arte_moderna}).values[0]
    elif (arte_moderna == 2) and (natura == 2):
        return infer.query(['NewYork'], evidence={'Musei': musei, 'Panorama': panorama}).values[0]
    elif (arte_moderna == 2) and (panorama == 2):
        return infer.query(['NewYork'], evidence={'Musei': musei, 'Natura': natura}).values[0]
    elif arte_moderna == 2:
        return infer.query(['NewYork'], evidence={'Musei': musei, 'Natura': natura, 'Panorama': panorama}).values[0]
    elif natura == 2:
        return infer.query(['NewYork'], evidence={'Musei': musei, 'Arte_moderna': arte_moderna, 'Panorama': panorama}).values[0]
    elif musei == 2:
        return infer.query(['NewYork'], evidence={'Arte_moderna': arte_moderna, 'Natura': natura, 'Panorama': panorama}).values[0]
    elif panorama == 2:
        return infer.query(['NewYork'], evidence={'Musei': musei, 'Arte_moderna': arte_moderna, 'Natura': natura}).values[0]



# dichiarazione del modello
model = BayesianModel([('Cultura', 'Religione'), ('Cultura', 'Arte_antica'), ('Cultura', 'Arte_moderna'),
                       ('Cultura', 'Musei'), ('Relax', 'Natura'), ('Relax', 'Panorama'), ('Relax', 'Divertimento'),
                       ('Avventura', 'Divertimento'), ('Avventura', 'Sport'), ('Cultura', 'Cattedrali'),
                       ('Arte_antica', 'Amsterdam'), ('Musei', 'Amsterdam'), ('Panorama', 'Amsterdam'),
                       ('Arte_antica', 'SanPaolo'), ('Musei', 'SanPaolo'), ('Divertimento', 'SanPaolo'),
                       ('Natura', 'BuenosAires'), ('Scienza', 'BuenosAires'), ('Sport', 'BuenosAires'),
                       ('Panorama', 'Berlino'), ('Arte_antica', 'Berlino'), ('Arte_moderna', 'Berlino'),
                       ('Arte_antica', 'Londra'), ('Panorama', 'Londra'), ('Sport', 'Londra'),
                       ('Panorama', 'Parigi'), ('Divertimento', 'Parigi'), ('Sport', 'Parigi'), ('Musei', 'Parigi'),
                       ('Religione', 'Istanbul'), ('Arte_antica', 'Istanbul'), ('Scienza', 'Istanbul'),
                       ('Panorama', 'Istanbul'),
                       ('Scienza', 'Mosca'), ('Natura', 'Mosca'), ('Cattedrali', 'Mosca'), ('Arte_moderna', 'Mosca'),
                       ('Musei', 'Madrid'), ('Cattedrali', 'Madrid'), ('Arte_moderna', 'Madrid'),
                       ('Divertimento', 'Madrid'),
                       ('Arte_moderna', 'NewYork'), ('Musei', 'NewYork'), ('Natura', 'NewYork'),
                       ('Panorama', 'NewYork'),
                       ('Panorama', 'Tokyo'), ('Arte_antica', 'Tokyo'), ('Religione', 'Tokyo')])

# variabili genitori
cpd_Scienza = TabularCPD(variable='Scienza', variable_card=2, values=[[0.6], [0.4]])
cpd_Relax = TabularCPD(variable='Relax', variable_card=2, values=[[0.85], [0.15]])
cpd_Avventura = TabularCPD(variable='Avventura', variable_card=2, values=[[0.65], [0.35]])
cpd_Cultura = TabularCPD(variable='Cultura', variable_card=2, values=[[0.8], [0.2]])

# variabili intermedie
cpd_Religione = TabularCPD(variable='Religione', variable_card=2, values=[[0.8, 0.4],
                                                                          [0.2, 0.6]],
                           evidence=['Cultura'],
                           evidence_card=[2])
cpd_Cattedrali = TabularCPD(variable='Cattedrali', variable_card=2, values=[[0.6, 0.7],
                                                                            [0.4, 0.3]],
                            evidence=['Cultura'],
                            evidence_card=[2])
cpd_Arte_antica = TabularCPD(variable='Arte_antica', variable_card=2, values=[[0.95, 0.1],
                                                                              [0.05, 0.9]],
                             evidence=['Cultura'],
                             evidence_card=[2])
cpd_Arte_moderna = TabularCPD(variable='Arte_moderna', variable_card=2, values=[[0.85, 0.2],
                                                                                [0.15, 0.8]],
                              evidence=['Cultura'],
                              evidence_card=[2])
cpd_Musei = TabularCPD(variable='Musei', variable_card=2, values=[[0.8, 0.4],
                                                                  [0.2, 0.6]],
                       evidence=['Cultura'],
                       evidence_card=[2])
cpd_Natura = TabularCPD(variable='Natura', variable_card=2, values=[[0.80, 0.4],
                                                                    [0.20, 0.6]],
                        evidence=['Relax'],
                        evidence_card=[2])
cpd_Panorama = TabularCPD(variable='Panorama', variable_card=2, values=[[0.7, 0.5],
                                                                        [0.3, 0.5]],
                          evidence=['Relax'],
                          evidence_card=[2])
cpd_Divertimento = TabularCPD(variable='Divertimento', variable_card=2, values=[[0.75, 0.3, 0.9, 0.2],
                                                                                [0.25, 0.7, 0.1, 0.8]],
                              evidence=['Relax', 'Avventura'],
                              evidence_card=[2, 2])
cpd_Sport = TabularCPD(variable='Sport', variable_card=2, values=[[0.95, 0.7],
                                                                  [0.05, 0.3]],
                       evidence=['Avventura'],
                       evidence_card=[2])
# città
cpd_Amsterdam = TabularCPD(variable='Amsterdam', variable_card=2,
                           values=[[0.99, 0.82, 0.78, 0.53, 0.55, 0.33, 0.28, 0.01],
                                   [0.01, 0.18, 0.22, 0.47, 0.45, 0.67, 0.72, 0.99]],
                           evidence=['Arte_antica', 'Panorama', 'Musei'],
                           evidence_card=[2, 2, 2])
cpd_SanPaolo = TabularCPD(variable='SanPaolo', variable_card=2,
                          values=[[0.99, 0.84, 0.62, 0.23, 0.81, 0.44, 0.18, 0.01],
                                  [0.01, 0.16, 0.38, 0.77, 0.19, 0.56, 0.82, 0.99]],
                          evidence=['Musei', 'Divertimento', 'Arte_antica'],
                          evidence_card=[2, 2, 2])
cpd_BuenosAires = TabularCPD(variable='BuenosAires', variable_card=2,
                             values=[[0.99, 0.96, 0.95, 0.85, 0.32, 0.04, 0.02, 0.01],
                                     [0.01, 0.04, 0.05, 0.15, 0.68, 0.96, 0.98, 0.99]],
                             evidence=['Natura', 'Sport', 'Scienza'],
                             evidence_card=[2, 2, 2])
cpd_Berlino = TabularCPD(variable='Berlino', variable_card=2, values=[[0.99, 0.92, 0.41, 0.19, 0.94, 0.61, 0.1, 0.01],
                                                                      [0.01, 0.08, 0.59, 0.81, 0.06, 0.39, 0.9, 0.99]],
                         evidence=['Panorama', 'Arte_antica', 'Arte_moderna'],
                         evidence_card=[2, 2, 2])
cpd_Londra = TabularCPD(variable='Londra', variable_card=2, values=[[0.99, 0.77, 0.61, 0.31, 0.69, 0.2, 0.12, 0.01],
                                                                    [0.01, 0.23, 0.39, 0.69, 0.31, 0.8, 0.88, 0.99]],
                        evidence=['Arte_antica', 'Panorama', 'Sport'],
                        evidence_card=[2, 2, 2])
cpd_Tokyo = TabularCPD(variable='Tokyo', variable_card=2, values=[[0.99, 0.75, 0.83, 0.42, 0.87, 0.5, 0.33, 0.01],
                                                                  [0.01, 0.25, 0.17, 0.58, 0.13, 0.5, 0.67, 0.99]],
                       evidence=['Panorama', 'Arte_antica', 'Religione'],
                       evidence_card=[2, 2, 2])
cpd_Parigi = TabularCPD(variable='Parigi', variable_card=2, values=[
    [0.99, 0.52, 0.9, 0.46, 0.91, 0.47, 0.61, 0.2, 0.76, 0.19, 0.54, 0.06, 0.4, 0.04, 0.47, 0.01],
    [0.01, 0.48, 0.1, 0.54, 0.09, 0.53, 0.39, 0.8, 0.24, 0.81, 0.46, 0.94, 0.6, 0.96, 0.53, 0.99]],
                        evidence=['Panorama', 'Divertimento', 'Sport', 'Musei'],
                        evidence_card=[2, 2, 2, 2])

cpd_Istanbul = TabularCPD(variable='Istanbul', variable_card=2, values=[
    [0.99, 0.84, 0.97, 0.69, 0.94, 0.65, 0.73, 0.52, 0.41, 0.12, 0.23, 0.06, 0.2, 0.03, 0.09, 0.01],
    [0.01, 0.16, 0.03, 0.31, 0.06, 0.35, 0.27, 0.48, 0.59, 0.88, 0.77, 0.94, 0.8, 0.97, 0.91, 0.99]],
                          evidence=['Religione', 'Arte_antica', 'Scienza', 'Panorama'],
                          evidence_card=[2, 2, 2, 2])

cpd_Mosca = TabularCPD(variable='Mosca', variable_card=2, values=[
    [0.99, 0.63, 0.79, 0.22, 0.91, 0.42, 0.57, 0.12, 0.93, 0.39, 0.61, 0.09, 0.83, 0.26, 0.43, 0.01],
    [0.01, 0.37, 0.21, 0.78, 0.09, 0.58, 0.43, 0.88, 0.07, 0.61, 0.39, 0.91, 0.17, 0.74, 0.57, 0.99]],
                       evidence=['Scienza', 'Natura', 'Cattedrali', 'Arte_moderna'],
                       evidence_card=[2, 2, 2, 2])

cpd_Madrid = TabularCPD(variable='Madrid', variable_card=2, values=[
    [0.99, 0.96, 0.92, 0.8, 0.9, 0.79, 0.81, 0.5, 0.51, 0.39, 0.43, 0.1, 0.23, 0.13, 0.08, 0.01],
    [0.01, 0.04, 0.08, 0.2, 0.1, 0.21, 0.19, 0.5, 0.49, 0.61, 0.57, 0.9, 0.77, 0.87, 0.92, 0.99]],
                        evidence=['Musei', 'Cattedrali', 'Arte_moderna', 'Divertimento'],
                        evidence_card=[2, 2, 2, 2])
cpd_NewYork = TabularCPD(variable='NewYork', variable_card=2, values=[
    [0.99, 0.41, 0.83, 0.22, 0.94, 0.36, 0.73, 0.15, 0.9, 0.29, 0.69, 0.09, 0.78, 0.19, 0.59, 0.01],
    [0.01, 0.59, 0.17, 0.78, 0.06, 0.64, 0.27, 0.85, 0.1, 0.71, 0.31, 0.91, 0.22, 0.81, 0.41, 0.99]],
                         evidence=['Arte_moderna', 'Musei', 'Natura', 'Panorama'],
                         evidence_card=[2, 2, 2, 2])

model.add_cpds(cpd_Scienza, cpd_Relax, cpd_Avventura, cpd_Cultura, cpd_Religione, cpd_Cattedrali, cpd_Arte_antica,
               cpd_Arte_moderna, cpd_Musei, cpd_Natura, cpd_Panorama,
               cpd_Divertimento, cpd_Sport, cpd_Tokyo, cpd_NewYork, cpd_Madrid, cpd_Mosca, cpd_Parigi, cpd_Istanbul,
               cpd_Londra, cpd_Berlino, cpd_BuenosAires, cpd_SanPaolo, cpd_Amsterdam)

infer = VariableElimination(model)  #calcolo della prob di new tork sapendo le seguenti evidenze usando  il metodo di eliminazione delle variabili


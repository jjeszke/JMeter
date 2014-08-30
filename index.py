# coding=utf-8
__author__ = 'Jakub.Jeszke'

import cherrypy
import time
import math
import random
from datetime import timedelta, date
PI = 3.14
IP= "D001000"

class jmeter(object):

    @cherrypy.expose
    def index(self):
        return """<b>To jest prosta aplikacji, dzięki której nauczysz się podstaw JMetera.</b> <br><br> Zadanie na dzisiaj
            składa się z 4 requestów, które musisz przetestować, ich nazwy to "obwod", "pole, "data" i "numer-4". <br> Aby zobaczyć
            krótką dokumentację dotyczącą każdego z requestów, wykonanaj go bez podania argumentu, na przykład
            "{}:8080/obwod". <br> Pierwsze dwa requesty ("obwod" i "pole") to requesty typu GET. W celu zaznajomienia się
            z ich dokumentacją, wykonaj je z poziomu paska adresu jakiejkolwiek przeglądarki. <br> Trzeci i czwarty
            request ("data" i "numer-4") to requesty typu POST. Z wykorzystaniem odpowiednich dodatków je również możesz
            wykonać z poziomu przeglądarki, ale proszę Cię abyś wykorzystał do tego samego JMetera. <br><br>
            Celem dzisiejszego workshopu jest przetestowanie czasu odpowiedzi, kodu statusu HTML oraz samej odpowiedzi
            wszystkcih czterech requestów.<br><br><b>POWODZENIA</b>""".format(IP)

    @cherrypy.expose
    def przyklad(self, argument = None):
        try:
            if argument is None:
                return """To jest przykladowy request GET, podaj cokolwiek jako argument. Nazwa argumentu to... "argument" ;)"""
            else:
                return "Prawidłowo podałeś argument"
        except:
            return "ZLE!"

    @cherrypy.expose
    def obwod(self, radius = None):
        """
        Zadanie numer 1 - prosty get z jednym argumentem, uczestnik musi zweryfikowac czas requesta oraz zawartosc odpowiedzi.
        """
        try:
            if radius is None:
                return """<b>Request GET, numer 1.</b><br> Nazwa argumentu, którą trzeba podać do obliczenia pola koła jest "radius" i jego wartość musi on być większa od 0.
                <br><br>Na początek spróbuj w pasku adresu przeglądarki wpisać dane requestu wraz z argumentem, niedługo później powinieneś zobaczyć odpowiedź.
                <br><br>Przykładowy request:<b> http://{}:8080/obwod?radius=5 </b>
                <br> Odpowiedź:<b> Obwod wynosi: 31.4 </b>
                <br><br>Teraz czas podany request przetestować z wykorzystaniem JMetera - pamiętaj by przygotować asercję sprawdzającą odpowiedź (czy jest zgodna z przykładem).
                """.format(IP)
            if float(radius) > 0:
                return "Obwod wynosi: {}".format(str(2*PI*float(radius)))
            else:
                return "Na pewno zrobiles wszystko dobrze?"
        except:
            return "ZLE!"

    @cherrypy.expose
    def pole(self, promien = None):
        """
        Zadanie numer 2 - celowo dodany zostal time.sleep(5), tak by czas requestow byl zbyt dlugi.
        """
        try:
            if promien is None:
                return """<b>Request GET, numer 2.</b><br><br> Nazwa argumentu, którą trzeba podać do obliczenia pola koła jest "promien" i jego wartość musi on być większa od 0.
                <br><br>Przykładowa odpowiedź:<b> Pole wynosi: 12.56 </b>
                <br><br>Tak jak przy poprzednim zadaniu, przetestuj ten request z wykorzystaniem JMetera (pamiętaj o wszystkich asercjach)!"""
            if float(promien) > 0:
                time.sleep(5)
                return "Pole wynosi: {}".format(str(PI*math.pow(float(promien),2)))
            else:
                return "Na pewno zrobiles wszystko dobrze?"
        except:
            return "ZLE!"

    @cherrypy.expose()
    @cherrypy.tools.allow(methods=['POST'])
    def data(self, dni = None):
        """
        Zadanie numer 3 - time.sleep z randomem, celowy błąd w odpowiedzi (powinno to zostać dostrzeżone przez asercje w JMeterze).
        Doddatkowo w zadaniu trzeba wykorzystać HTTP Cookie Managera w JMeterze.
        """
        try:
            if dni is None:
                return """ Request POST, numer 3. Request zwraca datę dzisiejszą powiększoną o ilości dni podaną w argumencie.
                Nazwa tego argumentu to po prostu "dni" i przyjmuje wartości całkowite większe od 0.
                Dodatkowo musisz dodać ciasteczko o nazwie "test" i wartości "workshop".
                Odpowiedź powinna zostać zwrócona w formacie: YYYY-MM-DD (na przykład: 2014-09-15)
                Tak jak przy poprzednich zadaniach, przetestuj ten request z wykorzystaniem JMetera (pamiętaj o wszystkich asercjach)
                """
            if int(dni) > 0 and str(cherrypy.request.cookie.get('test').value) == "workshop":
                time.sleep(random.choice([0,1,2,3,4]))
                return str(date.today() + timedelta(days = int(dni) + 1))
            else:
                return "Na pewno zrobiles wszystko dobrze?"
        except:
            return "ZLE!"

cherrypy.quickstart(jmeter())
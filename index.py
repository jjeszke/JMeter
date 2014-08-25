# coding=utf-8
__author__ = 'Jakub.Jeszke'

import cherrypy
import time
import math
import random
from datetime import timedelta, date
PI = 3.14

class jmeter(object):
    @cherrypy.expose
    def index(self):
        return """<b>To jest prosta aplikacji, dzięki której nauczysz się podstaw JMetera.</b> <br><br> Pierwsze zadanie składa się z 4 requestów,  \
               które musisz przetestować ("obwod", "pole, "numer-3" i "numer-4").
               <br> Aby zobaczyć krótką dokumentację dotyczącą każdego z requestów, wykonanaj go bez podania argumentu na przykład "ip:8080/obwod"
               <br> Trzeci i czwarty request to POSTy, więc aby poznać treść dokumentacji powinieneś skorzystać z samego JMetera (oczywiście da się
               wykonać request POST z poziomu przeglądarki, ale celem zadania jest wykonanie go z poziomu Jmetera).
               <br><br><b>POWODZENIA</b>"""

    @cherrypy.expose
    def obwod(self, radius = None):
        """
        Zadanie numer 1 - prosty get z jednym argumentem, uczestnik musi zweryfikowac czas requesta oraz zawartosc odpowiedzi.
        """
        try:
            if radius is None:
                return """<B> To jest pierwsze zadanie workshopu o JMeterze.
                """
            if float(radius) > 0:
                return "Obwod wynosi: {}".format(str(2*PI*float(radius)))
            else:
                return "Na pewno zrobiles wszystko dobrze?"
        except:
            return "ZLE!"

    @cherrypy.expose
    def pole(self, promien = None):
        """
        Zadanie numer 2 - celowo dodany zostal time.sleep(10), tak by czas requestow byl zbyt dlugi.
        """
        try:
            if promien is None:
                return """<B> To jest pierwsze zadanie workshopu o JMeterze. </b><br>Ponizej znajdziesz szczegolowe informacje. <br>POWODZENIA!"""
            if float(promien) > 0:
                time.sleep(10)
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
        """
        try:
            if dni is None:
                return """<B> Trzecie zadanie: Prawidłowy format daty: 2014-09-01"""
            if int(dni) > 0:
                time.sleep(random.choice([1,2,3,7,8,9]))
                return str(date.today() + timedelta(days = int(dni)+10))
            else:
                return "Na pewno zrobiles wszystko dobrze?"
        except:
            return "ZLE!"

cherrypy.quickstart(jmeter())
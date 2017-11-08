# Kormákur Atli Unnþórsson
# 31.10.2017
# Skilaverkefni 10

from bottle import *
from sanitize import sanitize
import pymysql

#static files route
@route("/static/<filename>")
def staticFile(filename):
    return static_file(filename, root="./static/")

@route("/")
def index():        
    return template("index.tpl")
@post("/results")
def index():
    if request.forms.get("fastanr"):
        leitarnr = sanitize(request.forms.get("fastanr")).upper()
        connection = pymysql.connect(host='tsuts.tskoli.is',
                                     port=3306,
                                     user='1604002850',
                                     passwd='mypassword',
                                     db='1604002850_vef2verk11')
        with connection.cursor() as cursor:
            sql = "SELECT skraningarnumer, Tegund, verksmidjunumer, skraningardagur, co2, þyngd, skodun, stada FROM bilar WHERE skraningarnumer = '"+leitarnr+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                fastanr = result[0]
                tegund = result[1]
                verksmidjunr = result[2]
                skraningardagur = result[3]
                co2 = result[4]
                thyngd = result[5]
                skodun = result[6]
                stada = result[7]
                if str(result[0]) == str(leitarnr):
                    return template("info.tpl", a = fastanr,
                                                b = tegund,
                                                c = verksmidjunr,
                                                d = skraningardagur,
                                                e = co2,
                                                f = thyngd,
                                                g = skodun,
                                                h = stada)
            else:
                return template("popup.tpl",text="Bíll ekki til")
        connection.close()
    return template("index.tpl")
"""
@get("/nyskraningarsida")
def nyskraningarsida():
    return  template("nyskraning.tpl")

@post("/nyskraning")
def nyskraning():
    connection = pymysql.connect(host='tsuts.tskoli.is',
                             port=3306,
                             user='1604002850',
                             passwd='mypassword',
                             db='1604002850_vef2verk10')

    
    with connection.cursor() as cursor:
        sql = "SELECT user, pass FROM user WHERE user = '"+username+"'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            uttak = "Notandi er nú þegar til"
        else:
            sql = "INSERT INTO user (user, pass) VALUES ('"+username+"', '"+password+"')"
            cursor.execute(sql)
            connection.commit()
            uttak = "Notandi hefur verið stofnaður!"
    connection.close()
    return template("indexAfterSignup.tpl",uttak=uttak)
"""
@get("/innskraning")
def innskraning():
    return  template("innskraning.tpl")
@post("/check")
def check():
    connection = pymysql.connect(host='tsuts.tskoli.is',
                             port=3306,
                             user='1604002850',
                             passwd='mypassword',
                             db='1604002850_vef2verk10')
    username = sanitize(request.forms.get("username"))
    password = str(sanitize(request.forms.get("password")))
    with connection.cursor() as cursor:
        sql = "SELECT pass FROM user WHERE user = '"+username+"'"            
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            if str(result[0]) == str(password):
                response.set_cookie("account",username, secret=password)
                return template("leynisida.tpl",username=username)
            else:
                uttak = "Rangt lykilorð"
        else:
            uttak = "Notandinn er ekki til"
    connection.close()                
    if uttak == "Rangt lykilorð":
        return template("indexAfterSignup.tpl",uttak=uttak)
    elif uttak == "Notandinn er ekki til":
        return template("indexAfterSignup.tpl",uttak=uttak)

@route('/changeCar', method=['GET', 'POST'], name='/changeCar')
def index():
    connection = pymysql.connect(host='tsuts.tskoli.is',
                                     port=3306,
                                     user='1604002850',
                                     passwd='mypassword',
                                     db='1604002850_vef2verk11')
    if request.forms.get("skodun") or request.forms.get("tegund") or request.forms.get("verksmidjunumer") or request.forms.get("skraningardagur") or request.forms.get("co2") or request.forms.get("thyngd") or request.forms.get("skodun") or request.forms.get("stada") or request.forms.get("skraningarnumer"):
        with connection.cursor() as cursor:
            sql = "SELECT skraningarnumer, Tegund, verksmidjunumer, skraningardagur, co2, þyngd, skodun, stada FROM bilar WHERE skraningarnumer = '"+request.forms.get("fastanr")+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                fastanr = result[0]
                tegund = result[1]
                verksmidjunr = result[2]
                skraningardagur = result[3]
                co2 = result[4]
                thyngd = result[5]
                skodun = result[6]
                stada = result[7]
        fastanrNytt = sanitize(request.forms.get("fastanr"))
        tegundNytt = sanitize(request.forms.get("tegund"))
        verksmidjunrNytt = sanitize(request.forms.get("verksmidjunr"))
        skraningardagurNytt = sanitize(request.forms.get("skraningardagur"))
        co2Nytt = sanitize(request.forms.get("co2"))
        thyngdNytt = sanitize(request.forms.get("thyngd"))
        skodunNytt = sanitize(request.forms.get("skodun"))
        stadaNytt = sanitize(request.forms.get("stada"))
        listi = [fastanrNytt,tegundNytt,verksmidjunrNytt,skraningardagurNytt,co2Nytt,thyngdNytt,skodunNytt,stadaNytt]
        listiOG = [fastanr,tegund,verksmidjunr,skraningardagur,co2,thyngd,skodun,stada]
        for i in range(len(listi)):
            if not listi[i]:
                listi[i] = listiOG[i]
        print(fastanrNytt)
        print(tegundNytt)
        print(fastanr)
        print(tegund)
        with connection.cursor() as cursor:
            sql = "UPDATE bilar SET skraningarnumer = '"+str(fastanr)+"', Tegund = '"+str(tegund)+"', verksmidjunumer = '"+str(verksmidjunr)+"', skraningardagur = '"+str(skraningardagur)+"', co2 = "+str(co2)+", þyngd = "+str(thyngd)+", skodun = '"+str(skodun)+"', stada = '"+str(stada)+"' WHERE skraningarnumer = '"+str(fastanr)+"'"
            cursor.execute(sql)
    elif request.forms.get("fastanr"):
        leitarnr = sanitize(request.forms.get("fastanr")).upper()
        connection = pymysql.connect(host='tsuts.tskoli.is',
                                     port=3306,
                                     user='1604002850',
                                     passwd='mypassword',
                                     db='1604002850_vef2verk11')
        with connection.cursor() as cursor:
            sql = "SELECT skraningarnumer, Tegund, verksmidjunumer, skraningardagur, co2, þyngd, skodun, stada FROM bilar WHERE skraningarnumer = '"+leitarnr+"'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                fastanr = result[0]
                tegund = result[1]
                verksmidjunr = result[2]
                skraningardagur = result[3]
                co2 = result[4]
                thyngd = result[5]
                skodun = result[6]
                stada = result[7]
                if str(result[0]) == str(leitarnr):
                    return template("changeCar.tpl", a = fastanr,
                                                    b = tegund,
                                                    c = verksmidjunr,
                                                    d = skraningardagur,
                                                    e = co2,
                                                    f = thyngd,
                                                    g = skodun,
                                                    h = stada)
            else:
                return template("popup.tpl",text="Bíll ekki til")
    connection.close()
    return template("index.tpl")

@route("/utskra")
def utskraning():
    response.set_cookie("account","", expires=0)
    return template("index.tpl")

run()

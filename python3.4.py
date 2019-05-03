# -*- coding: utf-8 -*-
"""
Created on Thu May 03 11:27:48 2018

@author: colpaera
"""
import time
import qi
import argparse
import sys
import numpy
from PIL import Image
from naoqi import ALProxy
import math
import mysql.connector

"""
-------------------------------------------------------Interaction----------------------------------------------------
"""
class HumanGreeter(object):
        
    def __init__(self, app,salle):
        """ Constructeur """
        self.flag=False
        self.salle=salle
        """ Transfert au robot """
        app.start()
        session = app.session
        """ Connexion aux differents services """
        self.memory = session.service("ALMemory")
        self.speech_reco=session.service("ALSpeechRecognition")
        self.tts=session.service("ALTextToSpeech")
        self.animatedspeech=session.service("ALAnimatedSpeech")
        """ Liaison du callback """
        self.subscriber = self.memory.subscriber("WordRecognized")
        self.subscriber.signal.connect(self.fonctionage)
        """ Initialisation des parametres """
        self.speech_reco.setLanguage("French")
        vocabulaire=["je suis perdu","aurevoir","ok google","quelle est cette salle","qui est moche ici","a quoi sert cette salle","menu","bonjour","comment visiter l'école"]
        self.speech_reco.setVocabulary(vocabulaire,True)
        self.speech_reco.setLanguage("French")
        
    def fonctionage(self, value):
        
        print("Lancement du callback")
        self.speech_reco.unsubscribe("Test_ASR")
        self.flag=False
        configuration = {"bodyLanguageMode":"random"}

        if "bonjour" in value[0] and value[1]>0.5:
            self.animatedspeech.say("bonjour, je peux vous aider ?",configuration)
            
        if "comment visiter l'école" in value[0] and value[1]>0.5:
            self.animatedspeech.say("Il suffit d'appuyer sur ma tablette",configuration)

        if "menu" in value[0] and value[1]>0.5:
            self.animatedspeech.say("Vous pouvez me dire les phrases suivantes.                               .bonjour.                        .comment visiter l'école.                        .quelle est cette salle.                        .a quoi sert cette salle.                        .ok google et pour arréter l'écoute dites au revoir.",configuration)
        
        elif "aurevoir" in value[0] and value[1]>0.5:
            self.tts.say("aurevoir, a bientot")
            self.flag=True

        elif "quelle est cette salle" in value[0] and value[1]>0.5:
            if self.salle=="couloir":
                self.tts.say("on est dans le couloir")
            else :
                self.animatedspeech.say("on est dans la salle "+self.salle)

        elif "a quoi sert cette salle" in value[0] and value[1]>0.5:
            if self.salle=="couloir":
                self.tts.say("c'est le couloir")
            else :
                self.animatedspeech.say("la salle "+self.salle+" sert au za p p")
            
        elif "ok google" in value[0] and value[1]>0.5:
            self.tts.say("je suis pas google mais je peux quand même vous aider")
                
        print("Valeur du drapeau : " + str(self.flag))
                    
        if self.flag==False:
            self.speech_reco.subscribe("Test_ASR")
#       
        

    












"""          
--------------------------------------------------------------DEBUT DIJKSTRA------------------    
"""  

def ligneInit(Graphe,depart) :
    """ Renvoie la première ligne du tableau """
    L = []
    # nombre de lignes de Graphe donc nombre de sommets
    n = len(Graphe)
    for j in range(n) :
        poids = Graphe[depart][j]
        if poids :
        # si l’arête est présente
            L.append([ poids, depart ])
        else :
            L.append(False)
    return [L]
def SommetSuivant(T, S_marques) :
    """ En considérant un tableau et un ensemble de sommets marqués,
    détermine le prochain sommet marqué. """
    L = T[-1]
    n = len(L)
    # minimum des longueurs, initialisation
    min = False
    for i in range(n) :
        if not(i in S_marques) :
    # si le sommet d’indice i n’est pas marqué
            if L[i]:
                if not(min) or L[i][0] < min :
    # on trouve un nouveau minimum
    # ou si le minimum n’est pas défini
                    min = L[i][0]
                    marque = i
    return(marque)
def ajout_ligne(T,S_marques,Graphe) :
    """ Ajoute une ligne supplémentaire au tableau """
    L = T[-1]
    n = len(L)
    # La prochaine ligne est une copie de la précédente,
    # dont on va modifier quelques valeurs.
    Lnew = L
    # sommet dont on va étudier les voisins
    S = S_marques[-1]
    # la longueur du (plus court) chemin associé
    long = L[S][0]
    for j in range(n) :
        if j not in S_marques:
            poids = Graphe[S][j]
            if poids :
            # si l’arète (S,j) est présente
                if not(L[j]) : # L[j] = False
                    Lnew[j] = [ long + poids, S ]
                else :
                    if long + poids < L[j][0] :
                        Lnew[j] = [ long + poids, S ]
    T.append(Lnew)
        # Calcul du prochain sommet marqué
    S_marques.append(SommetSuivant(T, S_marques))
    return T, S_marques
    
def calcule_tableau(Graphe, depart) :
    """ Calcule le tableau de l’algorithme de Dijkstra """
    n = len(Graphe)
    # Initialisation de la première ligne du tableau
    # Avec ces valeurs, le premier appel à ajout_ligne
    # fera le vrai travail d’initialisation
    T=[[False] *n]
    T[0][depart] = [depart, 0]
    8
    # liste de sommets marques
    S_marques = [ depart ]
    while len(S_marques) < n :
        T, S_marques = ajout_ligne(T, S_marques, Graphe)
    return T
    
def plus_court_chemin(Graphe, depart, arrivee) :
    """ Détermine le plus court chemin entre depart et arrivee dans
    le Graphe"""
    n = len(Graphe)
    # calcul du tableau de Dijkstra
    T = calcule_tableau (Graphe,depart)
    # liste qui contiendra le chemin le plus court, on place l’arrivée
    C = [ arrivee ]
    while C[-1] != depart :
        C.append( T[-1][ C[-1] ][1] )
    # Renverse C, pour qu’elle soit plus lisible
    C.reverse()
    return C
    
def transfo2(g):
    liste1=g.split("/")
    liste2=[]
    liste_temp=[]
    for i in liste1:
        liste2.append(i.split(","))

    for j in range (len(liste2)):
        for k in range(len(liste2[j])):
            if len(liste2[j][k])==1:
                liste2[j][k]=int(liste2[j][k])
            else :
                liste2[j][k]=False

    return liste2
    
def computeShortestPath(graphe,position,cible):
    b=""
    position_string=""
    a=transfo2(graphe)
    chemin=plus_court_chemin(a,position,cible)
    for i in range (len(chemin)):
        if (len(str(chemin[i]))==1):
            position_string="0"+str(chemin[i])
        else:
            position_string=str(chemin[i])
        b=b+position_string+","
    return b
"""          
--------------------------------------------------------------FIN DIJKSTRA------------------    
"""    
    
def retourne_position_cible(liste,i):
    position=liste[3*i:(3*i)+2]
    cible=liste[(3*(i+1)):(3*(i+1))+2]
    return position,cible
    
def lecture_txt(nom_fichier):
    x="http://tp-epu.univ-savoie.fr/~colpaera/app/bdd/plan/"+nom_fichier+".txt"
    import urllib
    page=urllib.urlopen(x)
    strpage=page.read()
    return (strpage)
    
def cherche_angle_distance(donnees,destination):
    x=donnees.find(destination)
    angle=donnees[x+5:x+8]
    distance=donnees[x+9:x+10]
    return angle,distance
    
def cherche_angle_correction(donnees,destination):
    x=donnees.find(destination)
    angle=donnees[x+11:x+14]
    return angle
    
def fait_angle(angle):
    motionProxy  = ALProxy("ALMotion", "193.48.125.58", 9559)
    motionProxy.moveTo(0,0,math.radians(angle))

    
def fait_distance(distance):
    motionProxy  = ALProxy("ALMotion", "193.48.125.58", 9559)
    motionProxy.moveTo(distance,0,0)
    

def parle(texte):
    tts = ALProxy("ALTextToSpeech", "193.48.125.58", 9559)
    tts.say(texte)
    
def cherche_information(nom_fichier):
    x="http://tp-epu.univ-savoie.fr/~colpaera/app/bdd/information/"+nom_fichier+".txt"
    import urllib
    page=urllib.urlopen(x)
    strpage=page.read()
    return (strpage)

def nao_mark():
    
    motionProxy  = ALProxy("ALMotion", "193.48.125.58", 9559)
    tracker = ALProxy( "ALTracker" ,"193.48.125.58", 9559)
    tracker.lookAt([3,0,0],0,0.5,False)
    targetName = "LandMark"
    distanceX = 0.9
    distanceY = 0.0
    angleWz = 0.0
    thresholdX = 0.1
    thresholdY = 0.1
    thresholdWz = 0.1
    sizeMark = 0.15
    markIds = [68, 85, 84, 204, 145, 76, 115, 153, 112, 11, 135, 127, 170, 123, 114, 121]
    effector = "None"
    isRunning = False
    tracker.setEffector(effector)
    tracker.registerTarget(targetName, [sizeMark, markIds])
    
    tracker.setRelativePosition([-distanceX, distanceY, angleWz,
                                       thresholdX, thresholdY, thresholdWz])
                                       
    tracker.setMode("Head")
    tracker.track(targetName) #Start tracker
    isRunning = True
    texte="Je me recalibre en igrec"
    parle(texte)
    time.sleep(0.5)
    y=(tracker.getTargetPosition(2))
    print("Target position: ", y)
    isRunning=False
    tracker.stopTracker()
    motionProxy.moveTo(0,y[1],0)
    tracker.lookAt([3,0,0],0,0.5,False)
    tracker.setMode("Move")
    tracker.track(targetName) #Start tracker
    isRunning = True
    texte="Je me recalibre en x"
    parle(texte)
    time.sleep(2)
    texte="Je suis recalibré"
    parle(texte)    
    y=(tracker.getTargetPosition(2))
    print("Target position: ", y)
    isRunning=False
    tracker.stopTracker()
    
def calibrage_angle(angle_init,position):
    motionProxy  = ALProxy("ALMotion", "193.48.125.58", 9559)
    print("angle de base : ",angle_init)
    
    x="http://tp-epu.univ-savoie.fr/~colpaera/app/bdd/plan/angle/"+position+".txt"
    import urllib
    page=urllib.urlopen(x)
    angle=float(page.read())
    
    pos=(motionProxy.getRobotPosition(True))[2]    
    print("angle actuel : ",pos)
    
    
    delta=(pos-angle)-angle_init
    print("delta : ",delta)
    motionProxy.moveTo(0,0,delta)
    
def calibrage_angle2(angle_init,angle,position):
    x="http://tp-epu.univ-savoie.fr/~colpaera/app/bdd/plan/angle/"+position+".txt"
    import urllib
    page=urllib.urlopen(x)
    angle_nao=float(page.read())
    
    motionProxy  = ALProxy("ALMotion", "193.48.125.58", 9559)
    pos=(motionProxy.getRobotPosition(True))[2] 
    
    delta=(angle_init+angle_nao+angle)-pos
    if (delta>math.pi) :
        delta=delta-(2*math.pi)
    elif (delta<-math.pi):
        delta=delta+(2*math.pi)
    print("delta : ",delta)
    motionProxy.moveTo(0,0,delta)    
    
def main2(session,position,destination,pos_init):

    
    
    graphe=lecture_txt("graphe")
    """provient de a tablette : """
    chemin_le_plus_court=computeShortestPath(graphe,position,destination)
    print("chemin_le_plus_court\n")
    print(chemin_le_plus_court)
    tracker = ALProxy( "ALTracker" ,"193.48.125.58", 9559)
    tracker.lookAt([3,0,0],0,0.5,False)
    nao_mark()
    for i in range((len(chemin_le_plus_court)/3)-1):

        position_cible=retourne_position_cible(chemin_le_plus_court,i)
        print("position,cible\n")    
        print(position_cible)
        contenu_fichier_position=lecture_txt(position_cible[0])
        print("contenu en fonction de position\n")
        print(contenu_fichier_position)
        angle_distance=cherche_angle_distance(contenu_fichier_position,position_cible[1])
        print("angle distance jusque cible\n")
        print(angle_distance)
        angle=int(angle_distance[0])
        fait_angle(angle)
        
        calibrage_angle2(pos_init,math.radians(angle),position_cible[0])
        print(angle_distance[1])
        distance=int(angle_distance[1])
        fait_distance(distance)
        angle_correction=cherche_angle_correction(contenu_fichier_position,position_cible[1])
        angle_c=int(angle_correction)
        fait_angle(angle_c)
        
        calibrage_angle(pos_init,position_cible[1])
        
        nao_mark()        
        texte="Je suis arrivé au point "+position_cible[1]
        parle(texte)
        
    information=cherche_information(str(destination))
    parle(information)
    
def trad(point):
    if (point=="A217"):
        return (0)
    elif (point=="A203"):
        return (2)
    elif (point=="A204"):
        return (3)
    elif (point=="A205"):
        return (6)
    
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    
    
    parser.add_argument("--ip", type=str, default="193.48.125.58",
                        help="Robot IP address. On robot or Local Naoqi: use '193.48.125.58'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["HumanGreeter", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    
    animatedSpeechProxy = ALProxy("ALAnimatedSpeech", "193.48.125.58", 9559)
    animation_player_service = session.service("ALAnimationPlayer")
    motionProxy  = ALProxy("ALMotion", "193.48.125.58", 9559)
    pos_init=(motionProxy.getRobotPosition(True))[2]
    
    conn = mysql.connector.connect(host="tp-epu.univ-savoie.fr",port=3308,user="colpaera", password="z6uiwjy9", database="colpaera")
    cursor = conn.cursor()
    
    cursor.execute("Delete from app")
    cursor.execute("INSERT INTO app(position) values('A217')") 
    
    """connection_url = "tcp://" + args.ip + ":" + str(args.port)
    app = qi.Application(["HumanGreeter", "--qi-url=" + connection_url]) """ 
    human_greeter = HumanGreeter(app,"A217")
    while(True):
        cursor.execute("SELECT destination FROM app")
        rows=cursor.fetchall()
        print(rows)
#        ^start(animations/[posture]/Gestures/Me_1)
#        animation_player_service.run("animations/[posture]/Gestures/ShowTablet_1")
        
        animatedSpeechProxy.say("Allez-y cliquez sur. Guide moi Pepper et choisissez une destination pour que je vous y emmène.")
        
        
        while(rows[0][0]==None):
            cursor.execute("SELECT destination FROM app")
            rows=cursor.fetchall()
            print("Pas de destination pour l'instant")
            time.sleep(1)
        dest=rows[0][0]
        print("destination :",dest)
        dest=dest.encode('ascii','ignore')
        animatedSpeechProxy.say("Veuillez reculer pour me laisser libre de mes mouvements,  ne restez pas dans mon chemin. Je vous ferez signe quand vous pouvez interagir de nouveau avec moi")

        animatedSpeechProxy.say("c'est parti nous allons a la salle   "+dest)
        
        cursor.execute("SELECT position FROM app")
        rows=cursor.fetchall()
        pos=rows[0][0]
        print("position : ",pos)
        pos=pos.encode('ascii','ignore')
        
        position=trad(pos)
        print(position)
        destination=trad(dest)
        print(destination)
        
        time.sleep(2)
        ##PARTIE DEPLACEMENT
        main2(session,position,destination,pos_init)
        
        time.sleep(2)
        animatedSpeechProxy.say("nous somme arrivé")
        
        cursor.execute("Update app set position='"+dest+"'")
        cursor.execute("Update app set destination=NULL")
        
        human_greeter.salle=dest
        human_greeter.tts.say("je vous ecoute, dites menu pour savoir les phrases à me dire")
        human_greeter.speech_reco.subscribe("Test_ASR")
        
        while (human_greeter.flag==False):
            print(human_greeter.flag)
            time.sleep(1)
        

      
    conn.close()

    

    
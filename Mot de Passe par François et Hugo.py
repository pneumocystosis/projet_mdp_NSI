import tkinter as tk
from functools import partial
import tkinter.font as tkFont

carspeciaux = ["~","!","@","#","$","%","^","*","(",")","_","-","+","=","{","}","[","]","|",":",";","\"","?"]

#fonctions suivantes verifient si contraintes sont respectées

#verifie si le mdp contient maj et min        
def hasUpperLower(mdp1string):
    hasUpper, hasLower = False, False #valeurs booléennes qui deviendront vraies seulement si les critères sont respectées
    for both in mdp1string: #boucle qui qui prend "both", qui est un caractère dans la chaîne de caractères
        if both.isupper():  #isUpper est une fonction prédéfinie qui vérifie qu'un caractère est en majuscule
            hasUpper = True
        if both.islower(): #isLower est une fonction prédéfinie qui vérifie qu'un caractère est en minuscule
            hasLower = True
    if hasLower and hasUpper: #si les deux valeurs booléennes sont vraies, alors les 2 critères sont respectés 
        return True #la fonction retourne donc "True"

#verifie si contient numéro
def hasNum(mdp1string):
    for num in mdp1string: #pour chaque caractère dans la chaîne de caractères
        if num.isnumeric(): #isnumeric est une fonction prédéfinie qui verifie qu'il y a un numéro
            return True #la fonction retourne "True"

#verifie si contient 8 caracteres ou plus
def hasMinChar(mdp1string):
    if len(mdp1string) >= 8: #si la longueur est supérieure ou égale à 8
        return True #la fonctione retourne "True"
            
#verfie si contient caracteres spéciaux
def hasSpecial(mdp1string):
    for spec in mdp1string: #pour chaque caractère dans la chaîne de caractères
        if spec in carspeciaux: #si le caractère est aussi présent dans la liste des carctères spéciaux
            return True #la fonction retourne "True"

#verifie si toutes contraintes sont respectées et renvoie message d'erreur
def allTrue(mdp1string):
    
    #creation de 5 variables booléennes qui sont représentées par les fonctions 
    hasCases = hasUpperLower(mdp1string) #si la fonction hasUppperLower qui a pour paramètre la liste de caractères, est vraie, alors hasCases sera vraie
    hasNumbers = hasNum(mdp1string)
    hasEnoughChars = hasMinChar(mdp1string)
    hasSpecialChars = hasSpecial(mdp1string)
    #si tout est vérifié (if all is true then allTrue becomes true)
    if hasCases and hasNumbers and hasEnoughChars and hasSpecialChars:
        return True
    else:
        #on verifie si toutes les variables sont vraies puis on affiche un message d'erreur en fonction de ce qui n'est pas vérifié
        if not hasCases:
            
            error1Label.place(relx=0.01, rely=0.85) #positionnement de message d'erreur. relx et rely sont des valeurs de 0 à 1, avec 0 min et 1 max
        if not hasNumbers:
            
            error2Label.place(relx=0.01, rely=0.91)
        if not hasEnoughChars:
            
            error3Label.place(relx=0.5, rely=0.85)
        if not hasSpecialChars:
            
            error4Label.place(relx=0.5, rely=0.91)
        return False #la fonction allTrue est fausse car les contraintes ne sont pas toutes respectées

def validateCheck(mdp1, mdp2):
    #variable mdp1string est = a ce que l'on a mis dans la boite texte mdp1
    mdp1string = mdp1.get()
    #variable mdp2string est = a ce que l'on a mis dans la boite texte mdp2
    mdp2string = mdp2.get()

    #tous les messages d'erreur (ou de succès) deviennent invisibles avant la vaalidation. ils se réafficheront si les contraintes ne sont toujours pas respectées, bien sûr
    error1Label.place_forget() 
    error2Label.place_forget()
    error3Label.place_forget()
    error4Label.place_forget()
    SuccesspassLabel.place_forget()
    FailpassLabel.place_forget()
    if allTrue(mdp1string):
        if mdp1string == mdp2string: #si les 2 mots de passe sont identiques
            #affiche du texte dans la deuxieme boite qui dit que les codes sont les memes et qu'ils verifient toutes les contraintes
            SuccesspassLabel.place(relx=0.21, rely=0.88)       
            return True
        else: #si les 2 mots de passe ne sont pas identiques
            #les codes verifient les contraintes mais ne sont pas les mêmes
            FailpassLabel.place(relx=0.19, rely=0.88)
            return False

#variables de mise en page
HEIGHT = 700
WIDTH = 1000
canvasBG="#e5e5e5" #couleur de l'arrière plan
BG="#fff" #couleur du 2ème arrière plan
EntryBG="#fff" #couleur de la zone de saisie
CheckBG="#008952" #couleur du bouton "Vérifier"
textColor="#0F0F0F" #couleur de texte 1
textColor2="#545454" #couleur de texte 2


#box, canvas and frame
box=tk.Tk() #initialisation de la fenêtre
box.title("Password verification") #titre de la fenêtre
canvas=tk.Canvas(box, height=HEIGHT, width=WIDTH, bg=canvasBG) #initialisation de l'arrière plan 1
frame=tk.Frame(box, bg=BG) #initialisation de l'arrière plan 2

#fonts
titleFont=tkFont.Font(family="Calibri", size=28, weight="bold") #titre
subtitleFont=tkFont.Font(family="Calibri", size=13, weight="bold") #sous titre
entryLabelFont=tkFont.Font(family="Calibri", size=16, weight="bold") #texte demandant le mdp
entryFont=tkFont.Font(family="Calibri", size=25, weight="bold") #texte de l'entrée
checkFont=tkFont.Font(family="Calibri", size=16, weight="bold")#texte du bouton "Valider"
errorFont=tkFont.Font(family="Calibri",size=11,weight="bold") #texte des messages d'erreur
passComparisonOutputFont=tkFont.Font(family="Calibri",size=18,weight="bold") #texte des messages affichés si les contraintes sont respectées (sauf la vérification que les 2 mdp sont égaux)

#error and success labels, used in functions
error1Label=tk.Label(frame, text="\u2757 mot de passe doit contenir majuscules et minuscules", fg="red", font=errorFont, bg=BG) #se place dans le "frame", s'affiche en tant que points gras, texte, couleur du texte, type de la police défini plus haut, couleur de l'arrière plan défini plus haut aussi
error2Label=tk.Label(frame, text="\u2757 mot de masse doit contenir des nombres", fg="red", font=errorFont, bg=BG)
error3Label=tk.Label(frame, text="\u2757 mot de passe doit contenir 8 caractères au minimum", fg="red", font=errorFont, bg=BG)
error4Label=tk.Label(frame, text="\u2757 mot de passe doit contenir des caractères spéciaux", fg="red", font=errorFont, bg=BG)
SuccesspassLabel=tk.Label(frame, text="Les mots de passe sont conformes et identiques", fg="#60b91f", bg=BG, font=passComparisonOutputFont)
FailpassLabel=tk.Label(frame, text="Les mots de passe sont conformes mais différents", fg="red", bg=BG, font=passComparisonOutputFont)

#entry, subtitle title labels
titre=tk.Label(frame, text="Password Verification", font=titleFont, bg=BG,fg=textColor)
subtitle=tk.Label(frame, text="Vérifiez si votre mot de passe remplit nos critères de sécurité.",font=subtitleFont, bg=BG, fg=textColor)
mdp1Label=tk.Label(frame, text="Nouveau mot de passe", bg=BG, fg=textColor2, font=entryLabelFont)
mdp2Label=tk.Label(frame,text="Confirmez le mot de passe", bg=BG, fg=textColor2, font=entryLabelFont)
mdp1=tk.StringVar()
mdp2=tk.StringVar()
mdp1Entry=tk.Entry(frame, textvariable=mdp1, show='\u2022', relief="groove", borderwidth=5, font=entryFont, bg=EntryBG, fg=textColor)
mdp2Entry=tk.Entry(frame, textvariable=mdp2, show='\u2022',relief="groove", borderwidth=5, font=entryFont, bg=EntryBG, fg=textColor)


#CheckButton
validateCheckvar=partial(validateCheck, mdp1, mdp2) #validation du mdp. la fonction "partial" permet de de passer une fonction avec ses paramètres, la valeur de validateCheckvar sera booléenne
CheckButton=tk.Button(frame, text="Valider", command=validateCheckvar, cursor="hand2", bg=CheckBG, font=checkFont, fg="#fff") #"command" est la fonction activée lorsque le bouton est pressé, "cursor" est le type de curseur

#affiche l'arrière plan
canvas.pack()

#position de tous les messages et boutons quand ils doivent être affichés
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
titre.place(relx=0.29, rely=0.05)
subtitle.place(relx=0.22, rely=0.18)

mdp1Label.place(relx=0.2, rely=0.3)
mdp1Entry.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.12)

mdp2Label.place(relx=0.2, rely=0.52)
mdp2Entry.place(relx=0.2, rely=0.57, relwidth=0.6, relheight=0.12)


CheckButton.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.08)

#pour que le programme fonctionne
box.mainloop()
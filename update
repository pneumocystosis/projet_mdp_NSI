'''
Saint-Jean François -602
Parkhouse Hugo -602
'''
#tkinter=crée des boites
#partial, permet d'éxecuter une fonction avec 2 paramètres
#tkfont = polices d'écriture
import tkinter as tk
from functools import partial
import tkinter.font as tkFont
 
 
#fonctions suivantes verifient si contraintes sont respectées
 
#verifie si le mdp contient maj et min        
def hasUpperLower(mdp1string):
    hasUpper, hasLower = False, False
    for both in mdp1string:
        if both.isupper():
            #isUpper est une fonction prédéfinie
            hasUpper = True
        if both.islower():
            #isLower est une fonction prédéfinie
            hasLower = True
    if hasLower and hasUpper:
        return True
 
#verifie si contient numéro
def hasNum(mdp1string):
    for num in mdp1string:
        if num.isnumeric():
            #isnumeric est une fonction prédéfinie qui verifie qu'il y a un numéro
            return True
 
#verifie si contient 8 caracteres ou plus
def hasMinChar(mdp1string):
    if len(mdp1string) >= 8:
        return True
           
#verfie si contient caracteres spéciaux
def hasSpecial(mdp1string):
    for spec in mdp1string:
        if spec in carspeciaux:
            return True
 
#verifie si toutes contraintes sont respectées et renvoie message d'erreur
def allTrue(mdp1string):
   
    #creation de 5 variables qui sont représentées par les fonctions
    hasCases = hasUpperLower(mdp1string)
    hasNumbers = hasNum(mdp1string)
    hasEnoughChars = hasMinChar(mdp1string)
    hasSpecialChars = hasSpecial(mdp1string)
    #si tout est vérifié (if all is true then allTrue becomes true)
    if hasCases and hasNumbers and hasEnoughChars and hasSpecialChars:
        return True
    else:
        #on verifie si toutes les variables sont vraies puis on affiche un message d'erreur en fonction de ce qui n'est pas vérifié
        if not hasCases:
           
            error1Label.place(relx=0.01, rely=0.85)
        if not hasNumbers:
           
            error2Label.place(relx=0.01, rely=0.91)
        if not hasEnoughChars:
           
            error3Label.place(relx=0.5, rely=0.85)
        if not hasSpecialChars:
           
            error4Label.place(relx=0.5, rely=0.91)
        return False
 
def validateCheck(mdp1, mdp2):
    #variable mdp1string est = a ce que l'on a mis dans la boite texte mdp1
    mdp1string = mdp1.get()
    #variable mdp2string est = a ce que l'on a mis dans la boite texte mdp2
    mdp2string = mdp2.get()
    #oublie les messages d'erreur affichés lors du "validate" précédent
    error1Label.place_forget()
    error2Label.place_forget()
    error3Label.place_forget()
    error4Label.place_forget()
    SuccesspassLabel.place_forget()
    FailpassLabel.place_forget()
    if allTrue(mdp1string):
        if mdp1string == mdp2string:
            #affiche du texte dans la deuxieme boite qui dit que les codes sont les memes et qu'ils verifient toutes les contraintes
            SuccesspassLabel.place(relx=0.21, rely=0.88)      
            return True
        else:
            #les codes verifient les contraintes mais ne sont pas les mêmes
            FailpassLabel.place(relx=0.19, rely=0.88)
            return False
 
#liste de caractères spéciaux
carspeciaux = ["~","!","@","#","$","%","^","*","(",")","_","-","+","=","{","}","[","]","|",":",";","\"","?"]
 
HEIGHT = 700
WIDTH = 1000
 
#boite d'affichage
box = tk.Tk()
box.title("Password verification")
#canvas est un fond gris pour faire plus ressortir le "frame" utilisé plus tard dans le programme
canvas = tk.Canvas(box, height=HEIGHT, width=WIDTH)
canvas.pack()
 
#crée un carré dans le canvas, de couleur blanche
frame = tk.Frame(box, bg='#fff')
#placement de "frame"
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
 
#fonts
#police de "password verification"
titleFont = tkFont.Font(family="Calibri", size=28, weight="bold")
#"verifiez si vos ...
subtitleFont=tkFont.Font(family="Calibri", size=13, weight="bold")
#police des sous-titres "nv mdp et confirmez mdp"
entryLabelFont = tkFont.Font(family="Calibri", size=16, weight="bold")
#ce qu'on entre comme mdp
entryFont = tkFont.Font(family="Calibri", size=25, weight="bold")
#police d'ecriture de Valider
checkFont = tkFont.Font(family="Calibri", size=16, weight="bold")
#pour les messages d'erreur
errorFont = tkFont.Font(family="Calibri",size=11,weight="bold")
#police du message final affiché, si les mdp correspondent ou non
singleReturnFont = tkFont.Font(family="Calibri",size=18,weight="bold")
 
#messages d'erreur en fonction des critères non remplis
error1Label= tk.Label(frame, text="\u2757 mot de passe doit contenir majuscules et minuscules", fg = "red", font=errorFont, bg="#fff")
error2Label= tk.Label(frame, text="\u2757 mot de masse doit contenir des nombres", fg = "red", font=errorFont, bg="#fff")
error3Label= tk.Label(frame, text="\u2757 mot de passe doit contenir 8 caractères au minimum", fg = "red", font=errorFont, bg="#fff")
error4Label= tk.Label(frame, text="\u2757 mot de passe doit contenir des caractères spéciaux", fg = "red", font=errorFont, bg="#fff")
#critères remplis, messages d'affichage en fonction de si les mdp sont identiques ou non
SuccesspassLabel= tk.Label(frame, text="Les mots de passe sont conformes et identiques", fg = "#60b91f", bg="#fff", font=singleReturnFont)
FailpassLabel= tk.Label(frame, text="Les mots de passe sont conformes mais différents", fg = "red", bg="#fff", font=singleReturnFont)
 
'''
placement de tous les élements du programme
titre
subtitles
labels
entry box
bouton "validate"
'''
titre = tk.Label(frame, text="Password Verification", font=titleFont, bg="#fff",fg ="#000")
titre.place(relx=0.29, rely=0.05)
 
 
subtitle=tk.Label(frame, text="Vérifiez si votre mot de passe remplit nos critères de sécurité.",font=subtitleFont, bg="#fff", fg="#707173")
subtitle.place(relx=0.22, rely=0.18)
 
 
mdp1Label= tk.Label(frame, text="Nouveau mot de passe", bg='#fff', fg="#000", font=entryLabelFont)
mdp1Label.place(relx=0.2, rely=0.3)
# StringVar() permet de retenir ce qui est entré par l'utilisateur
mdp1 = tk.StringVar()
mdp1Entry = tk.Entry(frame, textvariable=mdp1, show='\u2022', relief="groove", borderwidth=5, font=entryFont)
mdp1Entry.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.12)
 
mdp2Label = tk.Label(frame,text="Confirmez le mot de passe", bg='#fff', fg="#000", font=entryLabelFont)
mdp2Label.place(relx=0.2, rely=0.52)
mdp2 = tk.StringVar()
mdp2Entry = tk.Entry(frame, textvariable=mdp2, show='\u2022',relief="groove", borderwidth=5, font=entryFont)
mdp2Entry.place(relx=0.2, rely=0.57, relwidth=0.6, relheight=0.12)
 
_validateCheck = partial(validateCheck, mdp1, mdp2)
 
 
CheckButton = tk.Button(frame, text="Valider", command=_validateCheck, cursor ="hand2", bg="#008952", font=checkFont, fg="#fff")
CheckButton.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.08)
 
 
box.mainloop()

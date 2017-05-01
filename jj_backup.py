import sys,os
from OptionFrame import OptionFrame
from backupOptions import BackupOption
from functions import displayError
from BackupFactory import BackupFactory


#si des args on été passés   
if(len(sys.argv)>1):
    #si 2 arguments ont été passés créer une erreur
    args = sys.argv[1:]
    optionsList=[]      #type: List[BackupOption]
    if (args[0] =="-all"):
        # si l'argument est all : ajoute à la liste un objet BackupOption depuis chaque fichier conf
        for filename in os.listdir("conf"):
            if (os.path.isfile("conf/"+filename)):
                optionsList.append(BackupOption.createFromConfFile("conf/"+filename))
    else:
        #ajout de chaque option à la liste 
        for confName in args:
            if (os.path.isfile("conf/"+confName)==False):
                # si l'argument est un fichier conf existant, ajout un objet BackupOption à la liste
                displayError("Le fichier conf : "+"conf/"+confName+" n'existe pas")
            else:
                optionsList.append(BackupOption.createFromConfFile("conf/"+confName))
    for option in optionsList:        
        try:
            backup = BackupFactory.create(option)
            backup.execute()
        except Exception as e:
            displayError(e.args[1])

else:
    options =  BackupOption()
    if(sys.stdout.isatty()):
        #TODO appeler du menu principal en console
        pass
    else:
        hFrame = OptionFrame(options)
        hFrame.show()
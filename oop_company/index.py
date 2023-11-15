import random

def error(text):
    print(f"ERROR: {text}")

class grade:
    def __init__(self, grade_name):
        self.__name = grade_name
        
    

class worker: 
    def __init__(self, worker_name, worker_grade = False):
        self.__name = worker_name
        self.__grade = worker_grade


    def __str__(self):
        return f"Jméno zaměstnance: {self.__name}, Pozice: {self.__grade}"
       

class branch:
    def __init__(self, mesto, ulice, cislo_popisne):
        self.__town = mesto
        self.__street = ulice
        self.__depNum = cislo_popisne
    
    def __str__(self):
        return f"Město: {self.__town}, Ulice: {self.__street}, Číslo popisné: {self.__depNum}"
           
class company:

    def __init__(self, company_name):
        self.__name = company_name
        self.__branches = {}
        self.__workers = {}
        self.__grades = {}
    def addBranch(self, name, town, street, depNum):
        if not name in self.__branches:
            self.__branches[name] = branch(town, street, depNum)
        else:
            error(f"Duplicitní hodnota {name}")
    def removeBranch(self, name):
        if name in self.__branches:
            del self.__branches[name]
    
    def addWorker(self, name, grade):
        id = random.randint(1,9999)
        if not id in self.__workers:
            self.__workers[id] = worker(name,grade)
    
    def removeWorker(self, id):
            if id in self.__workers:
                del self.__workers[id]   
    def addGrade(self, name):
        id = random.randint(1,9999)
        if not id in self.__grades:
            self.__grades[id] = grade(name)
    def removeGrade(self, id):
            if id in self.__grades:
                del self.__grades[id] 

    def __str__(self):
       return f"Jmeno firmy: {self.__name}, Pocet pobocek: {len(self.__branches)}"
      
    def getBranches(self):
        return self.__branches
    
    def getWrokers(self):
        return self.__workers

    def getGrades(self):
        return self.__grades
    
    def getData(self):
        return f"Firma: {self.__name}, Počet poboček: {len(self.__branches)}, Počet zaměstnanců: {len(self.__workers)}"
    





company_list = {}
inputer = True 
state = "main_menu"
selected_comapny = 0
company_list[4569] = company("KOKOTI")

while inputer == True:
    if state == "main_menu":
        print("[1] Výpis firem")
        print("[2] Vytvořit firmu")
        print("[3] Vybrat firmu")
        task = int(input("Číslo akce: "))

        if task == 1:
            print("Výpis firem")
            for company in company_list.items():
                print(f"{company[0]}   {company[1]}")
        if task == 2:
            print("Zadejte jméno firmy: ")
            id = random.randint(1,9999)
            name = input("Jméno: ")
            company_list[id] = company(name)

        if task == 3:
            print("Vyber si firmu podle id")
            for company in company_list.items():
                print(f"{company[0]}   {company[1]}")
      
            id = int(input("ID FIRMY: "))
            if id in company_list:
                selected_comapny = id
                state = "company_selected"
            else:
                error(f"{id} Tato firma není vytvořena")
    if state == "company_selected":
        print("----------------------------------")
        print(f"Ovládáte {company_list[selected_comapny]}")
        print("----------------------------------")
        print("[1] Přidat pobočku")
        print("[2] Odstrant pobočku")
        print("[3] Přidat pozici")
        print("[4] Odstrant pozici")
        print("[5] Přidat zaměstnance")
        print("[6] Odstranit zaměstnance")
        print("_______________________________")
        print("[7] Zobrazit pobočky")
        print("[8] Zobrazit zaměstnance")
        print("[9] Zobrazit pozice")
        print("_______________________________")
        print("[10] Zpět do menu")
        task = int(input("Číslo akce: "))

        if task == 1:
            print("Přidat pobočku")
            name = input("Jméno pobočky: ")
            town = input("Město: ")
            street = input("Ulice: ")
            depNum = input("Číslo popisné: ")
            company_list[selected_comapny].addBranch(name, town, street, depNum)
        if task == 2:
            print("Odstrant pobočku")
            name = input("Jméno pobočky: ")
            company_list[selected_comapny].removeBranch(name)
        
        if task == 3:
            print("Přidat pozici")
            name = str(input("Jméno pozice: "))
            company_list[selected_comapny].addGrade(name)
        if task == 4:
            print("Odstrant pozici")
            name = input("Jméno pozice: ")
            company_list[selected_comapny].removeGrade(name)
        if task == 5:
            print("Přidat zaměstnance")
            name = input("Jméno zaměstnance: ")
            grade = input("Pozice: ")
            company_list[selected_comapny].addWorker(name, grade)
        
        if task == 6:
            print("Odstranit zaměstnance")
            id = input("ID zaměstnance: ")
            company_list[selected_comapny].removeWorker(id)
            
        if task == 7:
            print("Zobrazit pobočky")
            for branch in company_list[selected_comapny].getBranches().items():
                print(branch[1])
        if task == 8:
            print("Zobrazit zaměstnance")
            for worker in company_list[selected_comapny].getWrokers().items():
                print(worker[1])
        if task == 9:
            print("Zobrazit pozice")
            for grade in company_list[selected_comapny].getGrades().items():
                print(grade[1])
        if task == 10:
            state = "main_menu"
            selected_comapny = 0
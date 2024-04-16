import sys
sys.path.append("./")

import os
from openpyxl import Workbook, load_workbook
from backend.functions import *
from vars import variables as var

def load_db() -> dict[str, str]:        
    load_eng = True
    db = "db/database.xlsx"
    
    i = 1

    EFA_Clubs = {} ## TODO - LOAD CLUB VALUES WITH ID INTO DICT

    while load_eng:
        wb = load_workbook(db)
        wb.active = wb["England"]

        ws = wb.active
        
        EPL = dict[str, str]
        EFA = ws
        
        i = int(i) + 1

        ## Checking to end the loop
        if str(EFA["A" + str(i)].value) == "None":
            load_eng = False
            break

        
        ## DEBUGGING 
        print(EFA["A" + str(i)].value)

        

load_db()
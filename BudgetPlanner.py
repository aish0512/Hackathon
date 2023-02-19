# This entrypoint file to be used in development. Start by reading README.md
import budget
import warnings
from budget import create_spend_chart
import pandas as pd
warnings.filterwarnings("ignore")

# ALl the expenses
{"Expense":"Gas bill","Amt":100,"Happiness":-10,"Priority":True},
{"Expense":"Electric  bill","Amt":80,"Happiness":-5,"Priority":True},
{"Expense":"Phone  bill","Amt":50,"Happiness":0,"Priority": False},
{"Expense":"Internet subscription","Amt":40,"Happiness":-2,"Priority": False},
{"Expense":"Cable TV subscription","Amt":70,"Happiness":-3,"Priority": False},
{"Expense":"Groceries from BudgetMart","Amt":150,"Happiness":5,"Priority": False},
{"Expense":"Groceries from ExpensiveBoutique","Amt":250,"Happiness":7,"Priority": False},
{"Expense":"Expensive handbag","Amt":500,"Happiness":10,"Priority": False}

def Budget_Calc(choice_dict,Tot_Amt,Happy_Val):
    choice_sorted = sorted(choice_dict, key=lambda x: (-x['Priority'], -x['Happiness'],x['Amt']))
    Path = []
    Budget = Tot_Amt
    Happiness = Happy_Val

    for choice in choice_sorted:
        if choice['Amt'] > Budget:
            print("Max Budget Reached")
        elif choice['Amt'] <= Budget:

            Budget,Happiness,Path = Tx(choice['Expense'],choice['Amt'],choice['Happiness'],
                                                                           Path,Budget,Happiness)
            print(Budget)
            print(Happiness)
            print(Path)
            
    return Budget,Happiness,Path

choice_dict = [
    {"Expense":"Expensive handbag","Amt":1000,"Happiness":25,"Priority":False},
    {"Expense":"Gas bill","Amt":100,"Happiness":-10,"Priority":True},
    {"Expense":"Electric bill","Amt":800,"Happiness":-5,"Priority":True},
    {"Expense":"Phone  bill","Amt":100,"Happiness":0,"Priority": False}
]
Budget_Calc(choice_dict,2000,0)

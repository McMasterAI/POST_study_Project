import pandas as pd

df = pd.read_csv("dta_file_converted.csv",  low_memory = False)
#print([df['ices_caseid'] == 100001])

class Person():
    def __init__(self, idNum):
        try: 
            self.row = df[df["ices_caseid"] == str(idNum)]
        except:
            print("ID Num not found")
            raise Exception

        self.caseID = idNum

        try:
            
            self.ices_opioidbase = float(self.row["ices_opioidbase"])
        except:
            self.ices_opioidbase = -1

        try:
            self.ices_opioid3 = float(self.row["ices_opioid3"])
        except:
            self.ices_opioid3 = -1

        try:
            self.ices_opioid6 = float(self.row["ices_opioid6"])
        except:
            self.ices_opioid6 = -1

        try:
            self.ices_opioid9 = float(self.row["ices_opioid9"])
        except:
            self.ices_opioid9 = -1

        try:
            self.ices_opioid12 = float(self.row["ices_opioid12"])
        except:
            self.ices_opioid12 = -1

        try:
            self.ices_amountdose = float(self.row["ices_amountdose"])
        except:
            self.ices_amountdose = -1

        try:
            self.ices_currdose3 = float(self.row["ices_currdose3"])
        except:
            self.ices_currdose3 = -1

        try:
            self.ices_currdose6 = float(self.row["ices_currdose6"])
        except:
            self.ices_currdose6 = -1

        try:
            self.ices_currdose9 = float(self.row["ices_currdose9"])
        except:
            self.ices_currdose9 = -1

        try:
            self.ices_currdose12 = float(self.row["ices_currdose12"])
        except:
            self.ices_currdose12 = -1

    def __str__(self):
        return "ID: {0} ".format(self.caseID)

    def findValue(self, colName):
        try:
            return self.row[str(colName)]
        except:
            return "ERROR OCCURED" 

numOfRows = int(len(df.index))

#b = Person(df.iloc[0])
b = Person(100001)
#c = df[df["ices_caseid"] == str(100001)]


print(b)
print(b.ices_currdose12)
print(b.findValue("ices_currdose12"))








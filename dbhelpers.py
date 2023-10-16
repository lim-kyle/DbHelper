"""
	Python Database helper
"""
from mysql.connector import connect
from pwinput import pwinput

def db_connect()->object:
    return connect(
        host="localhost",
        user="root",
        password="",
        database="studentdb"
    )
    
def doProcess(sql:str)->bool:
    db:object = db_connect()
    cursor:object = db.cursor()
    cursor.execute(sql)
    db.commit()
    return True if cursor.rowcount>0 else False
    
def getProcess(sql:str)->list:
    db:object = db_connect()
    cursor:object = db.cursor(dictionary=True)
    cursor.execute(sql)
    return cursor.fetchall()

def getall(table:str)->list:
    sql:str = f"SELECT * FROM `{table}`"
    return getProcess(sql)

def getrecord(table:str,**kwargs)->list:
    params:list = list(kwargs.items())
    flds:list = list(params[0])
    sql:str = f"SELECT * FROM `{table}` WHERE `{flds[0]}`='{flds[1]}'"
    return getProcess(sql)

def userLogin(table:str,**kwargs)->List:
	params:list = list(kwargs.items())
	flds:list = list(params[0])
	sql:str = f"SELECT * FROM `{table}` WHERE `{flds[0]}`='{flds[0]}' AND `{flds[1]}`='{flds[1]}'"
	return getProcess(sql)
	
def addrecord(table:str,**kwargs)->bool:
    flds:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    fld:str = "`,`".join(flds)
    val:str = "','".join(vals)
    sql:str = f"INSERT INTO `{table}`(`{fld}`) values('{val}')"
    print(sql)
    return doProcess(sql)
    
def updaterecord(table:str,**kwargs)->bool:
    flds:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    fld:list = []
    for i in range(1,len(flds)):
        fld.append(f"`{flds[i]}`='{vals[i]}'")
    params:str = ",".join(fld)
    sql:str = f"UPDATE `{table}` SET {params} WHERE `{flds[0]}`='{vals[0]}'"
    print(sql)
    return doProcess(sql)
    
def deleterecord(table:str,**kwargs)->bool:
    params:list = list(kwargs.items())
    flds:list = list(params[0])
    sql:str = f"DELETE FROM `{table}` WHERE `{flds[0]}`='{flds[1]}'"
    return doProcess(sql)
#addrecord('student', idno='0004', lastname='Andrade', firstname='Jerjer', course='BSCE', level='5')
#print(getrecord("student",idno='0001'))
#print(getall("student"))
#updaterecord('student',idno='0003',lastname='Alcarmen',firstname='Brandon',course='bscs',level='3')
#print(deleterecord("student",idno='0002'))
usern:str= input("Enter Username:")
passw:str= pwinput("Enter Password:")

user:list = userlogin('user',username=usern,password=passw)
if len(user)>0:
	print("Login Accepted")
else:
	print("Login Failed")


import pyodbc
import datetime

commandDone = False

while True:
	timesnow = datetime.datetime.now()
	if(bool(timesnow.minute % 5 == 0) and bool(timesnow.second % 55 == 0) and (commandDone == False) and (timesnow.minute != 0) and (timesnow.second != 0)):
		conn = pyodbc.connect('DRIVER={FreeTDS};Server=Waseca-db2;PORT=1433; Database=WasMfg; UID=testpack; PWD=Itron2;TDS_Version=7.2;')
		cursor= conn.cursor()
		print("From : ")
		print(timesnow - datetime.timedelta(minutes=15))
		print("To : ")
		print(timesnow)
		print("-------------------------------------------------")
		commandDone = True
		cursor.execute("UPDATE dbo.TestEvent SET DataCategoryID = ? WHERE TestDate > ? AND Passed = ? AND (PartNumber like ? OR PartNumber like ? OR PartNumber = ?)", 'E' , timesnow - datetime.timedelta(minutes=15),'0' , 'ERW%', 'SUB%', 'PCA-1601-001') 
		cursor.commit()
		cursor.execute("UPDATE dbo.InProcess SET DataCategoryID = ? WHERE TestDate > ? AND Passed = ? AND (PartNumber like ? OR PartNumber like ? OR PartNumber = ?)", 'E' , timesnow - datetime.timedelta(minutes=15),'0' , 'ERW%', 'SUB%', 'PCA-1601-001') 
		cursor.commit()
		cursor.close()
		del cursor
		conn.close()
	if(timesnow.minute % 5 == 0 and timesnow.second % 56 == 0 and (timesnow.minute != 0) and (timesnow.second != 0)) :
		commandDone = False

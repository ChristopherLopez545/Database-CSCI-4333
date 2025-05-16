# code to create and do sql statements 
import csv
import sqlite3

# THIS CODE IS FOR SETTING UP THE DATABASES FOR ROBOTS, SENSOR READINGS AND INTERVALS

# creating/ connection to the db 

connection = sqlite3.connect("robots.db")

# this lets us run sql commands to the db 
cursor = connection.cursor()
 
# create the robots table with id(pk) and name 
statement= '''
CREATE TABLE IF NOT EXISTS Robots(
    id integer,
    name text,
    primary key (id)
);
'''
cursor.execute(statement)


# # opening the csv file and filling up robots db 
# with open('robot.csv',mode = 'r') as file:
#     csvFile= csv.reader(file)
#     for lines in csvFile:
#         id = lines[0]
#         name = lines[1]
#         cursor.execute('INSERT INTO Robots VALUES (?,?)',(id,name))
#         #print(lines[1])
    
#testing the connection 
print(connection.total_changes) 

#saving the rows

# creating the sensor reading table 
statement= '''
CREATE TABLE IF NOT EXISTS Sensor_Reading(
    reading_id integer PRIMARY KEY AUTOINCREMENT,
    robot_id integer,
    x float,
    y float,
    timestamp integer,
    foreign key (robot_id) references Robots(id)
);
'''
cursor.execute(statement)

 # filling up the sensor reading for first robot from the t1.csv data 
 # 
with open('t1.csv',mode = 'r') as file:
     csvFile= csv.reader(file)
     lineNumber = 1
     for lines in csvFile:
         x = lines[0]
         y = lines[1]
         cursor.execute("INSERT into Sensor_Reading (robot_id,x,y,timestamp) VALUES (?,?,?,?)",(1,x,y,lineNumber))
         #print(lineNumber)
         lineNumber = lineNumber + 1 
   

#filling up the sensor reading for the second robot
with open('t2.csv',mode = 'r') as file:
    csvFile= csv.reader(file)
    lineNumber = 1
    for lines in csvFile:
        x = lines[0]
        y = lines[1]
        cursor.execute("INSERT into Sensor_Reading (robot_id,x,y,timestamp) VALUES (?,?,?,?)",(2,x,y,lineNumber))
        #print(lineNumber)
        lineNumber = lineNumber + 1 
    
# filling table for third 
with open('t3.csv',mode = 'r') as file:
    csvFile= csv.reader(file)
    lineNumber = 1
    for lines in csvFile:
        x = lines[0]
        y = lines[1]
        cursor.execute("INSERT into Sensor_Reading (robot_id,x,y,timestamp) VALUES (?,?,?,?)",(3,x,y,lineNumber))
        #print(lineNumber)
        lineNumber = lineNumber + 1 

#filling up table for fourth robot  
with open('t4.csv',mode = 'r') as file:
    csvFile= csv.reader(file)
    lineNumber = 1
    for lines in csvFile:
        x = lines[0]
        y = lines[1]
        cursor.execute("INSERT into Sensor_Reading (robot_id,x,y,timestamp) VALUES (?,?,?,?)",(4,x,y,lineNumber))
        #print(lineNumber)
        lineNumber = lineNumber + 1 

# finally for the 5th robot 
with open('t5.csv',mode = 'r') as file:
    csvFile= csv.reader(file)
    lineNumber = 1
    for lines in csvFile:
        x = lines[0]
        y = lines[1]
        cursor.execute("INSERT into Sensor_Reading (robot_id,x,y,timestamp) VALUES (?,?,?,?)",(5,x,y,lineNumber))
        #print(lineNumber)
        lineNumber = lineNumber + 1 
 

#displaying the results 
#printing the whole table out 
cursor.execute("SELECT * FROM Sensor_Reading")
rows = cursor.fetchall()

for row in rows:
    print(row)


#saving the rows
connection.commit()
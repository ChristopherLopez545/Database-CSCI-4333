# this file is used for task 3 and 4
import sqlite3
connection = sqlite3.connect("robots.db")
cursor = connection.cursor()

#the sql statement to find the max x and min x for each robot 
statement = '''
SELECT name,
       MAX(sr.x) AS max_x,
       MIN(sr.x) AS min_x
FROM Robots AS ro
JOIN Sensor_Reading AS sr
  ON ro.id = sr.robot_id
GROUP BY ro.name;
'''

#printing out the table 
res = cursor.execute(statement)
relational_schema = [x[0] for x in res.description]

print(relational_schema)
print("----------------------------------")
for x in res:
    print(x)


#now for the y values 
statement = '''
SELECT name,
       MAX(sr.y) AS max_y,
       MIN(sr.y) AS min_y
FROM Robots AS ro
JOIN Sensor_Reading AS sr
  ON ro.id = sr.robot_id
GROUP BY ro.name;
'''

print("\n")

#print the results
res = cursor.execute(statement)
relational_schema = [x[0] for x in res.description]

print(relational_schema)
print("----------------------------------")
for x in res:
    print(x)



#task 4 

statement= '''
SELECT DISTINCT
  MIN(sr1.x, sr2.x) AS x_min,
  MAX(sr1.x, sr2.x) AS x_max,
  MIN(sr1.y, sr2.y) AS y_min,
  MAX(sr1.y, sr2.y) AS y_max
FROM Sensor_Reading sr1
JOIN Sensor_Reading sr2
  ON sr1.timestamp = sr2.timestamp
WHERE sr1.robot_id = (SELECT id FROM Robots WHERE name='Astro')
  AND sr2.robot_id = (SELECT id FROM Robots WHERE name='IamHuman')
  AND ABS(sr1.x - sr2.x) < 1
  AND ABS(sr1.y - sr2.y) < 1;
'''


#printing the result 
print("\n")
print("The Regions that Astro and IamHuman are closed with each other")
#print the results
res = cursor.execute(statement)
relational_schema = [x[0] for x in res.description]

print(relational_schema)
print("----------------------------------")
for x in res:
    print(x)


# task 4.2 

statement = '''
SELECT COUNT(DISTINCT sr1.timestamp) AS seconds_close
FROM Sensor_Reading sr1
JOIN Sensor_Reading sr2
  ON sr1.timestamp = sr2.timestamp
WHERE sr1.robot_id = (SELECT id FROM Robots WHERE name = 'Astro')
  AND sr2.robot_id = (SELECT id FROM Robots WHERE name = 'IamHuman')
  AND ABS(sr1.x - sr2.x) < 1
  AND ABS(sr1.y - sr2.y) < 1;
'''


#printing the result 
print("\n")
print("How many seconds they are close with each other")
#print the results
res = cursor.execute(statement)
relational_schema = [x[0] for x in res.description]

print(relational_schema)
print("----------------------------------")
for x in res:
    print(x)


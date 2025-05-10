# CS-121_Laboratory_Activity_Group-Sensor
Project Title: Classroom of the Sensors
python file sensor.py contains the source code of our group system
pdf file UML_Class_Diagram.pdf contains the Class Diagram for our program

Members:
Bernardo, Xiamara (N/A)
Donatos, Trixter Lanz (Grizzly-val)
Ilao, Kent Patrick (eequen)
Laganzon, Adrian (DIAN0402)

Program overview:
This is a program features multiple sensors that inherit from the Parent Sensor Class. The Sensor class has the attributes; (1) type for the type of sensor a sensor is, (2) unit for the unit number or the identification number of a specific sensor, (3) current reading for the current reading of a specific sensor. Our team created a subclass sensor of Proximity Sensor, Soil Sensor, Color Sensor, and RFID Sensor. Thus, the current reading can be distance(centimeter), moisture level(%), color(r/g/b), and signal(dB). You can display details of each sensors using the method display_details() which is an abstract method of the Parent class. The function display_status() is an abstract method in the parent class, so the user has the option to display the status of any of the sensors available.

How to run the program?
1. Upon Starting the program, the user will be asked to pick which type of sensor to check (Proximity, soil, color, or rfid sensor, or choices 1 to 4 respectively.).
2. After selecting the type of sensor, the user can then choose one from the multiple sensors of the selected type of sensor. Each sensor stores/processes different information.
3. Lastly, after a specific sensor has been selected, the user can then select which process(method), the sensor will do.
This program is written with error handling so unexpected inputs such as wrong int inputs, string, and blank inputs will not lead to errors.

This program is a collaborative project among our team's group members. Each subclass was created and conditioned for the parent class that was created at the start of this program's creation. Each member deserves an acknowledgement as this project wouldn't have seen its completion without our individual and group effort. It is understood by our group that this project was assigned to us by our professor to apply and improve our newly acquired knowledge which is Python Object-Oriented Programming. Additionally, our group would like to mention Lucidchart, the tool we used to create the UML Class Diagram for our system with ease.

CS-1202
Group 4: Sensor
Professor: John Richard Esguerra

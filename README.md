# CS-121 Laboratory Activity: Sensor Group  
**Project Title:** Sensor Classes

This repository contains the files for our group project:  
- `sensor.py` — Python source code implementing the sensor system.  
- `UML_Class_Diagram.pdf` — UML Class Diagram representing the class structure of the system.

---

## 👥 Group Members
- Bernardo, Xiamara *(N/A)*
- Donatos, Trixter Lanz *(Grizzly-val)*
- Ilao, Kent Patrick *(eequen)*
- Laganzon, Adrian *(DIAN0402)*

---

## 📘 Program Overview

This program features **multiple sensors**, each inheriting from a **parent `Sensor` class**. The parent class includes the following attributes:
1. `type` – Type of the sensor  
2. `unit` – Unit number or sensor ID  
3. `current_reading` – The current value or reading of the sensor  

We created **four sensor subclasses**:
- **ProximitySensor** – Measures distance in centimeters  
- **SoilSensor** – Measures moisture level in percentage (%)  
- **ColorSensor** – Detects color using RGB values  
- **RFIDSensor** – Measures signal strength in decibels (dB)  

Each sensor implements:
- `display_status()` – An abstract method that lets the user check the sensor's status

The program includes **robust error handling** for unexpected or invalid inputs (e.g., incorrect numbers, strings, blank input).

---

## ▶️ How to Run the Program
### Option A: Download `sensor.py` from our repository and run it in an IDE in your computer
### Option B: Copy and paste the code from `sensor.py` into an online Python compiler like Replit or Programiz (no download needed)
## Using the Program
1. **Run `sensor.py`.**  
2. **Choose a sensor type:**  
   - 1 — Proximity Sensor  
   - 2 — Soil Sensor  
   - 3 — Color Sensor  
   - 4 — RFID Sensor  

3. **Select a specific sensor** from the chosen type. Each sensor stores unique data.

4. **Choose a method** (e.g., `display_details()` or `display_status()`) to execute and view sensor output.

---

## 🤝 Acknowledgments

This program is a collaborative project among our team's group members. Each subclass was created and conditioned for the parent class that was created at the start of this program's creation. Each member deserves an acknowledgement as this project wouldn't have seen its completion without our individual and group effort. It is understood by our group that this project was assigned to us by our professor to apply and improve our newly acquired knowledge which is Python Object-Oriented Programming. Additionally, our group would like to mention ***Lucidchart***, the tool we used to create the UML Class Diagram for our system with ease.

---

## 🧑‍🏫 Course Information

- **Course Code:** CS-1202  
- **Group:** Group 4 – Sensor  
- **Professor:** John Richard Esguerra

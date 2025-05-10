from abc import ABC, abstractmethod

class Sensor:
    def __init__(self, type, unit, current_reading):
        self.type = type
        self.__unit = unit                          #   # : Private Attribute. Not meant to be directly accessed.
        self._current_reading = current_reading     #   - :  Protected Attribute. Can be directly accessed, but labeled as protected.
    
    @property
    def get_unit(self):
        return self.__unit
    
    @get_unit.setter
    def set_new_unit(self, new_unit):
        self.__unit = new_unit
        
    
    @abstractmethod
    def display_status(self):
        pass

# Sublcass Donatos
class Proximity_Sensor(Sensor):
    def __init__(self, unit_number, distance_reading, presence):
        super().__init__("Proximity Sensor", unit_number, distance_reading)
        self.presence = presence

    @property
    def get_distance(self):
        return self._current_reading
    
    @property
    def get_meter_distance(self):
        return self.get_distance / 100

    def display_status(self):
        print("=============================================")
        print(f"{self.type}\nUnit Number: {self.get_unit}\nObject Detected: {self.presence}")
        if self.presence == True:
            print(f"Distance: {self.get_distance}cm")
        else:
            print(f"Distance: N/A")
        print("=============================================")

    def check_distance(self):
        minimum_distance = 20 # cm
        if self.presence == True:
            if self.get_distance <= minimum_distance:
                print(f"Object too close!")
            else:
                print(f"Object is {self.get_distance - minimum_distance}cm away from the minimum distance ({self.get_distance}cm)")
        else:
            print("No object within proximity")


 # Subclass Ilao
class SoilSensor(Sensor):
    def __init__(self, location, moisture_level, temperature, ph_level):
        super().__init__("Soil Sensor", "%", moisture_level)
        self.location = location
        self.temperature = temperature  # °C
        self.ph_level = ph_level  # pH scale

    def read_data(self, moisture, temperature, ph):
        """Update the sensor readings."""
        self._current_reading = moisture
        self.temperature = temperature
        self.ph_level = ph

    def display_status(self):
        print("=============================================")
        print(f"{self.type}\nLocation: {self.location}")
        print(f"Moisture: {self._current_reading}% ({self.moisture_status})")
        print(f"Temperature: {self.temperature}°C ({self.temperature_status})")
        print(f"pH Level: {self.ph_level}")
        print("=============================================")

    def check_soil_health(self):
        """Evaluates whether soil conditions are within optimal ranges."""
        if self._current_reading < 30:
            print("Warning: Soil is too dry!")
        elif self._current_reading > 70:
            print("Warning: Soil is too wet!")
        else:
            print("Soil moisture is within the optimal range.")

    @property
    def moisture_status(self):
        """Returns a descriptive moisture condition."""
        if self._current_reading < 30:
            return "Dry"
        elif self._current_reading > 70:
            return "Too Wet"
        else:
            return "Optimal"

    @property
    def temperature_status(self):
        """Returns a descriptive temperature condition."""
        if self.temperature < 10:
            return "Cold"
        elif self.temperature > 35:
            return "Hot"
        else:
            return "Moderate"


# Subclass Bernardo
class Color_Sensor(Sensor):
    def __init__(self, unit_number, color_detected, rgb_values):
        super().__init__("Color_Sensor", unit_number, color_detected)
        self.__rgb_values = rgb_values            

    @property
    def color(self):
        return self._current_reading

    @property
    def rgb_values(self):
        return self.__rgb_values
  
    def display_status(self):
        print("========================================")
        print(f"Unit Number: {self.get_unit}")
        print(f"Detected Color: {self.color}")
        print(f"RGB Values: {self.rgb_values}")
        print("========================================")
    
    def is_primary_color(self):
        primary_colors = {"Red", "Green", "Blue"}
        if self.color.capitalize() in primary_colors:
            print(f"{self.color} is a primary color.")
        else:
            print(f"{self.color} is not a primary color.")

# Subclass Laganzon
class RFID_Sensor(Sensor):
    def __init__(self, unit_number, tag_id, signal_strength):
        super().__init__("RFID Sensor", unit_number, tag_id)
        self.signal_strength = signal_strength  
        self.__tag_id = tag_id  

    @property
    def tag_id(self):
        return self.__tag_id

    @tag_id.setter
    def tag_id(self, new_tag_id):
        self.__tag_id = new_tag_id

    @property
    def signal_strength_status(self):
        if self.signal_strength < -80:
            return "Signal is Weak"
        elif self.signal_strength > -30:
            return "Signal is strong"
        else:
            return "Signal is moderate"

    def display_status(self):
        print("=" * 45)
        print(f"{self.type}\nUnit Number: {self.get_unit}\nRFID Tag ID: {self.tag_id}")
        print(f"Signal Strength: {self.signal_strength} dB ({self.signal_strength_status})")
        print("=" * 45)

    def check_tag_readability(self):
        if self.signal_strength < -80:
            print("Warning: Signal strength is too weak, tag may not be readable.")
        elif self.signal_strength > -30:
            print("RFID tag is easily readable.")
        else:
            print("RFID tag is moderately readable.")





proxy1 = Proximity_Sensor("PROX0001", 19, True)
proxy2 = Proximity_Sensor("PROX1251", 285, True)
proxy3 = Proximity_Sensor("PROX3661", 0, False)
soil1 = SoilSensor("Garden", 45, 22, 6.5)
soil2 = SoilSensor("Backyard", 42, 20, 6.3)
color1 = Color_Sensor("CS-1202", "Orange", {"R": 255, "G": 165, "B": 0})
color2 = Color_Sensor("CS-1203", "Blue", {"R": 0, "G": 255, "B": 255})
rfid1 = RFID_Sensor("RFID-001", "TAG123456789", -55)
rfid2 = RFID_Sensor("RFID-002", "TAG987654321", -27)





def proximity_sensor1():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check Distance\n3. Convert to Meters")
        try:
            choice_function = int(input("Pick from 1 to 3 (0 to return): "))
            if choice_function not in [0, 1, 2, 3]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        print()
                        proxy1.display_status()
                        print()
                    case 2:
                        print()
                        proxy1.check_distance()
                        print()
                    case 3:
                        print()
                        print(f"Distance in meters({proxy1.get_distance}cm): {proxy1.get_meter_distance}m")
                        print()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print()
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")

def proximity_sensor2():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check Distance\n3. Convert to Meters")
        try:
            choice_function = int(input("Pick from 1 to 3 (0 to return): "))
            if choice_function not in [0, 1, 2, 3]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        print()
                        proxy2.display_status()
                        print()
                    case 2:
                        print()
                        proxy2.check_distance()
                        print()
                    case 3:
                        print()
                        print(f"Distance in meters({proxy2.get_distance}cm): {proxy2.get_meter_distance}m")
                        print()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print()
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")
    
def proximity_sensor3():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check Distance\n3. Convert to Meters")
        try:
            choice_function = int(input("Pick from 1 to 3 (0 to return): "))
            if choice_function not in [0, 1, 2, 3]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        proxy3.display_status()
                    case 2:
                        proxy3.check_distance()
                    case 3:
                        print(f"Distance in meters({proxy3.get_distance}cm): {proxy3.get_meter_distance}m")
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")

def choose_proximity_sensor():
    while True:
        try:
            print("\nWhich proximity sensor would you like to check?")
            print("Proximity Sensor 1\nProximity Sensor 2\nProximity Sensor 3")
            choose_prox = int(input("Pick from 1 to 3 (0 to return): "))
            if choose_prox not in [0, 1, 2, 3]:
                raise ValueError("Invalid Input")
            else:
                match choose_prox:
                    case 1:
                        print()
                        proximity_sensor1()
                    case 2:
                        print()
                        proximity_sensor2()
                    case 3:
                        print()
                        proximity_sensor3()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print()
            print(e)
            print("Please enter a Valid Input")

def soil_sensor1():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check Soil Health\n3. Check Moisture Status\n4. Check Temperature Status")
        try:
            choice_function = int(input("Pick from 1 to 4 (0 to return): "))
            if choice_function not in [0, 1, 2, 3, 4]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        print()
                        soil1.display_status()
                        print()
                    case 2:
                        print()
                        soil1.check_soil_health()
                        print()
                    case 3:
                        print()
                        print(soil1.moisture_status)
                        print()
                    case 4:
                        print()
                        print(soil1.temperature_status)
                        print()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")

def soil_sensor2():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check Soil Health\n3. Check Moisture Status\n4. Check Temperature Status")
        try:
            choice_function = int(input("Pick from 1 to 4 (0 to return): "))
            if choice_function not in [0, 1, 2, 3, 4]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        print()
                        soil2.display_status()
                        print()
                    case 2:
                        print()
                        soil2.check_soil_health()
                        print()
                    case 3:
                        print()
                        print(soil2.moisture_status)
                        print()
                    case 4:
                        print()
                        print(soil2.temperature_status)
                        print()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")

def choose_soil_sensor():
    while True:
        try:
            print("\nWhich soil sensor would you like to check?")
            print("Soil Sensor 1\nSoil Sensor 2")
            choose_prox = int(input("Pick from 1 to 2 (0 to return): "))
            if choose_prox not in [0, 1, 2]:
                raise ValueError("Invalid Input")
            else:
                match choose_prox:
                    case 1:
                        print()
                        soil_sensor1()
                    case 2:
                        print()
                        soil_sensor2()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print()
            print(e)
            print("Please enter a Valid Input")

def color_sensor1():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check if Primary Color")
        try:
            choice_function = int(input("Pick from 1 to 2 (0 to return): "))
            if choice_function not in [0, 1, 2]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        print()
                        color1.display_status()
                        print()
                    case 2:
                        print()
                        color1.is_primary_color()
                        print()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print()
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")

def color_sensor2():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check if Primary Color")
        try:
            choice_function = int(input("Pick from 1 to 2 (0 to return): "))
            if choice_function not in [0, 1, 2]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        print()
                        color2.display_status()
                        print()
                    case 2:
                        print()
                        color2.is_primary_color()
                        print()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print()
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")

def choose_color_sensor():
    while True:
        try:
            print("\nWhich color sensor would you like to check?")
            print("Color Sensor 1\nColor Sensor 2")
            choose_prox = int(input("Pick from 1 to 2 (0 to return): "))
            if choose_prox not in [0, 1, 2]:
                raise ValueError("Invalid Input")
            else:
                match choose_prox:
                    case 1:
                        print()
                        color_sensor1()
                    case 2:
                        print()
                        color_sensor2()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print()
            print(e)
            print("Please enter a Valid Input")

def rfid_sensor1():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check Signal Strength Status\n3. Check Tag Readability")
        try:
            choice_function = int(input("Pick from 1 to 3 (0 to return): "))
            if choice_function not in [0, 1, 2, 3]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        print()
                        rfid1.display_status()
                        print()
                    case 2:
                        print()
                        print(rfid1.signal_strength_status)
                        print()
                    case 3:
                        print()
                        rfid1.check_tag_readability()
                        print()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")

def rfid_sensor2():
    while True:
        print("Sensor functions:")
        print("1. Display Details\n2. Check Signal Strength Status\n3. Check Tag Readability")
        try:
            choice_function = int(input("Pick from 1 to 3 (0 to return): "))
            if choice_function not in [0, 1, 2, 3]:
                raise ValueError("Invalid Input")
            else:
                match choice_function:
                    case 1:
                        print()
                        rfid2.display_status()
                        print()
                    case 2:
                        print()
                        print(rfid2.signal_strength_status)
                        print()
                    case 3:
                        print()
                        rfid2.check_tag_readability()
                        print()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print
            print(e)
            print("Please enter a Valid Input")
    print("Sending you back...\n")

def choose_rfid_sensor():
    while True:
        try:
            print("\nWhich RFID sensor would you like to check?")
            print("RFID Sensor 1\nRFID Sensor 2")
            choose = int(input("Pick from 1 to 2 (0 to return): "))
            if choose not in [0, 1, 2]:
                raise ValueError("Invalid Input")
            else:
                match choose:
                    case 1:
                        print()
                        rfid_sensor1()
                    case 2:
                        print()
                        rfid_sensor2()
                    case 0:
                        print("Returning...")
                        break
        except ValueError as e:
            print()
            print(e)
            print("Please enter a Valid Input")

while True:
    try:
        print("Which sensor would you like to check?")
        print("1. Proximity Sensor\n2. Soil Sensor\n3. Color Sensor\n4. RFID Sensor")
        choice = int(input("Pick from 1 to 4 (0 to exit): "))
        if choice not in [0, 1, 2, 3, 4]:
            raise ValueError("Invalid Input")
        else:
            match choice:
                case 1:
                    choose_proximity_sensor()
                case 2:
                    choose_soil_sensor()
                case 3:
                    choose_color_sensor()
                case 4:
                    choose_rfid_sensor()
                case 0:
                    print("Exiting...")
                    break
    except ValueError as e:
        print()
        print(e)
        print("Please enter a Valid Input")
        print()

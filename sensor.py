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
                print(f"Object is {self.get_distance - minimum_distance}cm away from the minimum distance ({self.get_distance})")
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


print("TESTING PROXIMITY SENSOR")
proxy1 = Proximity_Sensor("PROX0001", 34, True)
proxy1.display_status()
proxy1.check_distance()
proxy1.set_new_unit = "PROX0002"
proxy1.display_status()

print()

print("TESTING SOIL SENSOR")
soil_sensor = SoilSensor("Garden", 45, 22, 6.5)
soil_sensor.display_status()
soil_sensor.check_soil_health()

print()

print("TESTING COLOR SENSOR")
sensor = Color_Sensor("CS-1202", "Orange", {"R": 255, "G": 165, "B": 0})
sensor.display_status()
sensor.is_primary_color()

print("TESTING RFID SENSOR")
rfid_sensor = RFID_Sensor("RFID-001", "TAG123456789", -55)
rfid_sensor.display_status()
rfid_sensor.check_tag_readability()


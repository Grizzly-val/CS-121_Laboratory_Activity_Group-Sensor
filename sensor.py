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
    def get_m_distance(self):
        return self.get_distance / 100

    def display_status(self):
        print("=============================================")
        print(f"{self.type}\nUnit Number: {self.get_unit}\nObject Detected: {self.presence}")
        if self.presence == True:
            print(f"Distance: {self.get_distance}cm")
        else:
            print(f"Distance: N/A")
        print("=============================================")

    def is_too_close(self):
        minimum_distance = 20 # cm
        if self.presence == True:
            if self.get_distance <= minimum_distance:
                print(f"Object too close!")
            else:
                print(f"Object is {self.get_distance - minimum_distance}cm away from the minimum distance")
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

proxy1 = Proximity_Sensor("ILYBBM", 34, True)
proxy1.display_status()
proxy1.is_too_close()
proxy1.set_new_unit = "HAHAHA"
proxy1.display_status()


soil_sensor = SoilSensor("Garden", 45, 22, 6.5)
soil_sensor.display_status()
soil_sensor.check_soil_health()


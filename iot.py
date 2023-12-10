import machine
import time
import urequests
from machine import Pin
from dht import DHT11, InvalidChecksum
import utime


dht_pin = Pin(0, Pin.IN)
data_dht = DHT11(dht_pin)


analog_pin = machine.ADC(22)


def categorize_pm_level(concentration):
    if concentration < 50:
        return "Good"
    elif 50 <= concentration < 100:
        return "Moderate"
    elif 100 <= concentration < 150:
        return "Unhealthy for Sensitive Groups"
    elif 150 <= concentration < 200:
        return "Unhealthy"
    elif 200 <= concentration < 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


while True:
    
    data_dht.measure()
    temperature = data_dht.temperature()
    humidity = data_dht.humidity()
    
    sensor_value = analog_pin.read_u16()
    pm_concentration = 120  
    
   
    url = "YOUR_SERVER_ENDPOINT"  
    headers = {'Content-Type': 'application/json'}
    payload = {
        'temperature': temperature,
        'humidity': humidity,
        'sensor_value': sensor_value,
        'pm_concentration': pm_concentration
    }
    
    response = urequests.post(url, json=payload, headers=headers)
    
    
    pm_level = categorize_pm_level(pm_concentration)
    print(f"Temperature: {temperature}°C, Humidity: {humidity}%, PM Level: {pm_level}")

    
    time.sleep(60)  
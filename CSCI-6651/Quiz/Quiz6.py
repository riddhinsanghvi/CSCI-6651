#Create a LabList of atleast 3 devices.

LabList = [
    {"Device_ID":"A12","Sensor A Type": "Pressure","Sensor A Readings":[0.0,1.1,2.2], "Sensor A Units":"kPa", "Sensor B Type": "Temperature","Sensor B Readings":[92.0,71.1,62.2], "Sensor B Units":"Degree fahrenheit"},
   { "Device_ID":"A13","Sensor A Type": "Gas","Sensor A Readings":[10.0,12.1,32.2], "Sensor A Units":"Amount of Co2","Sensor B Type": "Pressure","Sensor B Readings":[10.0,15.1,23.2], "Sensor B Units":"kPa"},
{"Device_ID":"A14","Sensor A Type": "Temperature","Sensor A Readings":[32.0,45.1,72.2], "Sensor A Units":"Degree Celcius", "Sensor B Type": "Gas","Sensor B Readings":[20.0,16.1,39.2], "Sensor B Units":"Amount of Co2"}
]

#Calling Lablist and iterating it over the dict and calling it labSummaryDict
labSummaryDict={}
for device in LabList:
    device_id = device["Device_ID"]

    for sensor_label in ["A", "B"]:
            sensor_type = device[f"Sensor {sensor_label} Type"]
            readings = device[f"Sensor {sensor_label} Readings"]
            units = device[f"Sensor {sensor_label} Units"]

            avg_reading = sum(readings) / len(readings) if readings else 0
            labSummaryDict.setdefault(device_id, []).append(
                (sensor_type, avg_reading, len(readings), units)
)

print(f"{'Device ID':<15}{'Device Type':<25}{'Average Reading':<25}{'Number of Points':<20}{'Units'}")
print("-" * 100)

for device_id, sensors in labSummaryDict.items():
    for sensor in sensors:
        sensor_type, avg, num_points, units = sensor
        print(f"{device_id:<15}{sensor_type:<25}{avg:<25.2f}{num_points:<20}{units}")

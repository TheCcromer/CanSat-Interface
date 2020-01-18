import csv
import numpy as np
import time

if __name__ == '__main__':
    fieldnames = [
                'TEAM ID',
                'MISSION TIME',
                'PACKET COUNT',
                'ALTITUDE',
                'PRESSURE',
                'TEMP',
                'VOLTAGE',
                'GPS TIME',
                'GPS LATITUDE',
                'GPS LONGITUDE',
                'GPS ALTITUDE',
                'GPS SATS',
                'AIR SPEED',
                'SOFTWARE STATE',
                'PARTICLE COUNT'
                ]
    with open('data.csv', mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    
    team_id = 4444
    mission_time = 0
    packet_count = 0
    software_state = 'mocked'
    while True:
        print("ok")
        data = {
                'TEAM ID': team_id,
                'MISSION TIME': mission_time,
                'PACKET COUNT': packet_count,
                'ALTITUDE': np.random.randint(100),
                'PRESSURE': np.random.randint(100),
                'TEMP': np.random.randint(100),
                'VOLTAGE': np.random.randint(100),
                'GPS TIME': np.random.randint(100),
                'GPS LATITUDE': np.random.randint(100),
                'GPS LONGITUDE': np.random.randint(100),
                'GPS ALTITUDE': np.random.randint(100),
                'GPS SATS': np.random.randint(100),
                'AIR SPEED': np.random.randint(100),
                'SOFTWARE STATE': software_state,
                'PARTICLE COUNT': np.random.randint(100)
                }
        with open('data.csv', mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(data)
            time.sleep(1)
        mission_time += 1
        packet_count += 1
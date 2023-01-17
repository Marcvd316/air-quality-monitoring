import time
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE # https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/breakout_bme68x
from pimoroni_i2c import PimoroniI2C

i2c = PimoroniI2C(sda=0, scl=1)
sensor = BreakoutBME68X(i2c)


def collect_data():
    heater = "Unstable" # This ensures the while loop below runs at least twice on execution, to ensure the heater can stabilize

    while heater is "Unstable":
        # Gather data
        temperature, pressure, humidity, gas, status, _, _ = sensor.read()
        heater = "Stable" if status & STATUS_HEATER_STABLE else "Unstable"

        # Print raw one-liner
        #print("{:0.2f}c, {:0.2f}Pa, {:0.2f}%, {:0.2f} Ohms, Heater: {}".format(temperature, pressure, humidity, gas, heater))
        
        # Print one value per line with adjusted measures
        print("Temperature:", "{:0.2f}C".format(temperature))
        print("Pressure:", "{:0.2f}kPa".format(pressure/1000))
        print("Humidity:", "{:0.2f}%".format(humidity))
        print("Gas:", "{:0.2f} kOhms".format(gas/1000))
        print("CO2 equivalent: {:.2f} ppm".format(gas/56.1))
        print("Heater:", heater)

        # Send to InfluxDB
        #influxdb.send_data()

        #################

        time.sleep(3)
from fastmcp import FastMCP,Context,exceptions
from read_DHT11 import DHT11Sensor
import board
# Create a server instance
mcp = FastMCP(name="Temperature and Humidity Sensor")
dht_sensor = DHT11Sensor(board.D23)
@mcp.resource(
    uri="sensor://temperature_and_humidity",
    name="Temperature and Humidity Sensor",
    description="Provides temperature and humidity data"
)
def get_temp_and_humidity(ctx: Context) -> dict:
    try:
        tempraure, humidity = dht_sensor.get_data()
        return {"temperature_celsius": tempraure, "humidity_percent": humidity}
    except:
        raise exceptions.ResourceError("Failed to read temperature and humidity data")
if __name__ == "__main__":
    mcp.run()
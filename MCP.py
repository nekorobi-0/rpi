import fastapi
import uvicorn
from read_DHT11 import DHT11Sensor
import board
# Create a server instance
app = fastapi.FastAPI(summary="Temperature and Humidity Sensor", description="Provides temperature and humidity data")
dht_sensor = DHT11Sensor(board.D23)
@app.post(
    path="/temperature_and_humidity",
    name="Temperature and Humidity Sensor",
    description="Provides temperature and humidity data"
)
def get_temp_and_humidity() -> dict:
    tempraure, humidity = dht_sensor.get_data()
    return {"temperature_celsius": tempraure, "humidity_percent": humidity}
if __name__ == "__main__":
    
    uvicorn.run(host="192.168.0.236",port=8000, app=app)
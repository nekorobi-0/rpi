import time
import board
import adafruit_dht

# センサーの初期化
# 使用するピンを board.D<GPIO番号> で指定します
# 今回はGPIO 4に接続したので board.D4 を指定

print("DHT11センサーから温湿度を読み取ります (Ctrl+Cで終了)")

class DHT11Sensor:
    def __init__(self, pin):
        self.dht_device = adafruit_dht.DHT11(pin)

    def get_data(self) -> tuple[float, int]:
        while True:
            try:
                temperature_c = self.dht_device.temperature
                humidity = self.dht_device.humidity
                return float(temperature_c), int(humidity)
            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                self.dht_device.exit()
                raise error


# クラスのインスタンスを作成
if __name__ == "__main__":
    dht_sensor = DHT11Sensor(board.D23)
    while True:
        temperature, humidity = dht_sensor.get_data()
        print(f"温度: {temperature:.1f} C, 湿度: {humidity}%")
        time.sleep(2.0)

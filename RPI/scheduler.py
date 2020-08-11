import schedule
from  time import sleep
from backend_GPIO import RELAY, DHT_SENSOR, READ_CPU_TEMP
import logging

logging.basicConfig(filename='rega.log', filemode='w', format='%(asctime)s: %(name)s - %(levelname)s - %(message)s')

relay1=RELAY(14,"relay1")
relay2=RELAY(15,"relay2")
relay3=RELAY(18,"relay3")
relay4=RELAY(23,"relay3") #fan started


schedle().every().day().at('19:00').do(relay1.start).tag(relay1.name)
schedle().every().day().at('19:00').do(relay2.start).tag(relay2.name)
schedle().every().day().at('19:00').do(relay3.start).tag(relay3.name)

schedle().every().day().at('19:00').do(relay1.stop).tag(relay1.name)
schedle().every().day().at('19:00').do(relay2.stop).tag(relay2.name)
schedle().every().day().at('19:00').do(relay3.stop).tag(relay3.name)

cpu=READ_CPU_TEMP()
temp_humd=DHT_SENSOR(10)


while True:
    schedule.run_pending()
    sleep(60)
    if cpu.cpu_temp < 47 :
        print("raspeberry pi too hot")
        relay4.start()
    else:
        relay4.stop()
    cpu.read_cpu_temp()



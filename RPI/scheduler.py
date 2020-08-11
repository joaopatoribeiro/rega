import schedule
from  time import sleep
from backend_GPIO import RELAY, DHT_SENSOR, READ_CPU_TEMP
import logging

logging.basicConfig(filename='rega.log', filemode='w', format='%(asctime)s: %(name)s - %(levelname)s - %(message)s')

relay1=RELAY(14,"relay1")
logging.info ('started relay2')
relay2=RELAY(15,"relay2")
logging.info ('started relay2')
relay3=RELAY(18,"relay3")
logging.info ('started relay4')
relay4=RELAY(23,"relay4") #fan started


schedule.every().day.at('19:00').do(relay1.start).tag(relay1.name)
logging.info ('started relay2')
schedule.every().day.at('19:00').do(relay2.start).tag(relay2.name)
logging.info ('started relay2')
schedule.every().day.at('19:00').do(relay3.start).tag(relay3.name)
logging.info ('started relay2')

schedule.every().day.at('19:00').do(relay1.stop).tag(relay1.name)
schedule.every().day.at('19:00').do(relay2.stop).tag(relay2.name)
schedule.every().day.at('19:00').do(relay3.stop).tag(relay3.name)

cpu=READ_CPU_TEMP()
temp_humd=DHT_SENSOR(2)


while True:
    schedule.run_pending()
    print(temp_humd.read())
    if cpu.cpu_temp > 47.0 :
        print(f"raspeberry pi too hot {cpu.cpu_temp}")
        relay4.start()
    else:
        relay4.stop()
        print(f"raspeberry pi is cool {cpu.cpu_temp}")
    cpu.read_cpu_temp()
    sleep(2)




# print screen every interval in sec

import pyautogui
import configparser
from datetime import datetime
from pathlib import Path
from datetime import datetime, timedelta
import time

config = configparser.RawConfigParser()
with Path(__file__).with_name('config.txt') as f:
	config.read(f)
	details = dict(config.items('DEFAULT'))

interval = int(details['interval'])
times = int(details['times'])

for i in range(times):
	dt = datetime.utcnow() + timedelta(hours=2)
	stime = dt.strftime('%y%m%d.%H%M%S.%f')[:-3]
	file_name = details['path_output'] + stime + '.jpg'
	
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(file_name)
	
	print(i)
	time.sleep(interval)


import requests
from datetime import datetime
from datetime import timezone
from sendSMS import sendSMS
from tpplug import send_cmd
import time
from vault import apikey

def main():
    dt = datetime.now()
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    times = int(timestamp-600)
    api_url = 'https://api.logdna.com/v1/export?from=%i&to=%i&query=PiTemp' % (times,int(timestamp))
    headers = {"servicekey": apikey}
    response = requests.get(api_url,headers=headers)
    x=int(response.text[138:140])
    text = f"Shutting down in 30s due to Pi Temperature: {x} C"
    if int(x) >= 60:
        sendSMS(text)
        time.sleep(30)
        send_cmd('off')

if __name__ == '__main__':
    main()

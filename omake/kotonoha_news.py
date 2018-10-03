import time
import csv
import os

def getcsv(path):
    csvlist = []
    with open(path, 'r') as f:
        reader = list(csv.reader(f))
    return reader

url_list = getcsv("yahoo_log.csv")


if len(url_list) > 0:
    intro = "ことのはゲームニュースのお時間です。最初のニュースはこちらです。"
    cmd = 'seikasay.exe -cid ' + "2000" + ' -speed ' + "1.20" + ' -pitch ' + "0.80" + ' -intonation ' + "1.00" + ' \"' + intro + '\"'
    sps.call(cmd,shell = True)
    for content in url_list:
        time.sleep(3)
        cmd = 'seikasay.exe -cid ' + "2000" + ' -speed ' + "1.20" + ' -pitch ' + "0.80" + ' -intonation ' + "1.00" + ' \"' + content[1] + '\"'
        sps.call(cmd,shell = True)
        time.sleep(2)
        for txt in content[2].split('\n'):
            cmd = 'seikasay.exe -cid ' + "2000" + ' -speed ' + "1.20" + ' -pitch ' + "0.80" + ' -intonation ' + "1.00" + ' \"' + txt + '\"'
            sps.call(cmd,shell = True)
        if content[0] == url_list[-1][0]:
            break
        time.sleep(2)
        intro = "次のニュースです。"
        cmd = 'seikasay.exe -cid ' + "2000" + ' -speed ' + "1.20" + ' -pitch ' + "0.80" + ' -intonation ' + "1.00" + ' \"' + intro + '\"'
        sps.call(cmd,shell = True)
    
    time.sleep(1)
    intro = "ことのはゲームニュースを終わります。"
    cmd = 'seikasay.exe -cid ' + "2000" + ' -speed ' + "1.20" + ' -pitch ' + "0.80" + ' -intonation ' + "1.00" + ' \"' + intro + '\"'
    sps.call(cmd,shell = True)

    os.remove("./yahoo_onetimelog.csv")
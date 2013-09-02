import sys
import time
import multiprocessing
import urllib.request
import subprocess
import re
import os

class NetTest:
    def __init__(self,a):
        self.a = a
        self.aa = 0
    def reporthook(self, count, blockSize, totalSize):
        global startTime
        if count == 0:
            startTime= time.time()
            return
        duration = time.time() - startTime
        progressSize = int(count*blockSize)
        if duration!=0:
            speed = int(progressSize / (1024 * duration ))
            self.aa=speed
            percent = int(count*blockSize*100/totalSize)
            sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" % (percent,progressSize/(1024*1024),speed, duration ))
            sys.stdout.flush()
    def target1(self,url):
        urllib.request.urlretrieve(url, reporthook=self.reporthook)
    def test(self):
        result = []
        for one in self.a:
            response = subprocess.Popen(["ping",one[1]], stdout=subprocess.PIPE)
            for line in response.stdout:
                print(line.decode("gb2312"))
                m=re.search('Average = (\d+ms)', str(line))
                if(m):
                    one.append(m.group(0))        
            proc = subprocess.Popen(["wget","-O","/dev/null",one[2]])
            try:
                outs, errs  = proc.communicate(timeout=10)
                proc.kill()
            #p = multiprocessing.Process(target=self.target1, args=(one[2],))
            #p.start()
            #time.sleep(10)
            #p.terminate()
            ##one.append(sum(self.aa)/len(self.aa))
            #one.append(self.aa)
            #print(self.aa)
            #self.aa = []
        for one in a:
            print(one[0]+'\n'+one[3]+'\n'+one[4]+'\n')
    
if __name__ == '__main__':
    a = [["Linode Fremont","speedtest.fremont.linode.com","http://speedtest.fremont.linode.com/100MB-fremont.bin"],["BuyVM","205.185.112.31","http://speedtest.lv.buyvm.net/100mb.test"]]
    n = NetTest(a)
    n.test()
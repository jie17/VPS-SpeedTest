import ping
import sys, time, urllib
import threading
import subprocess
import multiprocessing,signal

def reporthook(count, blockSize, totalSize):
    global startTime
    if count == 0:
        startTime= time.time()
        return
    duration = time.time() - startTime
    progressSize = int(count*blockSize)
    if duration!=0:
		speed = int(progressSize / (1024 * duration ))
		percent = int(count*blockSize*100/totalSize)

		sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" % (percent,progressSize/(1024*1024),speed, duration ))
		sys.stdout.flush()

a = [["Linode Fremont","speedtest.fremont.linode.com","http://speedtest.fremont.linode.com/100MB-fremont.bin"],["BuyVM","205.185.112.31","http://speedtest.lv.buyvm.net/100mb.test"]]
for one in a:
	times = 10
	all_ = []
	for i in range(1,times):
		delay = ping.Ping(one[1],timeout = 2000).do()
		if delay:
			all_.append(delay)
	print one[0]+'\n'+str(sum(all_)/len(all_))+'ms'+'\n'
	p = multiprocessing.Process(target=urllib.urlretrieve(one[2],reporthook=reporthook))
	p.start()
	#exec_proc = subprocess.Popen(urllib.urlretrieve(one[2],reporthook=reporthook), stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)
	#max_time = 10
	#cur_time = 0.0
	#return_code = 0
	#while cur_time <= max_time:
	#	#if exec_proc.poll() != None:
	#	#	return_code = exec_proc.poll()
	#	#	break
	#	time.sleep(0.1)
	#	cur_time += 0.1
	##if cur_time > max_time:
	p.terminate()
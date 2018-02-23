# -*-coding:utf-8-*-
import threading
import urllib2

class FetchUrls(threading.Thread):
    """

    """
    def __init__(self,urls,output,lock):
        threading.Thread.__init__(self)
        self.urls=urls
        self.output = output
        #self.name = None
        self.lock = lock

    def run(self):
        """
        线程中运行的任务，任务直接放在在这里就可以被执行
        """
        while self.urls:
            url = self.urls.pop()
            req = urllib2.Request(url)
            try:
                d = urllib2.urlopen(req)
            except urllib2.URLError as e:
                print("URL %s failed:%s"%(url,e.reason))
            self.lock.acquire()
            print("lock acquire")
            self.output.write(d.read())
            #self.name = threading.currentThread()
            print('write done by %s' % self.name)
            print('URL %s fetched by %s'%(url,self.name))
            self.lock.release()


def main():
    lock = threading.Lock()
    urls1 = ["https://baidu.com",'http://360.com']
    urls2 = ['http://hao123.com','http://22too.com']
    f = open("output.txt","w+")
    th1 = FetchUrls(urls1,f,lock)
    th2 = FetchUrls(urls2,f,lock)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    f.close()


if __name__ == "__main__":
    main()

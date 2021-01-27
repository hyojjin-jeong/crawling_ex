import urllib.request
import threading
import time

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def downloadImage(imagePath,fileName):
    print("Downloading Image From", imagePath)
    urllib.request.urlretrieve(imagePath,fileName)
    print('Complete Download')

def executeThread(i):
    imageName = "temp/threadimage-"+str(i)+".jpg"
    downloadImage("https://loremflickr.com/320/240/dog",imageName)

def main():
    t0 = time.time()
    
    threads = []

    for i in range(10):
        thread = threading.Thread(target=executeThread,args=(i,))
        threads.append(thread)
        thread.start()

        t1 = time.time()

        totalTime = t1-t0
        print("Total Execution Time {}".format(totalTime))

if __name__ == '__main__':
    main()

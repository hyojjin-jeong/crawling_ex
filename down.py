import urllib.request

opener = urllib.request.build_opener()

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]

urllib.request.install_opener(opener)

def downloadImage(imagePath, fileName):
    print("Downloading Image From", imagePath)
    urllib.request.urlretrieve(imagePath,fileName)

def main():
    for i in range(10):
        imageName = "temp/image-"+str(i)+".jpg"
        downloadImage("https://loremflickr.com/320/240/dog",imageName)

if __name__ == '__main__':
    main()
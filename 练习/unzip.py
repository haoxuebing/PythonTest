import zipfile
import optparse
from threading import Thread
import time
startTime = time.time()

def extractFile(zfile,password):
    try:
        zfile.extractall(pwd=password.encode('utf-8'))
        print(' Found password ' + password + '\n')
        print("spend time is {}".format(time.time()-startTime))
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',help='specify dictionary file')
    (options,args) = parser.parse_args()

    if(options.zname == None ) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        zfile = zipfile.ZipFile(zname)
        passFile = open(dname)
        for line in passFile.readlines():
            password = line.strip('\n')
            t = Thread(target = extractFile,args = (zfile,password))
            t.start()

if __name__ == '__main__':
    main()

# python unzip.py -f ttt.zip -d dic.txt

# 需要压缩时使用传统压缩方式，否者密码对了也解压不了，不知道为啥
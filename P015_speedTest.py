import speedtest
import datetime

def gcdt():
    GCDT = datetime.datetime.now()
    return GCDT


def spdtest():
    GCDT=gcdt()
    print("[{}] Initialization for Upload/Download Speed Test...".format(GCDT))
    server="www.google.com"
    s=speedtest.Speedtest()
    #s.get_servers(server)
    s.get_best_server()
    GCDT = gcdt()
    print("[{}] Calculation for Downloading Speed".format(GCDT)),
    print("= {0:.1f} MBytes".format(s.download()/1024/1024))
    GCDT = gcdt()
    print("[{}] Calculation for Uploading Speed".format(GCDT)),
    print("= {0:.1f} MBytes".format(s.upload()/1024/1024))
    #print (s.results.share())


def main():
    while(1):
        try:
            spdtest()
        except:
            GCDT = gcdt()
            print("[{}] Unable to connect to Internet.:<".format(GCDT))


# script starts here.

main()

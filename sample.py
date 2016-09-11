# -*- coding: utf-8 -*-
import gopro #import gopro.py
import time

if __name__=="__main__":
    camera = gopro.GoproHero4Session()

    #set timeout time of HTTP request (default=5)
    camera.setHttpTimeout(3)
    #check timetou time
    print ("timeout time:%d") % (camera.getHttpTimeout())
    
    #check Gopro's SSID
    ret = camera.getGoproSSID()
    if ret == None:
        print "failed to get gopro ssid "
    else:
        print "Gopro SSID = "+str(ret)

    #to check whether gopro is Recoding
    ret = camera.isRecoding()
    if ret == None:
        print "failed to check recoding"
    else:
        if ret:
            print "Gopro is Reconding "
        else:
            print "Gopro is NOT  Reconding "

    #to check whether batteru is charging
    ret = camera.isBatteryCharging()
    if ret == None:
        print "failed to check is battery charging"
    else:
        if ret:
            print "Battery is charging "
        else:
            print "Battery is NOT charging "

    #to check Gopro's batteru status
    ret = camera.getBatteryStatus()
    if ret == None:
        print "failed to get battery status "
    else:
        print "battery status = "+str(ret)

    #to check whether SD card is inserted
    ret = camera.isSDCardInserted()
    if ret == None:
        print "failed to check is SD card inserted"
    else:
        if ret:
            print "SD Card is Inserted "
        else:
            print "SD Card is NOT Inserted "

    #to check number of remaining photos
    ret = camera.getNumOfRemainingPhotos()
    if ret == None:
        print "failed to get Remaining Photos "
    else:
        print "Num. of Remaining Photos = "+str(ret)

    #to check number of taken photos
    ret = camera.getNumOfTabkenPhotos()
    if ret == None:
        print "failed to get Number of Taken photos "
    else:
        print "Num. of Taken Photos = "+str(ret)

    #update camera status
    ret = camera.updateCameraStatus()
    if ret == None:
        print "faild to get camera status"
    else:
        print "camera status:"
        print ret

    #Turn OFF the shutter
    ret = camera.shutterOff()
    if ret==None:
        print "fail shutter off"
    else:
        print "success shutter off"

    time.sleep(1)

    #get a medialist(when you get a medialist, you must tuen off the shutter.)
    ret = camera.getMediaList()
    if ret == None:
        print "failed to get media list"
    else:
        print "Media list: "
        print ret
        
    #Turn ON the shutter
    ret = camera.shutterOn()
    if ret==None:
        print "fail shutter on"
    else:
        print "success shutter on"
  

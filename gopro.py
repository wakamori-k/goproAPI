# -*- coding: utf-8 -*-
import urllib2
import json
import sys
import time
import socket
from urllib2 import HTTPError

class GoproHero4Session:
    IP = "10.5.5.9" #gopro's ip address
    REQTIMEOUT=5 #time out [sec]
    status = None
    
    def setHttpTimeout(self, time):
        self.REQTIMEOUT = time
        return self.REQTIMEOUT

    def getHttpTimeout(self):
        return self.REQTIMEOUT
        
    def httpRequest(self, addr):
        req = urllib2.Request(addr)
        try:
            response=urllib2.urlopen(req,timeout=self.REQTIMEOUT)
        except urllib2.URLError,e:
            print str(e.reason)+". url error."
            return None
        except socket.timeout,e:
            print str(e.reason)+". socket time out."
            return None
        return response.read()

    def shutterOn(self):
        addr="http://"+self.IP+"/gp/gpControl/command/shutter?p=1"
        return self.httpRequest(addr)

    def shutterOff(self):
        addr="http://"+self.IP+"/gp/gpControl/command/shutter?p=0"
        return self.httpRequest(addr)

    def setCameraStatus(self):
        addr="http://"+self.IP+"/gp/gpControl/status"
        ret =  self.httpRequest(addr)
        if ret == None:
            return None
        else:
            self.status = json.loads(ret,'utf-8')
            return ret

    def updateCameraStatus(self):
        ret = self.setCameraStatus()
        if ret == None:
            return None
        else:
            return ret
        
    def isBatteryCharging(self):
        if self.status == None:
            ret = self.	setCameraStatus()
            if ret == None:
                return None

        if self.status["status"]["2"] == 4:
            return True
        else:
            return False

    def getBatteryStatus(self):
        if self.status == None:
            ret = self.	setCameraStatus()
            if ret == None:
                return None
        return self.status["status"]["2"]

    def isSDCardInserted(self):
        if self.status == None:
            ret = self.	setCameraStatus()
            if ret == None:
                return None
        if self.status["status"]["33"] == 0:
            return True
        elif self.status["status"]["33"] == 2:
            return False
        else:
            return None

    def getNumOfRemainingPhotos(self):
        if self.status == None:
            ret = self.	setCameraStatus()
            if ret == None:
                return None
        return self.status["status"]["34"]

    def getNumOfTabkenPhotos(self):
        if self.status == None:
            ret = self.	setCameraStatus()
            if ret == None:
                return None
        return self.status["status"]["38"]

    def getGoproSSID(self):
        if self.status == None:
            ret = self.	setCameraStatus()
            if ret == None:
                return None
        return self.status["status"]["30"]

    def isRecoding(self):
        if self.status == None:
            ret = self.	setCameraStatus()
            if ret == None:
                return None
        if self.status["status"]["8"] == 1:
            return True
        elif self.status["status"]["8"] == 0:
            return False
        else:
            return None

    def getMediaList(self):
        addr="http://"+self.IP+":8080/gp/gpMediaList"
        return self.httpRequest(addr)
    

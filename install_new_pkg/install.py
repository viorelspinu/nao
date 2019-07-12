import qi
import ftplib
import os




print "Connecting NAOqi session"
app = qi.Application(url='tcp://'+'127.0.0.1'+':9559')
app.start()
session = app.session

print "Installing app"
packagemgr = session.service("PackageManager")
packagemgr.install("/home/nao/robot-language-romanian-nuance-1-2-0.pkg")

print "DONE !"

app.stop()
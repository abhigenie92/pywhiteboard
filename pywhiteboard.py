#!/usr/bin/env python2.7
from twisted.internet import protocol
from twisted.internet import reactor
from pymouse import PyMouse
import os,re,pdb

class ProcessProtocolXinput(protocol.ProcessProtocol):
    def connectionMade(self):
        print "connectionMade!"
    def outReceived(self, data):
        # check if it is motion
        if 'motion' in data:
            # get the x coordinate
            matchObj_x = re.search(r'a\[0\]=(\d+)', data, re.M|re.I)
            # get the y coordinate
            matchObj_y = re.search(r'a\[1\]=(\d+)', data, re.M|re.I)

            #move the mouse
            if matchObj_x and matchObj_y:                
                # transform the x and y coordinates
                raw_x=matchObj_x.group(1)
                xcor=int(round((float(raw_x)/float(white_board_x)) * x_screen))
                # xcor=int(round((float(raw_x-white_board_x_min)/float(white_board_x_diff)) * x_screen))
                raw_y=matchObj_y.group(1)
                ycor=int(round((float(raw_y)/float(white_board_y)) * y_screen)) 
                print(xcor,ycor)
            if matchObj_x:
                raw_x=matchObj_x.group(1)
                xcor=int(round((float(raw_x)/float(white_board_x)) * x_screen))
                print(xcor,m.position()[1])
            if matchObj_y:
                raw_y=matchObj_y.group(1)
                ycor=int(round((float(raw_y)/float(white_board_y)) * y_screen))
                print(m.position()[0],ycor)
        #m.click(x_dim/2, y_dim/2, 1)
    def errReceived(self, data):
        print data
    def inConnectionLost(self):
        pass
    def outConnectionLost(self):
        pass
    def errConnectionLost(self):
        pass
    def processExited(self, reason):
        pass
    def processEnded(self, reason):
        print "processEnded, status %d" % (reason.value.exitCode,)
        print "quitting"
        reactor.stop()

process_protocol_xinput_obj = ProcessProtocolXinput()
m = PyMouse()
#if starts at 0,0 at top-left corner
white_board_x=5000
white_board_y=5000
#else
white_board_x_min=250
white_board_x_max=500
white_board_x_diff=white_board_x_max-white_board_x_min
white_board_y_min=250
white_board_y_max=500
white_board_y_diff=white_board_y_max-white_board_y_min
x_screen, y_screen = m.screen_size()
reactor.spawnProcess(process_protocol_xinput_obj, "xinput", ["xinput","test","14"], env=None)
reactor.run()

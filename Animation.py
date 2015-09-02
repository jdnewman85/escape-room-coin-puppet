#!/usr/bin/python2

import time

def millisecs():
    return int(round(time.time() * 1000))

class Animation:
    #TODO Remove 'actual' time references, and add arguement for it in the position methods
    def __init__(self, positions, times, loop=False):
        self.startTime = 0
        self.positions = positions
        self.times = times
        self.loop = loop

        self.timeLength = 0
        for k,v in enumerate(self.times):
            self.timeLength += v

        self.reset()

    def reset(self):
        self.startTime = millisecs()

    def getPosition(self):
        timeOffset = self.startTime
        curTime = millisecs()

        if self.loop:
            curTime %= self.timeLength
            curTime += self.startTime

        for k,v in enumerate(self.times):
            timeOffset += v
            if curTime < timeOffset:
                return self.positions[k]

    def getPositionInterp(self):
        timeOffset = self.startTime
        curTime = millisecs()

        if self.loop:
            curTime %= self.timeLength
            curTime += self.startTime

        for k,v in enumerate(self.times):
            lastTime = timeOffset
            timeOffset += v
            if curTime < timeOffset:
                #Handle first position with no interp
                if k == 0:
                    return self.positions[0]

                #Else, interpolate
                interp = (curTime-lastTime)/float(timeOffset-lastTime)
                return (self.positions[k]-self.positions[k-1])*interp + self.positions[k-1]

    def done(self):
        return (not self.loop) and (millisecs() >= (self.startTime+self.timeLength))

class Converter:
    #BUG If either start and end are same
    def __init__(self, fStart, fEnd, tStart, tEnd, limit=True):
        self.fStart = fStart
        self.fEnd = fEnd
        self.tStart = tStart
        self.tEnd = tEnd
        self.limit = limit
    
    def convert(self, value):
        interp = (value-self.fStart)/float(self.fEnd-self.fStart)
        if self.limit:
            interp = min(1.0, max(0.0, interp))
        return interp*(self.tEnd-self.tStart) + self.tStart


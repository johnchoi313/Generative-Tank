import rhinoscriptsyntax as rs
import random
import math

#select nothing
rs.Command("SelNone")

#helper to get and assign parts
def makePart(name,group):
    obj = rs.ObjectsByName(name)[0]
    group.append(obj)
    return obj

# turret parts:
turretParts = []
turretPoint = makePart("turretPoint",turretParts)
turretPivot = makePart("turretPivot",turretParts)
barrelPivot = makePart("barrelPivot",turretParts)
barrelStart = makePart("barrelStart",turretParts)
turretHull = makePart("turretHull",turretParts)
topHatch = makePart("topHatch",turretParts)
barrel = makePart("barrel",turretParts)
# hull parts:
hullParts = []
sidePort = makePart("sidePort",hullParts)
hull = makePart("hull",hullParts)
# track parts:
trackParts = []
trackPiece = makePart("trackPiece",trackParts)
trackFront = makePart("trackFront",trackParts)
trackBack = makePart("trackBack",trackParts)
trackMid = makePart("trackMid",trackParts)
sprocketFrontParts = []
sprocketBackParts = []
#Sprocket Parts:
spf = []
for i in range(0,5):
    spf.append(makePart("spf"+str(i),sprocketFrontParts))
sprocketFront = makePart("sprocketFront",sprocketFrontParts)
sprocketFrontPoint = makePart("sprocketFrontPoint",sprocketFrontParts)
spb = []
for i in range(0,5):
    spb.append(makePart("spb"+str(i),sprocketBackParts))
sprocketBack = makePart("sprocketBack",sprocketBackParts)
sprocketBackPoint = makePart("sprocketBackPoint",sprocketBackParts)
#Wheel Parts
wheel = makePart("wheel",trackParts)
wheelPoint = makePart("wheelPoint",trackParts)

#randomize?
randomize = 0
phase = 9;

#turret variables:
barrelLength = 22.4 + random.uniform(-8,8)*randomize
barrelScale = 1.38 + random.uniform(-.5,1)*randomize
barrelCount = 1 + random.randrange(0,3)*randomize
turretScale = 1.22 + random.uniform(-.2,.5)*randomize
#hull variables:
hullHeight = 14.1 + random.uniform(-4,6)*randomize
hullWidth = 19.15 + random.uniform(-8,8)*randomize
hullLength = 36.0 + random.uniform(-12,12)*randomize
portsPerSide = 4 + random.randrange(0,4)*randomize
#track variables:
wheelCount = 4 + random.randrange(-1,5)*randomize
wheelSprocketDistance = 5.36 + random.uniform(-4,4)*randomize
wheelScale = 1.1 + random.uniform(-.5,1)*randomize
sprocketScale = 0.67 + random.uniform(-.5,1)*randomize
suspension = 2.33 + random.uniform(-2,3)*randomize
trackHeight = .68 + random.uniform(-.4,.6)*randomize
trackLength = 1.0 + random.uniform(-.8,.8)*randomize
trackOffset = 0 + phase*.1 + random.uniform(0,trackLength)*randomize
trackCount = 50 + random.randrange(-10,20)*randomize
#color variables
r = 0+random.randrange(0,160)*randomize
g = 45+random.randrange(0,160)*randomize
b = 12+random.randrange(0,160)*randomize
hullColor1 = [r,g,b]
hullColor2 = [r*4/5,g*4/5,b*4/5]
hullColor3 = [r*3/5,g*3/5,b*3/5]
r1 = 12+random.randrange(0,60)*randomize
g1 = 53+random.randrange(0,60)*randomize
b1 = 17+random.randrange(0,60)*randomize
wheelColor = [r1,g1,b1]
trackColor = [r1/2,g1/2,b1/2]

#print variables?
printvars = True
if (printvars):
    #turret variables
    print "barrelLength = "+str(barrelLength)
    print "barrelScale = "+str(barrelScale)
    print "barrelCount = "+str(barrelCount)
    print "turretScale = "+str(turretScale)
    #hull variables
    print "hullHeight = "+str(hullHeight)
    print "hullWidth = "+str(hullWidth)
    print "hullLength = "+str(hullLength)
    print "portsPerSide = "+str(portsPerSide)
    #track variables
    print "wheelCount = "+str(wheelCount)
    print "wheelSprocketDistance = "+str(wheelSprocketDistance)
    print "wheelScale = "+str(wheelScale)
    print "sprocketScale = "+str(sprocketScale)
    print "suspension = "+str(suspension)
    print "trackHeight = "+str(trackHeight) 
    print "trackLength = "+str(trackLength)
    print "trackOffset = "+str(trackOffset)
    print "trackCount = "+str(trackCount)
    #color variables
    print "(r,g,b) = "+str(r)+", "+str(g)+", "+str(b)
    print "(r1,g1,b1) = "+str(r1)+", "+str(g1)+", "+str(b1)

# --- color objects --- #
#hullColor1
for part in turretParts:
    rs.ObjectColor(part,hullColor1)
for part in hullParts:
    rs.ObjectColor(part,hullColor1)
#hullColor2
rs.ObjectColor(turretPivot,hullColor2)
rs.ObjectColor(barrelPivot,hullColor2)
#hullColor3
for part in trackParts:
    rs.ObjectColor(part,hullColor3)
#wheelColor
rs.ObjectColor(sprocketFront,wheelColor)
rs.ObjectColor(sprocketBack,wheelColor)
rs.ObjectColor(wheel,wheelColor)
#trackColor
rs.ObjectColor(trackPiece,trackColor)


# --- control hull --- #
#resize hull (hullLength,hullWidth,hullHeight)
(x,y,z) = [hullLength/36.0,hullWidth/20.0,hullHeight/10.0]
rs.ScaleObject(hullParts,(0,0,0),[x,y,z])
rs.ScaleObject(trackFront,(0,0,0),[x,1,z])
rs.ScaleObject(trackBack,(0,0,0),[x,1,z])
rs.ScaleObject(trackMid,(0,0,0),[x,1,z])
#move track parts to accommodate
rs.MoveObject(trackParts,[0,hullWidth/2.0-10.0,0])
rs.MoveObject(sprocketFrontParts,[0,hullWidth/2.0-10.0,0])
rs.MoveObject(sprocketBackParts,[0,hullWidth/2.0-10.0,0])
#move turret parts to accommodate
rs.MoveObject(turretParts,[0,0,hullHeight-10.0])
#move sprockets to accomodate
rs.MoveObject(sprocketFrontParts,[hullLength/2.0-18.0,0,0])
rs.MoveObject(sprocketBackParts,[-hullLength/2.0+18.0,0,0])
#make ports
if(portsPerSide > 1):
    rs.MoveObject(sidePort,[hullLength*.3,0,0])
    for i in range(1,portsPerSide):
        distance = (hullLength*.6)/(portsPerSide-1)*(-i) 
        rs.CopyObjects(sidePort,[distance,0,0]) 

# --- CONTROL WHEELS --- #
#scale wheels (wheelScale, sprocketScale)
rs.ScaleObject(sprocketFrontParts,sprocketFrontPoint,[sprocketScale,1,sprocketScale])
rs.ScaleObject(sprocketBackParts,sprocketBackPoint,[sprocketScale,1,sprocketScale])
rs.ScaleObject(wheel,wheelPoint,[wheelScale,1,wheelScale])

#move wheels down (suspension)
rs.MoveObject([wheel,wheelPoint],[0,0,-suspension])

#create wheels and curve(wheelCount, wheelSprocketDistance)
trackPoints = []
trackPoints.extend(spf)
sx = hullLength/2.0-wheelSprocketDistance
sy = hullWidth/2.0+2.5
sz = -wheelScale*2.5-suspension
trackPoints.append([sx+wheelSprocketDistance/4.0,sy,sz])
rs.MoveObject([wheel,wheelPoint],[hullLength/2.0-wheelSprocketDistance,0,0])
for i in range(1,wheelCount):
    distance = (hullLength-2.0*wheelSprocketDistance)/(wheelCount-1)*(-i)
    rs.CopyObjects([wheel,wheelPoint],[distance,0,0])
    trackPoints.append([sx + distance,sy,sz]) 
trackPoints.append([-sx-wheelSprocketDistance/4.0,sy,sz])
trackPoints.extend(spb)
trackPoints.append(spf[0])
trackCurve = rs.AddCurve(trackPoints)

# --- control turret --- #
#scale turret
rs.ScaleObject(turretParts,turretPoint,[turretScale,turretScale,turretScale])

#barrel (barrelLength, barrelCount)
rs.ScaleObject(barrel, barrelStart, [barrelLength/20.0,barrelScale,barrelScale])

#make barrels (barrelCount)
if(barrelCount > 1):
    rs.MoveObject(barrel,[0,4,0])
    for i in range(1,barrelCount):
        distance = (8)/(barrelCount-1)*(-i) 
        rs.CopyObjects(barrel,[0,distance,0]) 


#create track pieces (trackCount, trackHeight, trackLength)
rs.ScaleObject(trackPiece,(0,hullWidth/2.0,0), [trackLength,1,trackHeight])
rs.MoveObject(trackPiece,[trackOffset,0,sprocketScale*2.5])

#these commands are not in Rhino Python.
rs.Command("ArrayCrv") # make track along curve.
rs.Command("RunScript") # Set Material Render Colors.
rs.Command("Mirror") # mirror features.

#select all and rotate
rs.Command("SelAll")
all = rs.SelectedObjects()
rs.RotateObjects(all,(0,0,0), math.cos(phase*2.0*math.pi / 10.0)*10, axis = [0,0,1])

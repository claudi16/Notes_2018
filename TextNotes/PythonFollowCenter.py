import maya.cmds as cmds

def CreateLoc():
    sels = cmds.ls(sl=True)
    
    dups = cmds.duplicate(sels, rr=True)
    dups = cmds.polyUnite(dups, ch=True, mergeUVSets=True, centerPivot=True)[0]
    bbox = cmds.xform(dups, boundingBox=True, q=True)

    pivot = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]
    
    #alternatively you can do this: 
    #xPivot = (bbox[0] + bbox[3]) / 2
    #yPivot = (bbox[1] + bbox[4]) / 2
    #zPivot = (bbox[2] + bbox[5]) / 2
    
    cmds.delete(dups, ch=True)
    cmds.delete(dups)
    
    loc = cmds.spaceLocator()[0]
    cmds.xform(loc, translation=pivot, worldSpace=True)
    
CreateLoc()
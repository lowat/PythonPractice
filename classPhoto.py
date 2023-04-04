def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    return canTakePhoto(redShirtHeights, blueShirtHeights) if redShirtHeights[0] > blueShirtHeights[0] else canTakePhoto(blueShirtHeights, redShirtHeights) 

def canTakePhoto(topRow, bottomRow):
    for i in range(len(topRow)):
        if(bottomRow[i] >= topRow[i]):
            return False;
    return True;
import png

def captureShape(shape):
    emptyRow = [255] * shape[0]
    imagePixels = shape[2]
    shapePixels = []

    for row in imagePixels:
        if(row != emptyRow):
            shapePixels.append(row)
    
    print(len(shapePixels))


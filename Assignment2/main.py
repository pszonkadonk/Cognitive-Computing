import png 
import processShapes       

def main():

    r=png.Reader("shapes/B.png")
    circleA = r.read()

    processShapes.captureShape(circleA)



    # r=png.Reader("shapes/B.png")
    # s = png.Reader("shapes/B.png")
    # circleA = r.read()
    # circleB = s.read()
    # pixelsA = circleA[2]


    # print(type([]))
    # for p in pixelsA:
    #     print(type(p))
    # print(counter)
    # pixelsinA = list(circleA[2])
    # pixelsinB = list(circleB[2])

    # if(pixelsinA == pixelsinB):
    #     print("Its the same")
    # else:
    #     print("Its definitely not the same!")






if __name__ == "__main__":
    main()


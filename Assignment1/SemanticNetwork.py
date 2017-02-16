from RavenObject import RavenObject

class Node:
    def __init__(self, image, name, shapeChange = "", fillChange = "" ):
        self.image = image
        self.name = name
        self.shapeChange = shapeChange
        self.fillChange = fillChange













class SemanticNetwork:
    def __init__(self):
        self.imageRelationship = {}

    
    def createNetwork(imageOne, imageTwo):
        nodeOne = Node(imageOne.image, imageOne.name)
        nodeTwo = Node(imageTwo.image, imageTwo.name)
        
        if(imageOne.shape == imageTwo.shape):
        
        shape relationship and fill relationship


from RavenProblem import RavenObject

"""
A node in a semantic network representing the shape and name of the image (I.E 'Z')
"""

class Node:

    def __init__(self, imageTag, name):
        self.imageTag = imageTag
        self.name = name


class SemanticNetwork:

    def __init__(self, nodeOne, nodeTwo, nameRelationship = None, shapeRelationship = None, fillRelationship = None):
        self.nodeOne = nodeOne
        self.nodeTwo = nodeTwo
        self.nameRelationship = nameRelationship
        self.shapeRelationship = shapeRelationship
        self.fillRelationship = fillRelationship
    
    def createNetwork(imageOne, imageTwo):
        nodeOne = Node(imageOne.imageTag, imageOne.name)
        nodeTwo = Node(imageTwo.imageTag, imageTwo.name)
        nameRelationship = SemanticNetwork.getNameRelationship(imageOne, imageTwo)
        shapeRelationship = SemanticNetwork.getShapeRelationship(imageOne, imageTwo)
        fillRelationship = SemanticNetwork.getFillRelationship(imageOne, imageTwo)

        return SemanticNetwork(nodeOne, nodeTwo, nameRelationship, shapeRelationship, fillRelationship)


    def getNameRelationship(imageOne, imageTwo):
        if(imageOne.name == imageTwo.name):
            return True
        else:
            return False

    def getShapeRelationship(imageOne, imageTwo):
        if(imageOne.shape == imageTwo.shape):
            return True
        else:
            return False
            
    def getFillRelationship(imageOne, imageTwo):
        if(imageOne.fill == imageTwo.fill):
            return True
        else:
            return False

        
            
        


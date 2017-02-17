from SemanticNetwork import SemanticNetwork, Node


"""
Iterate through each of the proposed solutions from Ravens matrices, and establish a semantic network
between image C and each of the proposed solutions.  After creating the network, call compareNetwork to
step by step compare the semantic relationship between the target representation and the goal representation.
Return True and log the correct answer, otherwise return False
"""
def solve(target, imageC, solutions):
    nodeOne = Node(imageC.imageTag, imageC.name)
    goalFound = False

    for key, value in solutions.items():
        nodeTwo = Node(value.imageTag, value.name)
        nameRelationship = SemanticNetwork.getNameRelationship(imageC, value)
        shapeRelationship = SemanticNetwork.getShapeRelationship(imageC, value)
        fillRelationship = SemanticNetwork.getFillRelationship(imageC, value)

        goal = SemanticNetwork(nodeOne, nodeTwo, nameRelationship, shapeRelationship, fillRelationship)

        if(compareNetwork(target, goal)):
            print("I have found the proper image.")
            print("The answer is image #{}".format(goal.nodeTwo.imageTag))
            goalFound = True
            return goalFound
    
    if(goalFound == False):
        print("Sorry, none of the proposed solutions matches the target case")
        
    return goalFound

def compareNetwork(target, goal):
    if(target.nameRelationship == goal.nameRelationship
     and target.shapeRelationship == goal.shapeRelationship
     and target.fillRelationship == goal.fillRelationship):
        return True
    else:
        return False



        
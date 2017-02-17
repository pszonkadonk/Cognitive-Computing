from SemanticNetwork import SemanticNetwork, Node


def solve(target, imageC, solutions):
        nodeOne = Node(imageC.imageTag, imageC.name)

        for key, value in solutions.items():
            nodeTwo = Node(value.imageTag, value.name)
            nameRelationship = SemanticNetwork.getNameRelationship(imageC, value)
            shapeRelationship = SemanticNetwork.getShapeRelationship(imageC, value)
            fillRelationship = SemanticNetwork.getFillRelationship(imageC, value)

            solutionNetwork = SemanticNetwork(nodeOne, nodeTwo, nameRelationship, shapeRelationship, fillRelationship)

            if(compareNetwork(target, solutionNetwork)):
                print("I have found the proper image.")
                print("The answer is image #{}".format(solutionNetwork.nodeTwo.imageTag))
                return True
                
        return False

def compareNetwork(target, goal):
    if(target.nameRelationship == goal.nameRelationship
     and target.shapeRelationship == goal.shapeRelationship
     and target.fillRelationship == goal.fillRelationship):
        return True
    else:
        return False



        
from SemanticNetwork import SemanticNetwork, Node


"""
Iterate through each of the proposed solutions from Ravens matrices, and establish a semantic network
between image C and each of the proposed solutions.  After creating the network, call compareNetwork to
step by step compare the semantic relationship between the target representation and the goal representation.
Return True and log the correct answer, otherwise return False
"""
def solve(target, imageC, solutions):
    node_one = Node(imageC.image_tag)
    goal_found = False

    for key, value in solutions.items():
        node_two = Node(value.image_tag)
        shape_relationship = SemanticNetwork.get_shape_relationship(imageC, value)
        fill_relationship = SemanticNetwork.get_fill_relationship(imageC, value)

        goal = SemanticNetwork(node_one, node_two, shape_relationship, fill_relationship)

        if(compare_network(target, goal)):
            print("I have found the proper image.")
            print("The answer is image #{}".format(goal.node_two.image_tag))
            goal_found = True
            return goal_found
    
    if(goal_found == False):
        print("Sorry, none of the proposed solutions matches the target case")
        
    return goal_found

def compare_network(target, goal):
    if(target.shape_relationship == goal.shape_relationship
     and target.fill_relationship == goal.fill_relationship):
        return True
    else:
        return False



        
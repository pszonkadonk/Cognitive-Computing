from RavenProblem import RavenObject

"""
A node in a semantic network representing the shape and name of the image (I.E 'Z')
"""

class Node:

    def __init__(self, image_tag):
        self.image_tag = image_tag

class SemanticNetwork:

    def __init__(self, node_one, node_two, shape_relationship = None, fill_relationship = None):
        self.node_one = node_one
        self.node_two = node_two
        self.shape_relationship = shape_relationship
        self.fill_relationship = fill_relationship
    
    def create_network(image_one, image_two):
        node_one = Node(image_one.image_tag)
        node_two = Node(image_two.image_tag)
        shape_relationship = SemanticNetwork.get_shape_relationship(image_one, image_two)
        fill_relationship = SemanticNetwork.get_fill_relationship(image_one, image_two)

        return SemanticNetwork(node_one, node_two, shape_relationship, fill_relationship)


    def get_shape_relationship(image_one, image_two):
        if(image_one.shape == image_two.shape):
            return True
        else:
            return False
            
    def get_fill_relationship(image_one, image_two):
        if(image_one.fill == image_two.fill):
            return True
        else:
            return False

        
            
        


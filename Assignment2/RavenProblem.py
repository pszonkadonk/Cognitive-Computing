"""
Representation of an image in the Ravens matrix
"""
class RavenObject:
    
    def __init__(self, image_tag, shape, fill):
        self.image_tag = image_tag
        self.shape = shape
        self.fill = fill


class RavenProblem:

    def __init__(self, test, solutions):
        self.test = test
        self.solutions = solutions
    


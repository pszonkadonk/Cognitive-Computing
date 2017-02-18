import filereader

"""
Representation of an image in the Ravens matrix
"""
class RavenObject:
    
    def __init__(self, imageTag, name, shape, fill):
        self.imageTag = imageTag
        self.name = name
        self.shape = shape
        self.fill = fill


class RavenProblem:

    def __init__(self, test, solutions):
        self.test = test
        self.solutions = solutions

# Pass file through parseMatrixFile and return an array which
# can be further parsed into a matrix, seperating the test
# images from proposed solutions

    def createProblem(fileName):
        matrix = filereader.parseMatrixFile(fileName)
        problem = {}
        solutions = {}
        
        for sequence in matrix:
            if(sequence[0] == 'A' or sequence[0] == 'B' or sequence[0] == 'C'):
                imageId = sequence[0]
                problem[imageId] = RavenObject(imageId, sequence[1],  sequence[2].split(":")[1], sequence[3].split(":")[1])
            elif(sequence[0] == '1' or sequence[0] == '2' or sequence[0] == '3' or sequence[0] == '4' or sequence[0] == '5' or sequence[0] == '6'):
                imageId = sequence[0]
                solutions[imageId] = RavenObject(imageId, sequence[1],  sequence[2].split(":")[1], sequence[3].split(":")[1])

        return RavenProblem(problem, solutions)

    


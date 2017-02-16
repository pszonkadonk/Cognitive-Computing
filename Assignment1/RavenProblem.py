import filereader
from RavenObject import RavenObject

class RavenProblem:

    def __init__(self, test, solutions):
        self.test = test
        self.solutions = solutions
        

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

    

                
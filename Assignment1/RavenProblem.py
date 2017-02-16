import filereader
from RavenObject import RavenObject

class RavenProblem:

    def __init__(self, test, solutions):
        self.test = test
        self.solutions = solutions
        

    def createProblem(fileName):
        matrix = filereader.parseMatrixFile(fileName)
        problem = []
        solutions = []
        
        for sequence in matrix:
            if(sequence[0] == 'A' or sequence[0] == 'B' or sequence[0] == 'C'):
                ravenTestShape = RavenObject(sequence[0],  sequence[1].split(":")[1], sequence[2].split(":")[1])
                problem.append(ravenTestShape)
            elif(sequence[0] == '1' or sequence[0] == '2' or sequence[0] == '3' or sequence[0] == '4' or sequence[0] == '5' or sequence[0] == '6'):
                ravenSolutionShape = RavenObject(sequence[0],  sequence[1].split(":")[1], sequence[2].split(":")[1])
                solutions.append(ravenSolutionShape)

        return RavenProblem(problem, solutions)

    

                
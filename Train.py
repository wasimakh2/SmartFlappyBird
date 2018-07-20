from Bird import FlappyBird
import numpy as np
import time


populationCount = 10

def main(brains=None):
    birds = [FlappyBird(i) for i in range(populationCount)]
    if brains:
        for i in range(populationCount):
            birds[i].brain = brains[i]
    for bird in birds:
        bird.init()

    for bird in birds:
        bird.process.join()
    # all the birds have died
    
    birds = calculateFitness(birds)
    fitness = [birds[i].fitness for i in range(populationCount)]
    print(fitness)
    time.sleep(2)
    nextGeneration(birds)

def calculateFitness(birds):
    totalScore = sum([birds[i].getScore() for i in range(populationCount)])
    for bird in birds:
        bird.fitness = bird.finalScore.value / totalScore
    return birds

def nextGeneration(birds):
    newBirdBrains = []
    for i in range(populationCount):
        newBirdBrains.append(pickOne(birds))
    
    main(newBirdBrains)
def pickOne(birds):
    index = 0
    r = np.random.rand()
    while r > 0:
        r -= birds[index].fitness
        index += 1
    index -= 1
    return birds[index].mutate(0.0)


if __name__ == '__main__':
    main()
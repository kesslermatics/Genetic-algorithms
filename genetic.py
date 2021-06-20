
import random

def generateParent(length, geneSet):
    # Array mit Wort
    genes = []
    while len(genes) < length:
        sampleSize =  min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
        return "".join(genes)

def mutate(parent, geneSet):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene 
    return "".join(childGenes)

def getBest(getFitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = generateParent(targetLen, geneSet)
    bestFitness = getFitness(bestParent)
    display(bestParent)
    if bestFitness >= optimalFitness:
        return bestParent
    while True:
        child = mutate(bestParent, geneSet)
        childFitness = getFitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= optimalFitness:
            return child
        bestFitness = childFitness
        bestParent = child

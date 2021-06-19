
import random
import datetime

# GeneSet für alle möglichen Zeichen
geneSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!. "
# Ziel-Wort
target = "Robert ist ein kuehler Typ!"

# Anfangsstring wird hier zufällig generiert 
def generate_parent(length):
    # Array mit Wort
    genes = []
    while len(genes) < length:
        sampleSize =  min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
        return "".join(genes)

# Fitness wird hier definiert, wie viele Buchstaben schon dem Ziel-Wort entsprechen
def getFitness(guess):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)

# Hier wird ein Buchstabe zufällig verändert. Dazu gibt es noch eine alternierende Mutation, falls das neugenerierte Gen das Selbe ist, wie das zu ersetzende 
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene 
    return "".join(childGenes)

# Hier wird die aktuelle Generation auf dem Terminal angezeigt
def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = getFitness(guess)
    print("{}\t{}\t{}".format(guess, fitness, timeDiff))



random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = getFitness(bestParent)
display(bestParent)

while True:
    child = mutate(bestParent)
    childFitness = getFitness(child)
    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
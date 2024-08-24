# Genetic Algorithm Word Evolution

## Overview

This project implements a simple genetic algorithm to evolve a randomly generated string into a target phrase. The algorithm repeatedly mutates the string, selecting the most "fit" version of the string (i.e., the version closest to the target phrase) until it matches the target exactly. The project serves as an educational tool to illustrate the concepts of genetic algorithms in a fun and interactive way.

## How It Works

1. **GeneSet**: The possible characters that can be used to form the string, including lowercase and uppercase letters, spaces, and punctuation.
2. **Target Phrase**: The phrase we want the genetic algorithm to evolve towards. In this example, the target is `"Robert ist ein kuehler Typ!"`.
3. **Generate Parent**: The algorithm starts by generating a random string of the same length as the target phrase.
4. **Fitness Evaluation**: The fitness of a string is determined by how many characters match the corresponding characters in the target phrase.
5. **Mutation**: A random character in the string is replaced with another character from the GeneSet. If the mutation improves the fitness, it is accepted; otherwise, it is discarded.
6. **Evolution**: This process repeats, with the string evolving over time, until the target phrase is achieved.

## Code Explanation

- **generate_parent(length)**: Generates a random string of a given length using characters from the GeneSet.
- **getFitness(guess)**: Calculates the fitness score of a given string by comparing it to the target phrase.
- **mutate(parent)**: Mutates a single character in the string, ensuring that the new character is different from the original.
- **display(guess)**: Prints the current string, its fitness score, and the time elapsed since the start of the algorithm.

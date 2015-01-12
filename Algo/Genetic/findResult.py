
from rcdtype import *
import operator
import math

TARGET = int(raw_input("Number to find ?: "))
MAX_GEN = int(raw_input("Maximum number of generations ?: "))

POP_SIZE = 50
GEN_LEN = 4
CHROM_LEN = 80
MUTATION_RATE = 0.001
CROSSOVER_RATE = 0.7
RESULT_FOUND = 1337.42

Chromosome = recordtype('Chromosome', 'genes fitness')

DECODE_OP = {10: (operator.add, '+'),
             11: (operator.sub, '-'),
             12: (operator.mul, '*'),
             13: (operator.div, '/')}

def rand():
    from random import random
    return random()

def parseGenes(genes):
    op = True
    literals = []

    for i in range(0, GEN_LEN * CHROM_LEN, GEN_LEN):
        if not genes[i:i+GEN_LEN]:
            continue
        curr_gene = int(''.join(genes[i:i+GEN_LEN]), 2)
        if op:
            if curr_gene < 10 or curr_gene > 13:
                continue
            else:
                op = False
                literals.append(curr_gene)
                continue
        else:
            if curr_gene > 9:
                continue
            else:
                op = True
                if curr_gene == 0 and literals[-1] == 13:
                    literals[-1] = 10
                literals.append(curr_gene)
                continue

    return literals

def getFitness(genes, target):
    decoded = parseGenes(genes)
    res = 0.0

    for i in xrange(0, len(decoded)-1, 2):
        res = DECODE_OP[decoded[i]][0](res, decoded[i+1])

    if res == TARGET:
        return RESULT_FOUND
    else:
        return 1/math.fabs(TARGET - res)

def printChromosome(chrom):
    decoded = parseGenes(chrom.genes)

    print 0,
    for elem in decoded:
        print elem if elem < 10 else DECODE_OP[elem][1],
    print ''

def randGenes():
    return ['1' if rand() < 0.5 else '0' for x in range(GEN_LEN * CHROM_LEN)]

def randChromosome():
    chrom = Chromosome(randGenes(), 0.0)
    chrom.fitness = getFitness(chrom.genes, TARGET)
    return chrom

def crossover(pick1, pick2):
    if rand() < CROSSOVER_RATE:
        cross = int(rand() * GEN_LEN * CHROM_LEN)
        return (Chromosome(pick1.genes[0:cross] + pick2.genes[cross:GEN_LEN * CHROM_LEN], 0.0),
                Chromosome(pick2.genes[0:cross] + pick1.genes[cross:GEN_LEN * CHROM_LEN], 0.0))
    return pick1, pick2

def mutate(chrom):
    chrom.genes = ['1' if gene == '0' else '0' for gene in chrom.genes]
    return chrom

def wheelPick(pop, total_fitness):
    rand_part = rand() * total_fitness
    fitness = 0.0

    for i in xrange(POP_SIZE):
        fitness += pop[i].fitness
        if fitness >= rand_part:
            return pop[i]

    return Chromosome([], 0.0)

def main():
    pop = [Chromosome(randGenes(), 0.0) for i in xrange(POP_SIZE)]
    found = False
    n_gen = 0

    while not found:
        for i in xrange(POP_SIZE):
            pop[i].fitness = getFitness(pop[i].genes, TARGET)

        for chrom in pop:
            if chrom.fitness == RESULT_FOUND:
                print "Chromosome found in", n_gen, "generations"
                printChromosome(chrom)
                found = True
        if found or n_gen > MAX_GEN:
            break

        next_pop = []
        total_fitness = sum(chrom.fitness for chrom in pop)

        for i in xrange(POP_SIZE):
            pick1 = wheelPick(pop, total_fitness)
            pick2 = wheelPick(pop, total_fitness)
            pick1, pick2 = crossover(pick1, pick2)
            next_pop.append(mutate(pick1))
            next_pop.append(mutate(pick2))

        pop = next_pop

        n_gen += 1

    if n_gen > MAX_GEN:
        print "No solution found"

if __name__ == "__main__":
    main()

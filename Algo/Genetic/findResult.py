
from rcdtype import *
import operator
import math

# TARGET = int(raw_input("Number to find ?: "))
# MAX_GEN = int(raw_input("Maximum number of generations ?: "))

TARGET = 42.0
POP_SIZE = 50
MAX_GEN = 300
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
    from random import randint
    return randint(0,9)

def parseGenes(genes):
    op = True
    literals = []

    for i in range(0, GEN_LEN * CHROM_LEN, GEN_LEN):
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
    return ['1' if rand() < 5 else '0' for x in range(GEN_LEN * CHROM_LEN)]

def randChromosome():
    chrom = Chromosome(randGenes(), 0.0)
    chrom.fitness = getFitness(chrom.genes, TARGET)
    return chrom

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

        # TODO
        # next_pop = []
        # total_fitness = sum(chrom.fitness for chrom in pop)

        # for i in xrange(POP_SIZE):
        #     next_pop.append(crossover(wheelPick(pop, total_fitness),
        #                               wheelPick(pop, total_fitness)))
        # pop = next_pop

        n_gen += 1

    if n_gen > MAX_GEN:
        print "No solution found"

if __name__ == "__main__":
    main()

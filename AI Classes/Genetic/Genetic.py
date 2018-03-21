import numpy as np
import random
import math


class ChCreator:
    '''
    Klasa techniczna - nadaje nazwy genotypom
    '''

    ids = []
    id = 1

    def names(self):
        '''
        Funkcja nadaje unikalne nazwy genotypom
        '''

        if ChCreator.id not in ChCreator.ids:
            ChCreator.ids.append(ChCreator.id)
            ChCreator.id += 1
            return 'ch' + str(ChCreator.id-1)


class Genotype:

    def __init__(self):
        self.name = ChCreator.names(self)
        self.fitness = ''.join(random.choice('01') for _ in range(7))
        self.pick_chance = 0

    def __repr__(self):
        return self.name

    def mutation(self, m_prob):
        '''
        Mutacja polega na zmianie znaku w parametrze fitness na przeciwny
        w przypadku kiedy spelniona bedzie zaleznosc zwiazana z prawdopodobienstwem mutacji
        '''
        if np.random.rand() <= m_prob:
            _mutation = random.randint(0, 6)
            self.fitness = list(self.fitness)
            if self.fitness[_mutation] == '0':
                self.fitness[_mutation] = '1'
            else:
                self.fitness[_mutation] = '0'
            self.fitness = ''.join(self.fitness)
        return self.fitness

    def fitness_value(self):
        '''
        Przerabia wartosc dwojkowa fitness na postac dziesietna
        '''
        return int(self.fitness, 2)


def crossover(obj1, obj2, c_prob):
    '''
    Funkcja krzyzuje ze soba dwa kolejne osobniki w losowym puncie, jezeli
    spelniona dla nich zostanie zaleznosc ze prawdopodobienstwo krzyzowania
    bedzie wieksze lub rowne losowaniu
    '''
    if np.random.rand() <= c_prob:
        point = random.randint(0, 6)
        first_part = obj1.fitness[point:]
        second_part = obj2.fitness[point:]
        obj1.fitness = "{}{}".format(obj1.fitness[:point], second_part)
        obj2.fitness = "{}{}".format(obj2.fitness[:point], first_part)


def write(filename, lst, param):
    '''
    Funkcja zapisuje wyniki poszczegolnj iteracji
    '''
    file = open(filename, 'a')
    file.write('\n' + 'iteration = ' + str(param) + '\n')
    for obj in lst:
        file.write(str(obj.__repr__()) + ' fitness is: ' + obj.fitness + ',' + ' value is: ' + str(obj.fitness_value()) + '\n')
    file.write('avg: ' + str(np.mean([obj.fitness_value() for obj in lst])) + ' max: ' + str(np.max([obj.fitness_value() for obj in lst]))
               + ' min: ' + str(np.min([obj.fitness_value() for obj in lst])) + '\n')
    file.close()


def whole_fitness(lst):
    '''
    Funkcja sumuje wszystkie wartosci dziesietne fitness celem mozliwosci 
    wyznaczenia czesci dla kazdej z wartosci
    '''
    result = 0
    for elem in lst:
        result += elem.fitness_value()
    return result


def pick(lst):
    '''
    Funkcja tworzy liste z wartoscami stanowiacymi o wielkosci przedzialow 
    do losowania osobnikow podelgajacym krzyzowaniu 
    '''
    chances_list = []
    for obj in lst:
        obj.pick_chance = round(obj.fitness_value() / whole_fitness(lst), 2)
        chances_list.append(obj.pick_chance)
    return chances_list


def parent_picker(lst, index_number):
    '''
    Funkcja sluzy do doboru drugiego "rodzica" dla wylosowanego genotypu do krzyzowania 
    '''
    if index_number != len(lst)-1:
        return lst[index_number], lst[index_number+1]
    else:
        return lst[index_number], lst[0]


def roulette(lst):
    '''
    Na podstawie listy z przydzialem wartosci do losowania do krzyzowania,
    tworzy liste z progowym zakresem wartosci dla kazdego osobnika
    '''
    roulette_list = []
    threshold = 0
    for val in lst:
        threshold += val
        roulette_list.append(round(threshold, 2))
    return roulette_list


def generation(lst, lst2, c_prob):
    '''
    Funkcja wyznacza i krzyzuje ze soba osobniki (rodzicow) tworzac nowe (potomstwo)
    '''
    for idx in range(len(lst)):
        chance = round(random.random(), 2)
        for elem in lst:
            if chance <= elem:
                crossover(parent_picker(lst2, lst.index(elem))[0], parent_picker(lst2, lst.index(elem))[1], c_prob)
                break


def final_function(lst, a, b):
    '''
    Zwraca liste wynikow wartosci dziesitnych przystosowania przekazanych jako 'x'
    do przygotowanej funkcji.
    '''
    return [round(a*math.cos(x.fitness_value())+b, 2) for x in lst]


def main():
    open('/home/slawek/PycharmProjects/genetic/results.txt', 'w')
    open('/home/slawek/PycharmProjects/genetic/results.txt', 'w').close()
    population = 16#int(input("Set the population size: "))
    iterations = 1000#int(input("Set the number of iterations (generations): "))
    c_prob = 0.65#float(input("Set the crossing probability in range of 0.00 - 1.00: "))
    m_prob = 0.25#float(input("Set the mutation probability in range of 0.00 - 1.00: "))
    a = -3#int(input("Set the 'A' variable for function (can be negative): "))
    b = 4#int(input("Set the 'B' variable for function (can be negative): "))
    genes = [Genotype() for _ in range(population)]

    for run in range(iterations):
        generation(roulette(pick(genes)), genes, c_prob)
        for elem in genes:
            elem.mutation(m_prob)
        write('/home/slawek/PycharmProjects/genetic/results.txt', genes, run+1)

    print((final_function(genes, a, b)))
    print(max(final_function(genes, a, b)))
    for p in final_function(genes, a, b):
        if p == max(final_function(genes, a, b)):
            print(genes[final_function(genes, a, b).index(p)])


if __name__ == "__main__":
    main()

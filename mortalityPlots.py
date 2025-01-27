from util import *
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
def to_fraction(y, pos):
    return f'{y:.2%}'


def getLifeExpectancy(mortalityByAge, max_age=84):
    le = 0 
    for age in range(len(mortalityByAge)):
        chanceofDyingAtAge = 1
        for j in range(age):
            chanceofDyingAtAge *= (1-mortalityByAge[j])
        chanceofDyingAtAge *= mortalityByAge[age]
        le += chanceofDyingAtAge * age
    chanceofSurvivingToMaxAge = 1


    #add all the survivors to the max age
    for j in range(len(mortalityByAge)):
        chanceofSurvivingToMaxAge *= (1-mortalityByAge[j])
    le += chanceofSurvivingToMaxAge * len(mortalityByAge)
    return le 


def getAccumulatedChanceofDying(mortalityByAge):
    accumulatedChanceofDying = 1
    for i in range(len(mortalityByAge)):
        accumulatedChanceofDying *= (1-mortalityByAge[i]) #chance to survive to 85
    return 1-accumulatedChanceofDying



if __name__ == "__main__":
    file_pathInternal = "./InternalMortality.txt"  # Update this with the path to your file
    file_pathExternal = "./ExternalMortality.txt"  # Update this with the path to your file
    ages, internalMortality = getMortalityData(file_pathInternal)
    ages, externalMortality = getMortalityData(file_pathExternal)

    # adjust mortality to ancient era
    # externalMortality = [10*x for x in externalMortality]
    
    allCauseMortality = [internalMortality[i] + externalMortality[i] for i in range(len(internalMortality))]



    print("Life Expectancy: ", getLifeExpectancy(allCauseMortality))
    print("External Chance of Dying: ", getAccumulatedChanceofDying(externalMortality))
    print("Internal Chance of Dying: ",getAccumulatedChanceofDying(internalMortality))



    plt.plot(ages, externalMortality, label='External Mortality')
    plt.plot(ages, internalMortality, label='Internal Mortality')
    # plt.plot(ages, allCauseMortality, label='All Cause Mortality')
    # plt.yscale('log')
    # plt.ylim(0, 0.002)

    plt.xlabel('Age')
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=10))
    plt.ylabel('Mortality Rate')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_fraction))
    plt.gcf().subplots_adjust(left=0.15)
    plt.title('Mortality Rates by Age')
    plt.legend()
    plt.show()
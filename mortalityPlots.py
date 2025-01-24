from util import *
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

def to_fraction(y, pos):
    return f'{y:.2%}'

def getLifeExpectancy(crude_rate, max_age=84):
    """
    Given a list or function 'mortality' such that mortality[a] = M(a),
    return the expected life (life expectancy).
    """
    life_expectancy = 0.0
    prob_survive_to_a = 1.0  # S(0) = 1.0, meaning newborn survival is 100% initially
    
    for a in range(max_age + 1):
        life_expectancy += prob_survive_to_a
        prob_survive_to_a *= (1.0 - crude_rate[a])  
        if prob_survive_to_a < 1e-15:
            break
    return life_expectancy

if __name__ == "__main__":
    file_pathInternal = "./InternalMortality.txt"  # Update this with the path to your file
    file_pathExternal = "./ExternalMortality.txt"  # Update this with the path to your file
    ages, internalMortality = getMortalityData(file_pathInternal)
    ages, externalMortality = getMortalityData(file_pathExternal)

    # externalMortality = [10*x for x in externalMortality]
    
    allCauseMortality = [internalMortality[i] + externalMortality[i] for i in range(len(internalMortality))]

    print(getLifeExpectancy(allCauseMortality))

    plt.plot(ages, externalMortality, label='External Mortality')
    plt.plot(ages, internalMortality, label='Internal Mortality')
    plt.plot(ages, allCauseMortality, label='All Cause Mortality')
    # plt.yscale('log')
    # plt.ylim(0, 0.001)

    plt.xlabel('Age')
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=10))
    plt.ylabel('Mortality Rate')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_fraction))
    plt.gcf().subplots_adjust(left=0.15)
    plt.title('Mortality Rates by Age')
    plt.legend()
    plt.show()
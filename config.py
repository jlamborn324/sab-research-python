import csv
from scipy import stats
import matplotlib.pyplot as plt



class Case:
    def __init__(self, numcode, VMAR_Group, country, VMAR_Region, year, POLDIS,
                 ECDIS, GROUPCON, INTERCON, CCGROUPSEV1):
        self.numcode = numcode
        self.VMAR_Group = VMAR_Group
        self.country = country
        self.VMAR_Region = VMAR_Region
        self.year = year
        self.POLDIS = POLDIS
        self.ECDIS = ECDIS
        self.GROUPCON = GROUPCON
        self.INTERCON = INTERCON
        self.CCGROUPSEV1 = CCGROUPSEV1

    def __str__(self):
        return "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.numcode, self.VMAR_Group , self.country , self.VMAR_Region,
                                                      self.year, self.POLDIS, self.ECDIS ,  self.GROUPCON , self.INTERCON,
                                                      self.CCGROUPSEV1)


def parser(file):
    """Returns a dictionary of case instances. The keys are the number codes of the cases,
    and the values are the corresponding case instance. """
    data_dictionary = {}
    with open(file) as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        csvfile.readline()

        for row in readcsv:
            tuple(row)
            numcode, VMAR_Group, country, VMAR_Region,\
            year, POLDIS, ECDIS, GROUPCON, INTERCON , \
            CCGROUPSEV1 = row

            data_dictionary[numcode] = Case(numcode, VMAR_Group, country, VMAR_Region, year, POLDIS, ECDIS, GROUPCON,
                                            INTERCON, CCGROUPSEV1)

        return data_dictionary


def ecdisselector(data, range):
    """
    Takes a dictionary of case data and returns data containing given ECDIS values

    :param data:
    A dictionary of case data
    :param range:
    A list containing the values of ECDIS the user is looking for in the given data
    :return:
    A dictionary of case data only containing cases with certain ECDIS values
    """

    selected_data = {}
    for i in data:

        if data[i].ECDIS in range:
            selected_data[i] = data[i]
    return selected_data


def poldisselector(data, valuesneeded):
    """
    Takes a dictionary of case data and returns cases that have the given POLDIS values
    :param data:
    A dictionary of case data
    :param valuesneeded:
    A list containing the values of POLDIS the user is looking for in the given data
    :return:
    A dictionary of case data only containing cases with certain ECDIS values
    """

    selected_data = {}
    for i in data:
        if data[i].POLDIS in valuesneeded:
            selected_data[i] = data[i]
    return selected_data


def scatterplot(yvalues, ylabel, xvalues,  xlabel, filesave):

    slope, intercept, r_value, p_value, std_err = stats.linregress(yvalues, xvalues)
    print("Slope of best fit line is", slope)
    print("r_value - ", r_value)

    plt.scatter(yvalues, xvalues, alpha='.5')
    plt.axis([0, 3, 0, 6])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(ylabel +  "vs." +  xlabel)

    plt.savefig(filesave)
    plt.show()

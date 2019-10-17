import csv
import matplotlib.pyplot as plt
from scipy import stats

class case:
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


full_data = {}
with open ("Ethnic Enclave Data MAR _ S.csv" ) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    csvfile.readline()

    for row in readCSV:

        numcode = row[0]
        VMAR_Group = row[1]
        country = row[2]
        VMAR_Region = row[3]
        year = row[4]
        POLDIS= row[5]
        ECDIS = row[6]
        GROUPCON = row[7]
        INTERCON = row[8]
        CCGROUPSEV1 = row[9]

        full_data[numcode] = case(numcode, VMAR_Group, country, VMAR_Region,year, POLDIS, ECDIS, GROUPCON,
                                  INTERCON, CCGROUPSEV1)


low_level = {}
high_level= {}

for i in full_data:

    if full_data[i].POLDIS in ["0", "1", "2"]:
        if full_data[i].ECDIS in ["0", "1", "2"]:
            low_level[i] = full_data[i]
    if full_data[i].POLDIS in ["3", "4"]:
        if full_data[i].ECDIS in ["3", "4"]:
            high_level[i] = full_data[i]



for i in low_level:
    print("Case #: {} \n POLDIS #: {} \n ECDIS #: {} ".format(i, low_level[i].POLDIS, low_level[i].ECDIS))
    print("-" * 10)

print("--------------------------------------------------------------")

y_values = []
x_values = []

for i in full_data:
    if full_data[i].GROUPCON == "-99":
        continue
    if full_data[i].CCGROUPSEV1 == "-99":
        continue



    y_values.append(int(full_data[i].GROUPCON))
    x_values.append(int(full_data[i].CCGROUPSEV1))
# print(y_values)
# print(x_values)

slope, intercept, r_value, p_value, std_err = stats.linregress(x_values,y_values)
print("Slope of best fit line is" , slope)
print("r_value - ", r_value)


plt.scatter(x_values, y_values, alpha='.5')
plt.axis([0, 3, 0, 6])

plt.show()




    ## Level of dispersion on y (GROUPCON)
    ## Severity of intergroup conflict (CCSEV1)






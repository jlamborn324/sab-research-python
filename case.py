import matplotlib.pyplot as plt
from scipy import stats
from config import *


complete_data = parser("Ethnic Enclave Data MAR _ S.csv")

# data with  ecdis & poldis < 3
low_level_data = ecdisselector(poldisselector(complete_data, ["0", "1", "2"]), ["0", "1", "2"])

# data with ecids & poldis => 3
high_level_data = ecdisselector(poldisselector(complete_data, ["3", "4"]), ["3", "4"])


# for i in low_level_data:
#     print("Case #: {} \n POLDIS #: {} \n ECDIS #: {} ".format(i, low_level_data[i].POLDIS, low_level_data[i].ECDIS))
#     print("-" * 10)
#
# print("--------------------------------------------------------------")

y_values = []
x_values = []

for i in complete_data:
    if complete_data[i].GROUPCON == "-99":
        continue
    if complete_data[i].CCGROUPSEV1 == "-99":
        continue

    y_values.append(int(complete_data[i].GROUPCON))
    x_values.append(int(complete_data[i].CCGROUPSEV1))


# Demonstration of data analysis using Groupcon vs. CCSEV1 values.
scatterplot(y_values, "GROUPCON", x_values, "CCSEV1", "GROUPCON-vs-CCSEV1")





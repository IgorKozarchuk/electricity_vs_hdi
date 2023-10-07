import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

electric_hdi_data = pd.read_csv("electricity_hdi_data.csv")
# print(electric_hdi_data.head())

X = electric_hdi_data["Electricity consumption per capita, kWh/year"]
Y = electric_hdi_data["HDI"]
C = electric_hdi_data["Country"]

sns.set(rc={"figure.figsize":(11.7,8.27),
			"font.size": 9}) # labels font

sns.set_style("darkgrid")

ax = sns.scatterplot(x=X,
					y=Y,
					data=electric_hdi_data,
					hue="HDI",
					palette="Spectral")

ax.set_title("Human Development Index (HDI) vs. Annual electricity consumption (2019 data)", fontdict={"size": 16, "weight": "bold"})

sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))

plt.setp(ax.get_legend().get_title(), fontsize="9")
plt.setp(ax.get_legend().get_texts(), fontsize="8")

# plt.xscale("log") # logarithmic scale of x axis

filter_list = ["Argentina", "Bahrain", "Brazil", "China", "Germany", "Iceland", "India", "Italy", "Japan", "Niger", "Norway", "Pakistan", "Uganda", "Ukraine", "United States", "Vietnam", "Yemen"]

# label points funtion
def label_points(ax, filter_list):
	for x in filter_list:
		i = C[C == x].index[0] # index where item in a C series matches filter list item
		ax.annotate(x, (X[i], Y[i]))

label_points(ax, filter_list)

plt.show()

#Task-01
#Create a bar chart or histogram to visualize the distribution
#of a categorical or continuous variable,
#such as the distribution of ages or genders in a population.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_6298256.csv', skiprows=3)

newHeader =  data.iloc[0]
data = data[1:]
data.columns = newHeader

print(data.head(10))

print(data.columns.tolist())

countryName = 'Aruba'
countryData = data[data['Country Name'] == countryName]

years = [1960.0,1961.0, 1962.0, 1963.0, 1964.0, 1965.0, 1966.0, 1967.0, 1968.0, 1969.0, 1970.0, 1971.0, 1972.0, 1973.0, 1974.0, 1975.0, 1976.0, 1977.0, 1978.0, 1979.0, 1980.0, 1981.0, 1982.0, 1983.0, 1984.0, 1985.0, 1986.0, 1987.0, 1988.0, 1989.0, 1990.0, 1991.0, 1992.0, 1993.0, 1994.0, 1995.0, 1996.0, 1997.0, 1998.0, 1999.0, 2000.0, 2001.0, 2002.0, 2003.0, 2004.0, 2005.0, 2006.0, 2007.0, 2008.0, 2009.0, 2010.0, 2011.0, 2012.0, 2013.0, 2014.0, 2015.0, 2016.0, 2017.0, 2018.0, 2019.0, 2020.0, 2021.0, 2022.0]
population = countryData[years].iloc[0].astype(float)


plt.figure(figsize=(10, 5))
plt.plot(years, population, marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Population Trend for {countryName}')
plt.grid(True)
plt.tight_layout()
plt.show()

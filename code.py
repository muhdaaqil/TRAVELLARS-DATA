import pandas as pd
import numpy as np
import datetime
import csv
import matplotlib.pyplot as plt
list=[]
countries={}
c=[]

#load csv file
df=pd.read_excel('data.xlsx')

df.iloc[350:] #select the column values from 2007 onwards (in excel file it was from 350 the row onwards)

#print(df.columns)
print(type(df['Periods'])) #check wheather the data was lodaed properly by checking any one column date type
plt.plot(df.iloc[350:]['Periods'],df.iloc[350:][' Scandinavia'],label ='Scandinavia') # plotting graph between period and Scandinavia
plt.plot(df.iloc[350:]['Periods'],df.iloc[350:]['USA'],label ='USA')  # plotting graph between period and usa
plt.plot(df.iloc[350:]['Periods'],df.iloc[350:]['Canada'],label='Canada')  # plotting graph between period and canada
plt.plot(df.iloc[350:]['Periods'],df.iloc[350:]['Australia'],label='Australia')  # plotting graph between period and australia
plt.plot(df.iloc[350:]['Periods'],df.iloc[350:]['New Zealand'],label='New Zealand')   # plotting graph between period and newzealand
plt.plot(df.iloc[350:]['Periods'],df.iloc[350:][' Africa'],label='Africa')  # plotting graph between period and africa
plt.title('Number of Visitor vs Year ')
plt.ylabel('Number of Visitors to Singapore')
plt.xlabel('From 2007-2017')
plt.legend() #adding legend to ploted graph




a=df.iloc[350:][' Scandinavia'].sum() #count the Scandinava cloumn sum
print("Scandinava =", a) #print the Scandinava sum
list.append(a) # append the Scandinava sum into list
countries["Scandinava"]=a #insert the "Scandinava" data in to dictionary


b=df.iloc[350:]['USA'].sum() #count the usa cloumn sum
print("USA=",b) #print the usa sum 
list.append(b) #append the usaa sum into list
countries["USA"]=b #insert the "usa" data in to dictionary

c=df.iloc[350:]['Canada'].sum() #count the canada cloumn sum
print("canada = ",c) #print the canada sum
list.append(c) #append the canada sum into list
countries["canada"]=c #insert the "canada" data in to dictionary



d=df.iloc[350:]['Australia'].sum() #count the Australia cloumn sum
print("Australia = ",d) #print the  Australia sum
list.append(d) #append the Australia sum into list
countries["Australia"]=d #insert the "Australia" data in to dictionary



e=df.iloc[350:]['New Zealand'].sum() #count the New Zealand cloumn sum
print("New Zealand = ",e) #print the  New Zealand sum
list.append(e) #append the New Zealand sum into list
countries["New Zealand"]=e #insert the "New Zealand" data in to dictionary




f=df.iloc[350:][' Africa'].sum() #count the Africa  cloumn sum
print("Africa = ",f) #print the  Africa sum
list.append(f) #append the Africa sum into list
countries["Africa"]=f  #insert the "Africa" data in to dictionary

print("Top 3 Contries  ") # print top 3 countries
i=0
j=1
#sorting the values in descending order and printing upto first 3
for key, value in sorted(countries.items(), key=lambda item: item[1],reverse=True):
    print(j,".","%s: %s" % (key, value))
    j+=1
    if j==4:
        break

# plot the graph for the seelcted columns and show
frame1=plt.gca()
for xlabel_i in frame1.axes.get_xticklabels():
    xlabel_i.set_visible(False)
    xlabel_i.set_fontsize(0.0)
plt.show()


x=["Africa","canada","Scandinava","New Zealand","USA","Australia"]
y=sorted (countries.values())
plt.title("Total Travellars from Countries(Period: 2007 - 2017)")
plt.bar(x,y)
plt.show()


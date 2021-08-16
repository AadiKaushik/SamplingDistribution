import csv
import pandas as pd
import plotly.figure_factory as ff
import random 
import statistics

df = pd.read_csv('C:/Users/aadi_/Desktop/coding/python/sampling data/archive (1)/medium_data.csv')

data = df['reading_time'].tolist()



popmean = statistics.mean(data)
popSD = statistics.stdev(data)         

print('population mean and SD are ',popmean,popSD)

def randomSetOfmean(counter):
    dataset = []

    for  i in range(1,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)


    mean = statistics.mean(dataset)
    SD = statistics.stdev(dataset)



    return  mean
def sd() :
    mean_list = []
    for i in range(0,100):
        sampleMean = randomSetOfmean(30)     
        mean_list.append(sampleMean)


    return(mean_list)

def showFig(ml):
    
    mean2 =  statistics.mean(ml)
    print(mean2)
    sd2 = statistics.stdev(ml)
    print(sd2)
    fig = ff.create_distplot([ml],['average'],show_hist=False)
    fig.show()


showFig(sd())
 
sd()
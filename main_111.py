import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random


df = pd.read_csv("C 111 PRO/medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Mean of Population: ",population_mean)
print("Standard Deviation of Population: ",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        index = random.randint(0, len(data)-1)
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#Pass the number of time you want the mean of the data points as a parameter in range function in for loop
mean_list = []
for i in range(0, 100):
    set_of_mean = random_set_of_mean(30)
    mean_list.append(set_of_mean)

#Calculating the mean and standard deviation of the sampling distribution
sampling_mean = statistics.mean(mean_list)
sampling_std_deviation = statistics.stdev(mean_list)
print("Mean of Sampling Distribution: ",sampling_mean)
print("Standard Deviation of Sampling Distribution: ",sampling_std_deviation)

#finding the stadard deviation starting and ending values
first_std_deviation_start,first_std_deviation_end = population_mean - sampling_std_deviation, population_mean + sampling_std_deviation
second_std_deviation_start,second_std_deviation_end = population_mean - (2*sampling_std_deviation), population_mean + (2*sampling_std_deviation)
third_std_deviation_start,third_std_deviation_end = population_mean - (3*sampling_std_deviation), population_mean + (3*sampling_std_deviation)

#finding the mean of the first data
df = pd.read_csv("C 111 PRO/sample2.csv")
data = df["reading_time"].tolist()
mean_of_sample = statistics.mean(data)
print("Mean of Sample is: ", mean_of_sample)
fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist = False)
fig.add_trace(go.Scatter(x = [population_mean,population_mean], y = [0,0.72], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample,mean_of_sample], y = [0,0.72], mode = "lines", name = "Mean of sample1"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y = [0,0.72], mode = "lines", name = "STD1"))
fig.show()

z_score_ = (mean_of_sample - sampling_mean)/sampling_std_deviation
print("The Z score of data is: ", z_score_)
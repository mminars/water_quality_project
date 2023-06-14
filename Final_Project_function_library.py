#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:59:02 2022

@author: michaelminars
"""
#imports
import pandas as pd
import matplotlib.pyplot as plt
import speech_recognition as sr


#python reading excel file
data= pd.read_excel('/users/michaelminars/Documents/Final_Project_Data_set-2020_Water_quality_report.xlsx')

# Audio User Input Class
class Sr_input():
    def __init__(self, question):
        self.question=question

    def record_audioui (self): #initial user input
        r= sr. Recognizer () #setting a variable to use the speech recognition package
        with sr.Microphone() as source: #setting the source of the speech recognition as built-in microphone
            print (self.question)
            audio= r.listen(source)
            voice_data= r.recognize_google(audio)
            print (voice_data)
        return str (voice_data) #returning voice data as a string 


# code for graph:
    # testing comments !!!!!!!!!
#make data for graph
def make_table_data_graph():
    i=1
    table_data=[['Contaminate','Amount Detected']]
    while i < len (data):
        x=data['Contaminante'][i]
        y=data['Maximum Amount Detected'][i], data['Units'][i]
        table_data.append ([x,y])
        i+=1
    return table_data

#function to display table

def make_table (table_data,title):
    '''-> fig
    uses make_data fucntion to display a table
    '''
    fig, ax = plt.subplots() #define figure and axes
    table_data= table_data
    #create table
    table = ax.table(cellText=table_data, loc='center')

    #set table parameters and title
    ax.set_title(title, fontsize=35, y=1.95, pad=-20)
    table.set_fontsize(40)
    table.scale(2,1.6)
    ax.axis('off')
    
    return plt.show() #display table

#code for Pi-chart

#pi-chart class

class Pi_chart():
    def __init__(self,kind):
        self.kind=kind 
    def pichart(self):
        if self.kind== 'sources':
            percents=get_percent_of_sources()
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'Naturally occurring', 'drinking water disenfection', 'Water additive', 'Erosion of natural deposits', 'Corrosion of household plumbing systems', 'Road salt contamination', 'industrial sources', 'Other'
            sizes= [float (percents['Naturally occurring']), float (percents['drinking water disenfection']), float (percents['Water additive']), float (percents['Erosion of natural deposits']), float (percents['Corrosion of household plumbing systems']), float (percents['Road salt contamination']), float (percents['industrial sources']), float (percents['Other'])]
            explode = (0, 0, 0, 0, 0, 0, 0, 0)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                      shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
        if self.kind== 'category':
            percents=get_percent_of_category()
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'Regulated Substances', 'Metals & Inorganic Substances', 'Organic Substances', 'Physical Parameters & Unregulated Substances'
            sizes= [float (percents['Regulated Substances']), float (percents['Metals & Inorganic Substances']), float (percents['Organic Substances']), float (percents['Physical Parameters & Unregulated Substances'])]
            explode = (0, 0, 0, 0)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                 shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show() 

#function to round numbers            

def truncate(n, places):
    return round (n,places)

#function that gets percent for each source
def get_percent_of_sources ():
    source_list= data['Typical Source']
    mydict= {'Naturally occurring':0, 'drinking water disenfection':0, 'Water additive':0, 'Erosion of natural deposits':0,
                 'Corrosion of household plumbing systems':0, 'Road salt contamination':0, 'industrial sources':0, 'Other':0}
    total=0
    mydict_percents={}
    for source in source_list:
        if source in mydict.keys():
            mydict[source]+=1
        if source not in mydict.keys():
            mydict['Other']+=1
    for key in mydict.keys():
        total+= mydict[key]
    for key in mydict:
        x= truncate (((mydict[key]/total)*100),2)
        mydict_percents[key]=x
    return  mydict_percents

#function that gets percent for each category
def get_percent_of_category ():
    source_list= data['Category']
    mydict= {'Regulated Substances':0, 'Metals & Inorganic Substances':0, 'Organic Substances':0, 'Physical Parameters & Unregulated Substances':0}
    total=0
    mydict_percents={}
    for source in source_list:
        if source in mydict.keys():
            mydict[source]+=1
    for key in mydict.keys():
        total+= mydict[key]
    for key in mydict:
        x= truncate (((mydict[key]/total)*100),2)
        mydict_percents[key]=x
    return  mydict_percents

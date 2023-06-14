#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:53:28 2022

@author: michaelminars
"""
graphui= 'Date Sampled'
#imports
import pandas as pd
import matplotlib.pyplot as plt
import speech_recognition as sr

#python reading excel file
data= pd.read_excel('/users/michaelminars/Documents/Final_Project_Data_set-2020_Water_quality_report.xlsx')

# Audio User Input Class
class Sr_input():
    '''
    NoneType-> str
    class that has a method that is used to change a question being asked and records speech input
    and returns a str of speech data. also prints speech input
    '''
    def __init__(self, question): #instantiate class with attributes self and question
        self.question=question

    def record_audioui (self): #initial user input
        r= sr. Recognizer () #setting a variable to use the speech recognition package
        with sr.Microphone() as source: #setting the source of the speech recognition as built-in microphone
            print (self.question)
            audio= r.listen(source) #creates varibale audio representing voice data
            voice_data= r.recognize_google(audio) #inturpriting speech input using google API 
            print (voice_data) #printing speech input so user can see on console
        return str (voice_data) #returning voice data as a string, lowercase only


# code for graph block:
    
#make data for graph
def make_table_data_maximum():
    '''
    NoneType-> list
    makes a list of lists that represents data ready to go into a tbale making function
    '''
    i=1 #i represents index of rows for column Contaminate
    table_data=[['Contaminate','Amount Detected']] #initializing list which represents data for table, each element is a row of a table
    while i < len (data):
        x=data['Contaminant'][i] # x represents contaminates for index i 
        y=data['Maximum Amount Detected'][i], data['Units'][i] # y represents measurement and unit for index i  
        table_data.append ([x,y]) #add list x,y as an element of table_data
        i+=1
    return table_data #returns list table_data to be used in table making function 

#function to display table

def make_table (table_data,title):
    '''
    fucntion, str-> fig
    uses make_data fucntion to display a table
    '''
    fig, ax = plt.subplots() #define figure and axes
    table_data= table_data
    #create table
    #set table parameters and title
    ax.set_title(title, fontsize=35, y=1.95, pad=-20)
    table= ax.table(cellText= table_data,loc='center')
    table.set_fontsize(40)
    table.scale(2,1.6)
    ax.axis('off')

    return plt.show() #display table
#code for Pi-chart

#pi-chart class

class Pi_chart():
    '''
    NoneType-> fig
    creates a pi chart using a pi chart method
    '''
    def __init__(self,kind):
        '''
        parameters self adn kind
        this method is intantiating the class so methods can work on an input kind
        '''
        self.kind=kind 
    def pichart(self):
        if self.kind== 'sources':
            '''
            NoneType-> fig
            creates a pi- chart of the percent of contaminats in each source category
            '''
            percents=get_percent_of_sources() #setting perecnts variable as get_percent_of_sources function
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'Naturally Occurring', 'Drinking Water Disinfection', 'Water Additive', 'Erosion of Natural Deposits', 'Corrosion of Household Plumbing Systems', 'Road Salt Contamination', 'Industrial Sources', 'Other'
            sizes= [float (percents['Naturally Occurring']), float (percents['Drinking Water Disinfection']), float (percents['Water Additive']), float (percents['Erosion of Natural Deposits']), float (percents['Corrosion of Household Plumbing Systems']), float (percents['Road Salt Contamination']), float (percents['Industrial Sources']), float (percents['Other'])]
            explode = (0, 0, 0, 0, 0, 0, 0, 0)
            fig1, ax1 = plt.subplots()
            ax1.set_title('Typical Sources of Water Contaminates', fontsize=35, y=1.25, pad=-20)
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                      shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
        if self.kind== 'category':
            '''
            NoneType-> fig
            creates a pi- chart of the percent of contaminats in each contaminat category
            '''
            percents=get_percent_of_category()
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'Regulated Substances', 'Metals & Inorganic Substances', 'Organic Substances', 'Physical Parameters & Unregulated Substances'
            sizes= [float (percents['Regulated Substances']), float (percents['Metals & Inorganic Substances']), float (percents['Organic Substances']), float (percents['Physical Parameters & Unregulated Substances'])]
            explode = (0, 0, 0, 0)
            fig1, ax1 = plt.subplots()
            ax1.set_title('Categories of Water Contaminates', fontsize=35, y=1.25, pad=-20)
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                 shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show() 


def truncate(n, places):
    '''
    float, int-> float
    takes two parameters a number and number of decimal places. then function returns
    the number 'n' rounded to 'places' amount of decimal points 
    '''
    return round (n,places)

#function that gets percent for each source
def get_percent_of_sources ():
    '''
    None-> dict
    creates a dictionary mapping the source of contaminate to the percent of contaminates with source as the key
    '''
    source_list= data['Typical Source'] #source_list represents all data in typical source column 
    #create dict with source of contam as key and initially 0 percent:
    mydict= {'Naturally Occurring':0, 'Drinking Water Disinfection':0, 'Water Additive':0, 'Erosion of Natural Deposits':0,
                 'Corrosion of Household Plumbing Systems':0, 'Road Salt Contamination':0, 'Industrial Sources':0, 'Other':0}
    total=0
    mydict_percents={} #initialize new dict 
    for source in source_list:
        if source in mydict.keys(): #this if block adds 1 to each source for every contaminate that has it 
            mydict[source]+=1
        if source not in mydict.keys(): #for 'other' source add 1 to count
            mydict['Other']+=1
    for key in mydict.keys():
        total+= mydict[key] #sum of total amount of contaminates
    for key in mydict:
        x= truncate (((mydict[key]/total)*100),2) #getting percent of contaminates  coming from each source. and using truncate function to round to 2 decimal places
        mydict_percents[key]=x#new dictiony maps the source to the percent of contaminates that fall into the source
    return  mydict_percents

#function that gets percent for each category
def get_percent_of_category ():
    '''
    NoneType-> dict
    creates a dictionary mapping the category of contaminate to the percent of contaminates with category as the source
    '''
    category_list= data['Category']
    mydict= {'Regulated Substances':0, 'Metals & Inorganic Substances':0, 'Organic Substances':0, 'Physical Parameters & Unregulated Substances':0}
    total=0
    mydict_percents={}#initialize new dict 
    for category in category_list: 
        if category in mydict.keys(): #this if block adds 1 to each category for every contaminate that has it 
            mydict[category]+=1
    for key in mydict.keys():
        total+= mydict[key] #sum of total amount of contaminates
    for key in mydict:
        x= truncate (((mydict[key]/total)*100),2)#getting percent of contaminates coming from each category. and using truncate function to round to 2 decimal places
        mydict_percents[key]=x #new dictiony maps the category to the percent of contaminates that fall into the category
    return  mydict_percents


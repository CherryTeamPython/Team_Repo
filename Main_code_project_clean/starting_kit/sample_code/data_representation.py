#!/usr/bin/python2.7
# -*-coding:utf-8 -*
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import scale
import data_io
from imp import reload
from sklearn import datasets
from sklearn import linear_model
import os
codedir='sample_code/'
from sys import path;path.append(codedir)
import seaborn as sns;sns.set()
from scipy.misc import imread



datadir = '../public_data/'                        # Change this to the directory where you put the input data
dataname = 'crime'
basename = datadir  + dataname
#print basename
#reload(data_io)
data = data_io.read_as_df(basename)
categories = data.groupby('target')

class dataRepresentation:

    """
    attributes:
    crimes coordinate X and Y
    crimes date day/month/year
    résolution 0,1 or 2
    crimes location aka district number
    crimes categories
    """

    """
    function that create and display a map with the different location of each  crime in terms of the coordinates X and Y and the crime category
    """
    
    def create_map():
        CX=data[(data.X<30) & (data.Y<30)]
        sns.pairplot(CX, hue="target",x_vars='X',y_vars='Y',size=5)

    
    """Fonction de comparaison  """

#prend en argument un tableau de valeur "prédiction" et un tableau de résultat attendu "référence"
#on considére quue les tableaux sont de la même taille
    def comparaison(prediction,reference):
        tab3=[]
        #tab3 sert à référencer les numéros des valeurs
        erreur=0
        i=0
        print "Début de boucle"
        while i<len(prediction):
            tab3.append(i) #on incrémente tab3 avec les numéros des valeurs
            if prediction[i]!=reference[i]:
                erreur=erreur+1
            i=i+1 #on passe à la valeur suivante
            erreur=((erreur+0.)/(len(tab3)))*100 #on calcul le pourcentage d'erreur final moyen
        plt.plot(tab3,prediction,"b",linewidth=0.1,label="Prediction") #On créer la courbe de valeur de prédiction de couleur bleue
        plt.plot(tab3,reference,"r",linewidth=0.1,label="Resultat attendu") # On créer la courbe de valeur de référence de couleur rouge
        plt.xlabel('Numero de valeur')
        plt.ylabel('Valeur')
        plt.legend()    
        plt.show()
        print "Pourcentage d'erreur : ",erreur,"%"

    """
    function that create a circular chart for each crime category and represent the rate of arrest
    @param the resolution of type float
    @param the crime category of type string
    """
    
    """def crime_rate_arrest(resolution,category)
    extract the data from the file train.csv
    calculate each rate of resolution for each category
    create a HashMap<resolution,rate> which associate each resolution with his corresponding rate for each category
    create and display the circular chart for each category"""

    """
    function that create histograms which represent number of crimes in terms of a various period of time (ex: number of crimes each year from 2000 to 2012) and each bar is split between the different rates of each category
    @param the crime date Year, Month, Day and Day_num all of types float
    @param the crime category of type string
    """
    
    """def hist_rate_crime(Year,Month,Day,Day_num,category)
    extract the data from the file train.csv
    create a HashMap<Year(or Month,Day,Day_num),crime number> which associate each Year (or Month,Day,Day_num), with the corresponding crime number  
    create a HashMap<category,rate> which associate each category with his corresponding rate for each Year (or Month,Day,Day_num)
    create and display an histogram for each period of time (Year,Month,Day and Day_num) whose each bar is split between the different rate of each category
    """
        
    """
    function that display the number of crimes for each month in each year in 3D.Each bar plot correspond to one year
    """
    def hist_3D():
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d') # Create an empty 3D figure
        for c,y in zip(['red','green','blue','yellow','red','green','blue','yellow'],[1,2,3,4,5,6,7,8,9,10,11,12]):
            xs=np.arange(12) # Number of columns of each histograms
            CYear=data[(data.Year==y)]
            months = CYear.groupby('Month')
            month = []
            num_months = []
            for gr in months.groups:
                month.append(gr)
                num_months.append(len(months.get_group(gr)))
            ys=num_months # Create one histogram per year
            cs=[c]*len(xs) # Set the colors of the histograms
            ax.bar(xs, ys, zs=y, zdir='y', color=cs, alpha=0.8)
        
        ax.set_xlabel('Month')
        ax.set_ylabel('Year')
        ax.set_zlabel('Crime Number')
        plt.show()
    
    #create_map()
    #hist_3D()
    comparaison(data.Year,data.Year)
    
        
        
        

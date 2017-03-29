#!usr/bin/python2.7
# -*-coding:utf-8 -*

from sklearn import preprocessing
import unittest
import data_io
import numpy as np

class process:
    """
    Class preprocessing constructor
    @param data type .data
    """
    def __init__(self):
        self.datadir = 'public_data/'
        self.dataname = 'labels'
        self.basename = datadir + dataname
        reload(data_io)
        self.data = data_io.read_as_df(self.basename)
        self.features = np.loadtxt("starting_kit/public_data/crime_train.data")
        self.year,self.month,self.day,self.day_num,self.minute,self.hour,self.X,self.Y,self.PdDistrict,self.address,self.resolution=np.loadtxt("starting_kit/public_data/crime_train.data", unpack=True)
        self.labels = np.loadtxt("starting_kit/public_data/crime_train.solution")
        self.drug,self.larceny,self.missing_person,self.prostitution,self.vehicule_theft,self.warrants=np.loadtxt("starting_kit/public_data/crime_train.solution", unpack=True)
        self.scaler = preprocessing.RobustScaler()
        self.outliers()
		self.data1 = self.data
    
    def outliers(self):
        self.one_column()
        self.starKiller(self.resolution, 3, True)
        self.starKiller(self.X, 1, True)
        self.starKiller(self.Y, 1, True)
        self.resolution=self.scaler.fit_transform(self.resolution)
        self.X=self.scaler.fit_transform(self.X)
        self.Y=self.scaler.fit_transform(self.Y)
    
    def getYear(self):
        return self.year
    
    def getFeatures(self):
        return self.features
    
    def getLabels(self):
        return self.labels
    
    def getMonth(self):
        return self.month
    
    def getDay(self):
        return self.day
    
    def getDayNum(self):
        return self.day_num
    
    def getMinute(self):
        return self.minute
    
    def getHour(self):
        return self.hour
    
    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    
    def getPdDistrict(self):
        return self.PdDistrict
    
    def getAddress(self):
        return self.address
    
    def getResolution(self):
        return self.resolution
    
    def getDrug(self):
        return self.drug
    
    def getLarceny(self):
        return self.larceny
    
    def getMissingPerson(self):
        return self.missing_person
    
    def getProstitution(self):
        return self.prostitution
    
    def getVehiculeTheft(self):
        return self.vehicule_theft
    
    def getWarrants(self):
        return self.warrants

    def starKiller(self, variable_name, killer, star):
        a=list()
        if star==True:
            for data in variable_name:
                if data<killer:
                    a.append(data)
            variable_name=a
        else:
            for data in variable_name:
                if data>killer:
                    a.append(data)
            variable_name=a

    def one_column(self):
        b=self.labels[:,0]*0
        for i in range(1, 6):
            b+=self.labels[:,i]*i
        self.labels=b


test=process()
self.data.describe()
self.data1.describe()
print test.getX()
print test.getY()
print test.getResolution()
print test.getLabels()


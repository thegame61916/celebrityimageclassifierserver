#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 22:05:48 2017

@author: archit.j
"""

import pickle
import glob
import os
import urllib


def storeInFile(fileName,dic):
    pickle.dump(dic, open( fileName, "wb" ))

def function(url,filePath):
    #print url
    urllib.urlretrieve(url, filePath)


def adjustUrl(url):
    ans = ""
    for i in range(0,len(url)):
        if(url[i] != '\\'):
            ans = ans + url[i]
        else:
            i = i +2
    return ans
        

#print adjustUrl("https:\\/\\/encrypted-tbn0.gstatic.com\\/images?q=tbn:ANd9GcRBmnAw-SCUEq1ZkYSjk3cxnAk4pYICy01Ym7tofi89fz_sAD53")
        
#function(adjustUrl("https:\\/\\/encrypted-tbn0.gstatic.com\\/images?q=tbn:ANd9GcRBmnAw-SCUEq1ZkYSjk3cxnAk4pYICy01Ym7tofi89fz_sAD53"),"downloadedImage.jpg")


allFolders = [x[0] for x in os.walk("/Users/archit.j/Desktop/CrawledData")][1:]

#allFolders = ["Salman Khan ", "Shah Rukh Khan ", "Virat Kohli ", "Akshay Kumar ", "Mahendra Singh Dhoni", "Deepika Padukone ", "Sachin Tendulkar ", "Priyanka Chopra", "Amitabh Bachchan ", "Hrithik Roshan ", "Kapil Sharma", "Ranveer Singh", "AR Rahman", "Aamir Khan", "Arijit Singh ", "Rohit Sharma", "Yuvraj Singh", "Sonam Kapoor", "Ranbir Kapoor", "Sonakshi Sinha", "Shahid Kapoor", "Madhuri Dixit-Nene", "Shikhar Dhawan", "Jacqueline Fernandez ", "Katrina Kaif ", "Suresh Raina", "Ravichandran Ashwin", "Shreya Ghoshal", "Sania Mirza", "Rajinikanth", "Saina Nehwal", "Sunny Leone", "Mahesh Babu", "Ajinkya Rahane", "Ravindra Jadeja", "Anushka Sharma", "Sonu Nigam", "Kareena Kapoor-Khan", "Gautam Gambhir", "Chetan Bhagat", "Virender Sehwag", "Alia Bhatt", "Allu Arjun", "Harbhajan Singh", "Shraddha Kapoor", "Shruti Haasan", "Dhanush", "Karan Johar", "Kamal Haasan", "Varun Dhawan", "Suriya", "Farhan Akhtar", "Kajal Aggarwal", "John Abraham", "Junior NTR", "Mika Singh", "Parineeti Chopra", "Kangana Ranaut", "Sunidhi Chauhan", "Vishal-Shekhar", "Vijay", "PV Sindhu", "Arjun Kapoor", "Riteish Deshmukh", "Anil Kumble", "Abhishek Bachchan", "Ram Charan", "Anupam Kher", "Saif Ali Khan", "Ajay Devgn", "Bipasha Basu", "Vikram", "Sanjeev Kapoor", "Sidharth Malhotra", "Sanjay Leela Bhansali", "Nargis Fakhri", "Navjot Singh Sidhu", "Shilpa Shetty", "Diljit Dosanjh", "Sakshi Malik", "Badshah", "All India Bakchod (AIB)", "Shankar-Ehsaan-Loy", "Shaan", "Leander Paes", "Remo D'Souza", "Anurag Kashyap", "MC Mary Kom ", "Anirban Lahiri", "Prabhudheva", "Imtiaz Ali", "Ashutosh Gowariker", "Devdutt Pattanaik", "Vir Das", "Malaika Arora Khan", "Neeraj Pandey", "Arbaaz Khan", "Bharti Singh", "Sonali Bendre Behl", "Krushna Abhishek"]

def findDescriptorsInFolder(path,dest):
    print path
    for f in glob.glob(os.path.join(path, "*")):
        dic = pickle.load(open(f,"rb"))
        temp = f.split('/')
        temp = temp[-1]
        finalDest = dest +"/"+ temp
        print finalDest
        if not os.path.exists(finalDest):
            os.makedirs(finalDest)
        count = 0
        for url in dic.keys():
            if(url[0] != 'h'):
                continue
            url = adjustUrl(url)
            finalDest2 = finalDest +"/" + temp + str(count) + ".jpg"
            #print url
            #print finalDest2
            #break
            function(url,finalDest2)
            count = count  + 1
            
    
        

findDescriptorsInFolder("/Users/archit.j/Desktop/CrawledData","/Users/archit.j/Desktop/ImageDataset")
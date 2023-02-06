# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:56:48 2023

@author: Chris Sibusiso Majuba
"""

# Question 1
#function that checks date format

def is_date_format(x):
  date = str(x)    
  #boolean statements
  year_bl  = False
  month_bl = False
  date_bl  = False
  chr_bl   = False
  
  if date.count('-') == 2:  #checking number of '-' in date
    chr_bl = True
    
  if len(date[0:4]) ==  4:  #checking length of the year
    year_bl = True
    
  if len(date[5:7]) == 2:   #checking length of the month
    month_bl = True
    
  if len(date[8:10]) == 2:  #checking length of the date
    date_bl = True

  if (year_bl and chr_bl and date_bl and month_bl) == True:
       print("Date format is valid")
       return True           #checking all the necessary conditions
  else:
      print("Invalid Format,Use this format 1998-26-12")
      return False
         
#user_date = input("Please enter date: ")
#if(is_date_format(user_date)):
 # print("Date format is valid")
#else:
 # print("Error! Invalid Format. Please follow this format 1998-26-12")


# End of question 1 *********************************************

# Question 2

for i in range(1,11):
    if i == 6:
         "do nothing"
    else:
         print(i, end = ",")
        
# End of question 2 **********************************************



#Question 3
#Function that computes previous date
def compute_prev_date(x):
  dates = list(x)
  #new dates formats list
  new_dates = []
  size_dates = len(dates)
  for i in range(0,size_dates):
      if is_date_format(dates[i]):  #checking if the date is valid
           new_dates += [date_convert(dates[i])] #converting the dates & then adding them inside a new list
      else: 
        print("Invalid date format")
  return new_dates

  
# Function that converts the dates
def date_convert(s):
    #converting strings into integers
    year  = int(s[0:4])
    month = int(s[5:7]) 
    day   = int(s[8:10])
    #new date
    new_yr = 0
    new_mo = 0
    new_day = 0
    new_month_str = ""
  #list of months in strings
    list_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    new_day = day - 1
    new_mo  = month
    new_yr  = year
    if new_day <= 0:
       new_day = 31
       new_mo  -= 1 
    if new_mo <= 0 :
       new_yr -= 1
    new_month_str = list_months[new_mo-1]
    new_format = str(new_day) +" "+ str(new_month_str) +" " + str(new_yr)
    return(new_format)
                       
#calling the function
print(compute_prev_date(["1998-12-26","2023-01-01"]))

#End of Question 3 ************************************************

#Question 4

def main():
      #Using the try block to handle errors/Exceptions
    def fetch_quantity():
       while  True: 
         try:
            """
            Returns a number, any number
            """
            x = int(input("Enter Number: "))
         #Catch the exception
         except ValueError:
                print("Please enter a valid number")
         else:
           return x
           break
             
    def fetch_cost():
       while True: 
        try:
         """
         Returns a number, any number
         """
         x = int(input("Enter Number: "))
          #Catch the exception
        except ValueError:
          print("Please enter a valid number")
        else:
         return x
         break
             
    def compute_cost_per_quantity():
      while True:
        try:
          qty  = fetch_quantity()
          cost = fetch_cost()
          cost_per_quantity = cost/qty
        #Catch the exception
        except ZeroDivisionError as err: #defining a variable err for the type of error
           print(f"Error! {err}")
            #exit function that terminates the program
           exit(1)
        else:
          return cost_per_quantity
          break  
    cost_per_quantity = compute_cost_per_quantity()
    a = 1 + 2 + cost_per_quantity
    b = 4 + 5
    print(a+b)
#calling the main function to execute 
main()

# End of question 4 *******************************************************

#Question 5

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def get_params():
  
  #http://127.0.0.1:8000/get_params?name=John&surname=Doe
 initials = str("http://127.0.0.1:8000/get_params?name=John&surname=Doe")
 content = searcher(initials)
 return Response(content, status=status.HTTP_200_OK)
  
#function that searches through the URL request
def searcher(s):
  info = str(s)
  index_num_c = info.rindex("?") #index num that will be used to separate the message
  name_surname = info[index_num_c + 1:] #name & surname inside this variable
  nam_sur_tuple = name_surname.partition("&") #separate string using '&' into tuple
  sp_name    = nam_sur_tuple[0] 
  sp_surname = nam_sur_tuple[-1]
  #indexes of the actual name and surname
  index_name    = sp_name.find("=")
  index_surname = sp_surname.find("=",index_name)
  #variables for the Content dictionary
  var_name    = sp_name[index_name + 1:]
  var_surname = sp_surname[index_surname + 1 :]
  content = { "name":var_name,
              "surname": var_surname}
  return content
  
#calling the function
#print(searcher("http://127.0.0.1:8000/get_params?name=John&surname=Doe"))

# End of Question 5 ***************************************************

# Question 6
class TestMath:
  #constructor
  def __init__(self,x = 10 ,y = 10):
    self.x = x   #attributes
    self.y = y
    
  def test_add(self,x,y):
    return x + y  
  def test_subtract(self,x,y):
    return x - y
  def test_multiply(self,x,y):
    return x * y
# End of question 6 **************************************

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:56:48 2023

@author: Chris Sibusiso Majuba
"""
import pandas as pd #dependency
import numpy as np #dependency

#Class for Teachers
class Teacher:
  def __init__(self, name, married,school):
    self.name     = name
    self.married  = married
    self.school   = school
    self.students = []
    # Method that prints info to screen
  def teach_info(self):
    teach_dict = {}
    teach_dict["teacher"]  = self.name
    teach_dict["school"]   = self.school
    teach_dict["married"]  = self.married 
    teach_dict["students"] = self.students
    print(teach_dict)
  
  def set_student(self, std_name, std_age, std_height):
      student_info = {}
      student_info["name"]   = std_name
      student_info["age"]    = std_age
      student_info["height"] = std_height
      self.students.append(student_info)
    
#class for the students
class Student:
  def __init__(self, st_teacher, st_name, st_age, st_height):
    self.st_teacher = st_teacher
    self.st_name    = st_name
    self.st_age     = st_age
    self.st_height  = st_height
    # Method that adds new student infomation
  def add_new_info(self, keyword , key_variable):
    self.keyword = keyword
  
#function that puts data from teacher dataframe into a list of Teacher class instances
def put_teachers():
  df_teacher = pd.DataFrame({
 "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
"married": [True, True, False, True],
"school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})
  _size         = len(df_teacher["name"]) #get the length of list
  teachers_list = []
  for i in range(0,_size):  
    t_name    = df_teacher["name"][i]
    t_married = df_teacher["married"][i]
    t_school  = df_teacher["school"][i]
    #Create a new Teacher class every time we iterate
    teacher = Teacher(t_name,t_married,t_school)
    teachers_list.append(teacher) #add to list
  return teachers_list
#Function that Converts student dataframe to a list of student class instances
def put_students():
  df_student = pd.DataFrame({
  "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
  "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
  "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
  "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
  "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
  })
  student_list = []
  _size = len(df_student["teacher"])
  for i in range(0,_size):
    t_name   = df_student["teacher"][i]
    s_name   = df_student["name"][i]
    s_age    = df_student["age"][i]
    s_height = df_student["height"][i]
    good_student = Student(t_name, s_name, s_age, s_height)
    student_list.append(good_student)
  return student_list 
# converting pd_database data into list of Teacher & Student class instances
list_of_teachers = put_teachers()
list_of_students = put_students()

for i in range(0,len(list_of_students)):
  # searching for teacher's name in the list of student class instances  
  if list_of_students[i].st_teacher == "Mikel Arteta":
    for y in range(0,len(list_of_teachers)):
      # searching for the same teacher name but in the list of the teacher class instances
      if list_of_teachers[y].name == "Mikel Arteta":
        s_name = list_of_students[i].st_name
        s_age  = list_of_students[i].st_age
        s_hei  = list_of_students[i].st_height
        list_of_teachers[y].set_student(s_name, s_age, s_hei)
        
  elif list_of_students[i].st_teacher == "Pep Guardiola":
    for y in range(0,len(list_of_teachers)):
      # searching for the same teacher name but in the list of the teacher class instances
      if list_of_teachers[y].name == "Pep Guardiola":
        s_name = list_of_students[i].st_name
        s_age  = list_of_students[i].st_age
        s_hei  = list_of_students[i].st_height
        list_of_teachers[y].set_student(s_name, s_age, s_hei)
        
  elif list_of_students[i].st_teacher == "Jurgen Klopp":
    for y in range(0,len(list_of_teachers)):
      # searching for the same teacher name but in the list of the teacher class instances
      if list_of_teachers[y].name == "Jurgen Klopp":
        s_name = list_of_students[i].st_name
        s_age  = list_of_students[i].st_age
        s_hei  = list_of_students[i].st_height
        list_of_teachers[y].set_student(s_name, s_age, s_hei)

#Printing the infomation on screen
for i in range(0,len(list_of_teachers)):
  list_of_teachers[i].teach_info()

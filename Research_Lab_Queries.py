import mysql.connector

#Function to run a MySQL query
def run_query(cursor, query): 
    temp = cursor.cursor()
    print("Running Query: ", query)
    temp.execute(query)

    #Select statement case
    if query.strip().lower().startswith("select"): 
        result = temp.fetchall()
        print(result)
    
    #Modification statement case
    if query.strip().lower().startswith(("insert", "update", "delete", "create", "drop", "use")): cursor.commit()

#Server connection initialization
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MySQL_2025" #Replace with your password
)

print(mydb)

#Creating a new database
run_query(mydb, "drop database if exists Research_Lab;")
run_query(mydb, "create database if not exists Research_Lab;")
run_query(mydb, "use Research_Lab;")

#Dropping Tables before creating them
run_query(mydb, "drop table if exists Authorship;")
run_query(mydb, "drop table if exists Publication;")

run_query(mydb, "drop table if exists Lab_Working;")
run_query(mydb, "drop table if exists Funding;")
run_query(mydb, "drop table if exists Project_Grant;")
run_query(mydb, "drop table if exists Project;")

run_query(mydb, "drop table if exists Equipment_Usage;")
run_query(mydb, "drop table if exists Equipment;")

run_query(mydb, "drop table if exists Student;")
run_query(mydb, "drop table if exists Faculty;")
run_query(mydb, "drop table if exists External_Collaborator;")
run_query(mydb, "drop table if exists Mentorship;")
run_query(mydb, "drop table if exists Lab_Member;")

#Creating Tables for the database
run_query(mydb, "create table Lab_Member (Member_ID int Primary Key, Member_Name Varchar(255) not null, Member_Type Varchar(31) not null, Join_Date Date not null);")

run_query(mydb, "create table Student (Member_ID int Primary Key, Student_Number int not null, Academic_Level Varchar(31) not null, Major Varchar(31) not null, Foreign key (Member_ID) references Lab_Member(Member_ID), Unique (Member_ID, Student_Number));")

run_query(mydb, "create table Faculty (Member_ID int Primary Key, Department Varchar(31) not null, Foreign Key (Member_ID) references Lab_Member(Member_ID));")

run_query(mydb, "create table External_Collaborator ( Member_ID int Primary Key, Institutional_Affiliation Varchar(255) not null, Biography Varchar(255) not null, Foreign Key (Member_ID) references Lab_Member(Member_ID));")

run_query(mydb, "create table Mentorship(Mentor_ID int not null, Mentee_ID int not null, Start_Date date not null, End_Date date not null, primary key (Mentor_ID, Mentee_ID), foreign key (Mentor_ID) references Lab_Member(Member_ID), foreign key (Mentee_ID) references Lab_Member(Member_ID));")

run_query(mydb, "create table Equipment (ID int primary key, Equipment_Name varchar(31) not null, Equipment_Type varchar(31) not null, Purchase_Date date not null, Equipment_Status varchar(15) not null);")

run_query(mydb, "create table Equipment_Usage ( Equipment_ID int not null, Member_ID int not null, Purpose_of_Use varchar(255) not null, Start_Date date not null, End_Date date not null, primary key (Equipment_ID, Member_ID), foreign key (Equipment_ID) references Equipment(ID), foreign key (Member_ID) references Lab_Member(Member_ID));")

run_query(mydb, "create table Project(Project_ID int Primary Key, Faculty_ID int not null, Title Varchar(31) not null, Start_Date Date not null, End_Date Date not null, Project_Status Varchar(15) not null, Expected_Duration Varchar(63) not null, Foreign Key (Faculty_ID) references Faculty(Member_ID));")

run_query(mydb, "create table Lab_Working( Member_ID int not null, Project_ID int not null, Weekly_Hours int not null, Project_Role varchar(31) not null, primary key (Member_ID, Project_ID), foreign key (Member_ID) references Lab_Member(Member_ID), foreign key (Project_ID) references Project(Project_ID));")

run_query(mydb, "create table Project_Grant( ID int Primary Key, Grant_Source Varchar(31) not null, Duration Varchar(63) not null, Start_Date Date not null, Budget int not null, Reporting_Requirement Varchar(255) not null);")

run_query(mydb, "create table Funding( Project_ID int not null, Grant_ID int not null, primary key (Project_ID, Grant_ID), foreign key (Project_ID) references Project(Project_ID), foreign key (Grant_ID) references Project_Grant(ID));")

run_query(mydb, "create table Publication (ID int primary key, Title varchar(63) not null, Month_Date int not null, Year_Date int not null, Venue varchar(63) not null, DOI varchar(63) not null);")

run_query(mydb, "create table Authorship( Member_ID int not null, Publication_ID int not null, primary key (Member_ID, Publication_ID), foreign key (Member_ID) references Lab_Member(Member_ID), foreign key (Publication_ID) references Publication(ID));")

#Insert Table Statements
run_query(mydb, "insert into Lab_Member(Member_ID, Member_Name, Member_Type, Join_Date) values (100, 'John', 'Student', '2019-09-30'), (101, 'Smith', 'Faculty', '2018-05-17'), (102, 'Franklin', 'External Collaborator', '2019-10-12'), (103, 'Wong', 'Student', '2018-11-01'), (104, 'Alicia', 'Faculty', '2013-05-17'), (105, 'Zelaya', 'External Collaborator', '1998-10-12'), (106, 'Jennifer', 'Student', '2019-10-23'), (107, 'Wallace', 'Faculty', '2014-05-17'), (108, 'Ramesh', 'External Collaborator', '1998-10-12'), (109, 'Narayan', 'Student', '2016-08-30'), (110, 'Joyce', 'Faculty', '2017-05-20'), (111, 'English', 'External Collaborator', '1998-10-12'), (112, 'Ahmad', 'Student', '2019-06-22'), (113, 'James', 'Faculty', '2018-08-08'), (114, 'Borg', 'External Collaborator', '1998-10-12'), (115, 'Michael', 'Student', '2019-12-30'), (116, 'Ron', 'Student', '2018-01-27'), (117, 'Wade', 'Student', '2015-10-03'), (118, 'Trace', 'Student', '2018-10-04'), (119, 'Rachel', 'Student', '2019-09-30');")
    
run_query(mydb, "insert into Student(Member_ID, Student_Number, Academic_Level, Major) values (100, 1000, 'Freshman', 'Computer Science'), (103, 1001, 'Sophomore', 'Mathematics'), (106, 1002, 'Freshman', 'Accounting'), (109, 1003, 'Senior', 'Computer Science'), (112, 1004, 'Junior', 'Biology'), (115, 1005, 'Sophomore', 'Chemistry'), (116, 1006, 'Junior', 'Accounting'), (117, 1007, 'Freshman', 'Chemistry'), (118, 1008, 'Senior', 'Mathematics'), (119, 1009, 'Junior', 'Computer Science');")
    
run_query(mydb, "insert into Faculty(Member_ID, Department) values (101, 'Theoretical Chemistry'), (104, 'Mechanical and Current Physics'), (107, 'Calculus'), (110, 'Psychology and Arts'), (113, 'Commerce');")
    
run_query(mydb, "insert into External_Collaborator(Member_ID, Institutional_Affiliation, Biography) values (102, 'NJIT', 'He has a Masters in Computer Science and has over 8 years of experience as a professor in MIT.'), (105, 'Rutgers', 'She has done a Doctorate and has contributed a lot in the field of programming.'), (108, 'Harvard', 'He has worked in the accounting field for over 30 years and is currently a professor at Harvard for over 5 years.'), (111, 'NJIT', 'External Collaborator'), (114, 'NJIT', 'External Collaborator');")

run_query(mydb, "insert into Mentorship(Mentor_ID, Mentee_ID, Start_Date, End_Date) values(101, 100, '2019-10-02', '2023-04-28'), (104, 100, '2019-11-12', '2022-08-19'), (107, 103, '2018-11-01', '2020-11-30'), (107, 119, '2019-10-10', '2024-05-01');")
    
run_query(mydb, "insert into Equipment(ID, Equipment_Name, Equipment_Type, Purchase_Date, Equipment_Status) values(100000, 'Test Tubes', 'Chemistry Lab Equipments', '2004-10-19', 'In Use'), (100001, 'Hydraulic Press', 'Mechanical Equipments', '2005-09-26', 'Not in Use'), (100002, 'Bunsen Burner', 'Chemistry Lab Equipments', '2003-01-30', 'In Use'), (100003, 'Monitor sets', 'Computer Lab Equipments', '2006-05-23', 'Not in Use'), (100004, 'Microscopes', 'Biology Lab Equipments', '2004-11-16', 'In Use'), (100005, 'Chemical Boxes', 'Chemistry Lab Equipments', '2002-10-13', 'In Use'), (100006, 'Pendulum Sets', 'Mechanical Equipments', '2005-08-09', 'Not in Use');")

run_query(mydb, "insert into Equipment_Usage(Equipment_ID, Member_ID, Purpose_of_Use, Start_Date, End_Date) values(100000, 101, 'Chemical Reactions', '2019-09-30', '2021-10-15'), (100000, 111, 'Chemical Reactions', '2019-09-30', '2021-10-15'), (100002, 101, 'Chemistry Reactions', '2020-01-24', '2021-10-15'), (100004, 112, 'Biology Research', '2018-11-04', '2022-05-09'), (100005, 111, 'Chemistry Reactions', '2020-10-13', '2023-12-01');")

run_query(mydb, "insert into Project(Project_ID, Faculty_ID, Title, Start_Date, End_Date, Project_Status, Expected_Duration) values(0, 101, 'ProductX', '2018-08-29', '2026-04-05', 'Ongoing', '7 years 8 months'), (1, 104, 'Machine Designing', '2019-10-11', '2024-11-18', 'Completed', '5 years 1 month'), (2, 107, 'Complex Integration', '2017-01-14', '2025-12-01', 'Completed', '8 years 11 months'), (3, 110, 'Exhibition', '2020-10-04', '2027-04-05', 'Ongoing', '6 years 6 months'), (4, 113, 'Scaling of Economy', '2018-05-17', '2019-10-19', 'Completed', '1 year 5 months');")

run_query(mydb, "insert into Lab_Working(Member_ID, Project_ID, Weekly_Hours, Project_Role) values (101, 0, 48, 'Project Leader'), (100, 0, 40, 'Developer'), (102, 0, 36, 'Developer'), (105, 0, 40, 'Developer'), (108, 0, 39, 'Developer'), (115, 0, 37, 'Developer'), (104, 1, 48, 'Project Leader'), (101, 1, 40, 'Developer'), (103, 1, 37, 'Developer'), (106, 1, 38, 'Developer'), (109, 1, 40, 'Developer'), (107, 2, 48, 'Project Leader'), (104, 2, 39, 'Developer'), (111, 2, 36, 'Developer'), (112, 2, 37, 'Developer'),(116, 2, 36, 'Developer'), (110, 3, 48, 'Project Leader'), (107, 3, 40, 'Developer'),  (114, 3, 42, 'Developer'), (117, 3, 39, 'Developer'), (118, 3, 41, 'Developer'), (113, 4, 48, 'Project Leader'), (110, 4, 40, 'Developer'), (119, 4, 40, 'Developer'), (102, 4, 39, 'Developer'), (103, 4, 35, 'Developer');")

run_query(mydb, "insert into Project_Grant(ID, Grant_Source, Duration, Start_Date, Budget, Reporting_Requirement) values (2000, 'NSF', '2 years', '2023-01-01', 500000, 'Quarterly reports, Member Roles and updates'), (2001, 'NIH', '3 years', '2022-06-15', 750000, 'Annual reviews'), (2002, 'DoE', '1 year', '2024-03-20', 300000, 'Semi-annual financials'), (2003, 'DARPA', '4 years', '2021-11-01', 1200000, 'Quarterly and annual review'), (2004, 'NASA', '2 years', '2023-05-10', 650000, 'Annual technical report');")

run_query(mydb, "insert into Funding(Project_ID, Grant_ID) values (0, 2000), (1, 2001), (2, 2002), (3, 2003), (4, 2004);")

run_query(mydb, "insert into Publication(ID, Title, Month_Date, Year_Date, Venue, DOI) values (300, 'Revolutionary Science', 5, 2024, 'California', '10.1000/aihc2024'), (301, 'Technology in theory', 6, 2023, 'Washington', '10.1000/rs2023'), (302, 'Energy-Efficient Systems', 3, 2022, 'New York', '10.1000/ees2022'), (303, 'Data Modeling Advances', 9, 2024, 'England', '10.1000/dma2024'), (304, 'Physical Prodigy', 11, 2023, 'Germany', '10.1000/qn2023');")

run_query(mydb, "insert into Authorship(Member_ID, Publication_ID) values (100, 300),  (101, 300),  (104, 300), (102, 301),  (107, 301),  (113, 301), (103, 302),  (110, 302), (105, 303),  (111, 303),  (118, 303), (109, 304),  (114, 304),  (119, 304);")

#Select table statements
run_query(mydb, "select count(*) from Lab_Member;")
run_query(mydb, "select count(*) from Student;")
run_query(mydb, "select count(*) from Faculty;")
run_query(mydb, "select count(*) from External_Collaborator;")
run_query(mydb, "select count(*) from Mentorship;")
run_query(mydb, "select count(*) from Equipment;")
run_query(mydb, "select count(*) from Equipment_Usage;")
run_query(mydb, "select count(*) from Project;")
run_query(mydb, "select count(*) from Lab_Working;")
run_query(mydb, "select count(*) from Project_Grant;")
run_query(mydb, "select count(*) from Funding;")
run_query(mydb, "select count(*) from Publication;")
run_query(mydb, "select count(*) from Authorship;")
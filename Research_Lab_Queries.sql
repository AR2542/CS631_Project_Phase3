create database if not exists Research_Lab;

use Research_Lab;

drop table if exists Authorship;
drop table if exists Publication;

drop table if exists Lab_Working;
drop table if exists Funding;
drop table if exists Project_Grant;
drop table if exists Project;

drop table if exists Equipment_Usage;
drop table if exists Equipment;

drop table if exists Student;
drop table if exists Faculty;
drop table if exists External_Collaborator;
drop table if exists Mentorship;
drop table if exists Lab_Member;

create table Lab_Member (
    Member_ID int Primary Key,
    Member_Name Varchar(255) not null,
    Member_Type Varchar(31) not null,
    Join_Date Date not null
);

create table Student (
    Member_ID int Primary Key,
    Student_Number int not null,
    Academic_Level Varchar(31) not null,
    Major Varchar(31) not null,
    Foreign key (Member_ID) references Lab_Member(Member_ID),
    Unique (Member_ID, Student_Number)
);

create table Faculty (
    Member_ID int Primary Key,
    Department Varchar(31) not null,
    Foreign Key (Member_ID) references Lab_Member(Member_ID)
);

create table External_Collaborator (
    Member_ID int Primary Key,
    Institutional_Affiliation Varchar(255) not null,
    Biography Varchar(255) not null,
    Foreign Key (Member_ID) references Lab_Member(Member_ID)
);

create table Mentorship(
    Mentor_ID int not null,
    Mentee_ID int not null,
    Start_Date date not null,
    End_Date date not null,
    primary key (Mentor_ID, Mentee_ID),
    foreign key (Mentor_ID) references Lab_Member(Member_ID),
    foreign key (Mentee_ID) references Lab_Member(Member_ID)
);

create table Equipment (
    ID int primary key,
    Name varchar(31) not null,
    Type varchar(31) not null,
    Purchase_Date date not null,
    Status varchar(15) not null
);

create table Equipment_Usage (
    Equipment_ID int not null,
    Member_ID int not null,
    Purpose_of_Use varchar(255) not null,
    Start_Date date not null,
    End_Date date not null,
    primary key (Equipment_ID, Member_ID),
    foreign key (Equipment_ID) references Equipment(ID),
    foreign key (Member_ID) references Lab_Member(Member_ID)
);

create table Project(
    Project_ID int Primary Key,
    Faculty_ID int not null,
    Title Varchar(31) not null,
    Start_Date Date not null,
    End_Date Date not null,
    Project_Status Varchar(15) not null,
    Expected_Duration Varchar(63) not null,
    Foreign Key (Faculty_ID) references Faculty(Member_ID)
);

create table Lab_Working(
    Member_ID int not null,
    Project_ID int not null,
    Weekly_Hours int not null,
    Role varchar(31) not null,
    primary key (Member_ID, Project_ID),
    foreign key (Member_ID) references Lab_Member(Member_ID),
    foreign key (Project_ID) references Project(Project_ID)
);

create table Project_Grant(
    ID int Primary Key,
    Grant_Source Varchar(31) not null,
    Duration Varchar(63) not null,
    Start_Date Date not null,
    Budget int not null,
    Reporting_Requirement Varchar(255) not null
);

create table Funding(
    Project_ID int not null,
    Grant_ID int not null,
    primary key (Project_ID, Grant_ID),
    foreign key (Project_ID) references Project(Project_ID),
    foreign key (Grant_ID) references Project_Grant(ID)
);

create table Publication (
    ID int primary key,
    Title varchar(63) not null,
    Month_Date int not null,
    Year_Date int not null,
    Venue varchar(63) not null,
    DOI varchar(63) not null
);

create table Authorship(
    Member_ID int not null,
    Publication_ID int not null,
    primary key (Member_ID, Publication_ID),
    foreign key (Member_ID) references Lab_Member(Member_ID),
    foreign key (Publication_ID) references Publication(ID)
);

insert into Lab_Member(Member_ID, Member_Name, Member_Type, Join_Date) values 
    (100, 'John', 'Student', '2019-09-30'),
    (101, 'Smith', 'Faculty', '2018-05-17'),
    (102, 'Franklin', 'External Collaborator', '2019-10-12'),
    (103, 'Wong', 'Student', '2018-11-01'),
    (104, 'Alicia', 'Faculty', '2003-05-17'),
    (105, 'Zelaya', 'External Collaborator', '1998-10-12'),
    (106, 'Jennifer', 'Student', '2019-09-30'),
    (107, 'Wallace', 'Faculty', '2003-05-17'),
    (108, 'Ramesh', 'External Collaborator', '1998-10-12'),
    (109, 'Narayan', 'Student', '2019-09-30'),
    (110, 'Joyce', 'Faculty', '2003-05-17'),
    (111, 'English', 'External Collaborator', '1998-10-12'),
    (112, 'Ahmad', 'Student', '2019-09-30'),
    (113, 'James', 'Faculty', '2003-05-17'),
    (114, 'Borg', 'External Collaborator', '1998-10-12'),
    (115, 'Michael', 'Student', '2019-09-30'),
    (116, 'Ron', 'Student', '2019-09-30'),
    (117, 'Wade', 'Student', '2019-09-30'),
    (118, 'Trace', 'Student', '2019-09-30'),
    (119, 'Rachel', 'Student', '2019-09-30');
    
select count(*) from Lab_Member;
    
insert into Student(Member_ID, Student_Number, Academic_Level, Major) values
    (100, 1000, 'Freshman', 'Computer Science'),
    (103, 1001, 'Sophomore', 'Mathematics'),
    (106, 1002, 'Freshman', 'Accounting'),
    (109, 1003, 'Senior', 'Computer Science'),
    (112, 1004, 'Junior', 'Biology'),
    (115, 1005, 'Sophomore', 'Chemistry'),
    (116, 1006, 'Junior', 'Accounting'),
    (117, 1007, 'Freshman', 'Chemistry'),
    (118, 1008, 'Senior', 'Mathematics'),
    (119, 1009, 'Junior', 'Computer Science');

select count(*) from Student;

insert into Faculty(Member_ID, Department) values 
    (101, 'Theoretical Chemistry'),
    (104, 'Mechanical and Current Physics'),
    (107, 'Calculus'),
    (110, 'Psychology and Arts'),
    (113, 'Commerce');
    
select count(*) from Faculty;
    
insert into External_Collaborator(Member_ID, Institutional_Affiliation, Biography) values 
    (102, 'NJIT', 'He has a Masters in Computer Science and has over 8 years of experience as a professor in MIT.'),
    (105, 'Rutgers', 'She has done a Doctorate and has contributed a lot in the field of programming.'),
    (108, 'Harvard', 'He has worked in the accounting field for over 30 years and is currently a professor at Harvard for over 5 years.'),
    (111, 'NJIT', 'External Collaborator'),
    (114, 'NJIT', 'External Collaborator');

select count(*) from External_Collaborator;

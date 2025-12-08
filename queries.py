
QUERIES_1 = { #  PROJECT AND MEMBER MANAGEMENT
    # Query to fetch lab members
    'Query to fetch lab members': """
        SELECT * FROM lab_member
        WHERE MEMBER_ID IN ({placeholder});""",
    # Query to fetch projects
    'Query to fetch projects': """
        SELECT * FROM project
        WHERE PROJECT_ID IN ({placeholder});""",
    # Display status of a project
    'Display status of a project': """
        SELECT project_id, project_status from project WHERE project_id in ({placeholder});""",
    # Show members who have worked on projects funded by a given grant
    'Show members who have worked on projects funded by a given grant': """
        SELECT M.MEMBER_ID, M.MEMBER_NAME
        FROM lab_member M, funding F, project P, lab_working LW
        WHERE M.MEMBER_ID = LW.MEMBER_ID AND LW.PROJECT_ID = P.PROJECT_ID
        AND P.PROJECT_ID = F.PROJECT_ID AND F.GRANT_ID IN ({placeholder});""",
    # Show mentorship relations among members who have worked on the same project.
    'Show mentorship relations among members who have worked on the same project': """
        SELECT DISTINCT M.MENTOR_ID, M.MENTEE_ID
        FROM MENTORSHIP M JOIN LAB_WORKING LW1 ON M.MENTOR_ID = LW1.MEMBER_ID
        JOIN LAB_WORKING LW2 ON M.MENTEE_ID = LW2.MEMBER_ID AND LW1.PROJECT_ID = LW2.PROJECT_ID;""",
    # Add lab members
    'Add lab members': """
        insert into Lab_Member(Member_ID, Member_Name, Member_Type, Join_Date) values 
        ({placeholder});""",
    # Add projects
    'Add projects': """
        insert into Project(Project_ID, Faculty_ID, Title, Start_Date, End_Date, Project_Status, Expected_Duration) values
        ({placeholder});,""",
    # Update members
    'Update members': """ UPDATE Lab_Member
                         SET Member_Type=(%s), Join_Date=(%s)
                         WHERE Member_ID = (%s);""",
    # Update projects
    'Update projects': """UPDATE PROJECT
                         SET Start_Date=(%s), End_Date=(%s), Project_Status=(%s), Expected_Duration=(%s)
                         WHERE Project_ID = (%s);""",
    # Delete member
    'Delete member': """DELETE FROM LAB_MEMBER
                        WHERE MEMBER_ID = (%s);""",
    # Delete project
    'Delete project': """DELETE FROM PROJECT
                         WHERE PROJECT_ID = (%s);"""
}

QUERIES_2 = { # EQUIPEMENT USAGE TRACKING
    # Query to fetch equipments
    'Query to fetch equipments': """SELECT * FROM EQUIPMENT
                          WHERE ID IN ({placeholder});""",
    # Query to fetch equipment usages
    'Query to fetch equipment usages': """SELECT * FROM EQUIPMENT_USAGE
                          WHERE EQUIPMENT_ID IN ({placeholder});""",
    # Query to show status of a equipement
    'Query to show status of a equipement': """SELECT ID, EQUIPMENT_STATUS FROM EQUIPMENT
                              WHERE ID IN ({placeholder});""",
    # Show members currently using a given piece of equipment and the projects they are working on
    'Show members currently using a given piece of equipment and the projects they are working on': """SELECT  EQUIPMENT_ID, LM.MEMBER_ID, LM.MEMBER_NAME, LW.PROJECT_ID
                                FROM EQUIPMENT_USAGE EU, LAB_MEMBER LM, LAB_WORKING LW
                                WHERE LM.MEMBER_ID = EU.MEMBER_ID
                                AND LW.MEMBER_ID = LM.MEMBER_ID
                                AND EQUIPMENT_ID IN ({placeholder});""",
    # Add equipment
    'Add equipment': """
        insert into Equipment(ID, Equipment_Name, Equipment_Type, Purchase_Date, Equipment_Status) values
        ({placeholder});""",
    # Add equipment usage
    'Add equipment usage': """
        insert into Equipment_Usage(Equipment_ID, Member_ID, Purpose_of_Use, Start_Date, End_Date) values
        ({placeholder});,""",
    # Update equipment 
    'Update equipment': """ UPDATE EQUIPMENT
                         SET EQUIPMENT_STATUS=(%s)
                         WHERE ID = (%s);""",
    # Update equipment usage
    'Update equipment usage': """UPDATE Equipment_Usage
                         SET Start_Date=(%s), End_Date=(%s), Member_ID=(%s), Purpose_of_Use=(%s)
                         WHERE Equipment_ID = (%s), Member_ID=(%s);""",
    # Delete equipment
    'Delete equipment usage': """DELETE FROM EQUIPMENT
                        WHERE ID = (%s);""",
    # Delete equipment usage
    'Delete equipment usage': """DELETE FROM Equipment_Usage
                         WHERE Equipment_ID = (%s), Member_ID=(%s);"""
}

QUERIES_3 = { # GRANT AND PUBLICATION REPORTING
    # Identify the name of the member(s) with the highest number of publications
    'Identify the name of the member(s) with the highest number of publications': """ SELECT MEMBER_NAME FROM LAB_MEMBER NATURAL JOIN AUTHORSHIP
                         GROUP BY MEMBER_ID, MEMBER_NAME
                         HAVING COUNT(PUBLICATION_ID) = (SELECT MAX(PUBCOUNTS)
                                                         FROM (SELECT COUNT(PUBLICATION_ID) AS PUBCOUNTS
                                                               FROM AUTHORSHIP
                                                               GROUP BY MEMBER_ID));""",
    # Calculate the average number of student publications per major
    'Calculate the average number of student publications per major': """ SELECT MAJOR, AVG(PUBCOUNTS)
                             FROM (SELECT MEMBER_ID, MAJOR, COUNT(PUBLICATION_ID) AS PUBCOUNTS
                                   FROM STUDENT NATURAL JOIN LAB_MEMBER NATURAL JOIN AUTHORSHIP
                                   GROUP BY MEMBER_ID, MAJOR)
                             GROUP BY MAJOR;""",
    # Find the number of projects that were funded by a grant and were active during a given period of time.
    'Find the number of projects that were funded by a grant and were active during a given period of time':""" SELECT COUNT(*)
                                 FROM (PROJECT NATURAL JOIN FUNDING)
                                 WHERE START_DATE >= (%s) AND END_DATE <= (%s);""",
    # Find the three most prolific members who have worked on a project funded by a given grant.
    # Assuming by prolific they mean has the highest number of weekly hours of involvement
    'Find the three most prolific members who have worked on a project funded by a given grant': """ SELECT MEMBER_ID
                              FROM (SELECT PROJECT_ID FROM FUNDING NATURAL JOIN PROJECT
                                    WHERE GRANT_ID = (%s)) NATURAL JOIN LAB_WORKING 
                              ORDER BY WEEKLY_HOURS DESC
                              LIMIT 3;"""
}
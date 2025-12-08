-- -- QUERY: get_all_members
-- SELECT * FROM lab_member;

-- -- QUERY: get_all_projects
-- SELECT * FROM project;

DESC lab_working;

select * from lab_working;

-- QUERY: get_project_status
-- SELECT Project_ID, Project_Status from project
-- WHERE Project_ID IN (%s);

-- -- QUERY: get_project_members
-- SELECT m.*, p.project_id 
-- FROM member m
-- JOIN works_on wo ON m.member_id = wo.member_id
-- JOIN project p ON wo.project_id = p.project_id
-- WHERE p.project_id = %s;
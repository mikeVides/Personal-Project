-- Created our Database
-- CREATE DATABASE start_project;

USE start_project;

CREATE TABLE data_collected (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Employee_ID VARCHAR(255),
    Age INT,
    Gender VARCHAR(255),
    Job_Role VARCHAR(255),
    Industry VARCHAR(255),
    Years_of_Experience INT,
    Work_Location VARCHAR(255),
    Hours_Worked_Per_Week INT,
    Number_of_Virtual_Meetings INT,
    Work_Life_Balance_Rating INT,
    Stress_Level VARCHAR(255),
    Mental_Health_Condition VARCHAR(255),
    Access_to_Mental_Health_Resources VARCHAR(255),
    Productivity_Change VARCHAR(255),
    Social_Isolation_Rating INT,
    Satisfaction_with_Remote_Work VARCHAR(255),
    Company_Support_for_Remote_Work INT,
    Physical_Activity VARCHAR(255),
    Sleep_Quality VARCHAR (255),
    Region VARCHAR(255)
);


DROP TABLE data_collected;
-- Creating view SQL statement
CREATE VIEW need_meeting AS SELECT name FROM students WHERE students.score < 80 OR DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH);

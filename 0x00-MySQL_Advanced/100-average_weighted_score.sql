-- Task: Create a stored procedure to compute and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER &&
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id int)
BEGIN
	DECLARE total_weights INT DEFAULT 0;
	SELECT SUM(weight) INTO total_weights FROM projects WHERE id IN (SELECT project_id FROM corrections WHERE user_id = user_id);
	UPDATE users SET average_score = (SELECT SUM(crn.score * prj.weight / total_weights) FROM corrections crn LEFT JOIN projects prj ON crn.project_id = prj.id WHERE crn.user_id = user_id) WHERE id = user_id;
END &&
DELIMITER ;

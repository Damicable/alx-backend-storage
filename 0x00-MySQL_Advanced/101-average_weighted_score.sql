-- A stored procedure for the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER &&
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE row_id INT;
        DECLARE total_weights INT DEFAULT 0;
	DECLARE my_cursor CURSOR FOR SELECT id FROM users;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	OPEN my_cursor;

	read_loop: LOOP
		FETCH my_cursor INTO row_id;
		IF done THEN
			LEAVE read_loop;
		END IF;

		SELECT SUM(weight) INTO total_weights FROM projects WHERE id IN (SELECT project_id FROM corrections WHERE user_id = row_id);
		IF total_weights > 0 THEN
			UPDATE users SET average_score = (SELECT SUM(crn.score * prj.weight / total_weights) FROM corrections crn LEFT JOIN projects prj ON crn.project_id = prj.id WHERE crn.user_id = row_id) WHERE id = row_id;
		END IF;
	END LOOP;
	CLOSE my_cursor;
END &&
DELIMITER ;

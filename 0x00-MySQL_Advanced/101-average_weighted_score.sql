-- A stored procedure for the average weighted score for a student.

-- SQL script to create the stored procedure
DELIMITER //

-- Create stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- SQL query to calculate and store the average weighted score for a user
    INSERT INTO average_weighted_scores (user_id, average_score)
    SELECT user_id, SUM(score * weight) / SUM(weight) AS weighted_average
    FROM scores
    WHERE user_id = user_id
    GROUP BY user_id;

END //

DELIMITER ;

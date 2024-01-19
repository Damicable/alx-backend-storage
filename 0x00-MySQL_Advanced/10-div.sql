-- Creating a function
DELIMITER &&
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
	DECLEAR result FLOAT DEFAULT 0;
	IF b != 0 THEN
		SET result = a / b;
	END IF;
	RETURN result;

END &&
DELIMITER ;

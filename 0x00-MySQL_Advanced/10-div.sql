-- Create a function SafeDiv
DELIMITER &&
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
	DECLARE result FLOAT DEFAULT 0;
	IF b != 0 THEN
		SET result = a / b;
	END IF;
	RETURN result;
END &&
DELIMITER ;

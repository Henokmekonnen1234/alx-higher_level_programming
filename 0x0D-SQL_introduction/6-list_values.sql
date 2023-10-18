DELIMITER //

CREATE PROCEDURE checkAndSelectTable()
BEGIN
	  DECLARE tableExists INT;
	  
	  -- Check if the table exists
  SELECT 1 INTO tableExists FROM information_schema.TABLES WHERE TABLE_NAME = 'first_name';
  
  IF tableExists = 1 THEN
	    -- Table exists, so select its data
    SELECT * FROM first_name;
  ELSE
	    -- Table does not exist
    SELECT 'the table first_name does not exist.';
  END IF;
END //

DELIMITER ;

-- Call the stored procedure
CALL checkAndSelectTable();


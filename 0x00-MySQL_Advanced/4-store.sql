-- New order decrement trigger script
DROP TRIGGER IF EXISTS item_dcr_tr;
DELIMITER &&
CREATE TRIGGER item_dcr_tr AFTER INSERT ON orders
	FOR EACH ROW
	BEGIN
		UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
	END &&
DELIMITER ;

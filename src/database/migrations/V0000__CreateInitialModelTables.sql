CREATE TABLE mehrainbot_db.request_item (
    id INT AUTO_INCREMENT,
    discord_id BIGINT,
    poe_session_id BIGINT,
    item_name varchar(255),
    currency varchar(25),
    currency_amount DOUBLE,
    league varchar(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (ID)
);
--TODO pull items from poe.ninja API to check for occurences of the item name. 
-- Discord <- <JOUW_BOT> -> POE API


-- Requester
-- Item Name (ID?)
-- Currency
-- Amount
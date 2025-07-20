SHOW TABLES; 

--@block
DROP TABLE calorie_intake;

--@block
TRUNCATE TABLE calorie_intake;

--@block
CREATE TABLE calorie_intake (
    user_id INT PRIMARY KEY,
    breakfast INT DEFAULT 0,
    lunch INT DEFAULT 0,
    dinner INT DEFAULT 0,
    snacks INT DEFAULT 0,
    daily_goal INT DEFAULT 2365
);


--@block
INSERT INTO calorie_intake (user_id, breakfast, lunch, dinner, snacks, daily_goal) 
VALUES (1, 500, 0, 0, 0, 2000) 
ON DUPLICATE KEY UPDATE 
    breakfast=VALUES(breakfast), 
    lunch=VALUES(lunch), 
    dinner=VALUES(dinner), 
    snacks=VALUES(snacks);

--@block
UPDATE calorie_intake
SET breakfast = 500, lunch = 500, dinner = 500, snacks = 500
WHERE user_id = 1;

--@block
Desc calorie_intake;

--@block
SELECT * FROM calorie_intake;

--@block
CREATE TABLE registration (
  age TINYINT UNSIGNED NOT NULL,
  weight SMALLINT UNSIGNED NOT NULL,
  height SMALLINT UNSIGNED NOT NULL,
  gender ENUM('m', 'f') NOT NULL,
  bmi FLOAT DEFAULT NULL,
  bmi_category VARCHAR(100) DEFAULT NULL,
  bfp VARCHAR(4) DEFAULT NULL,
  bmr VARCHAR(6) DEFAULT NULL
);

--@block
Desc registration;

--@block
ALTER TABLE registration MODIFY COLUMN bfp DECIMAL(5,2);

--@block
DROP TABLE registration;

--@block
TRUNCATE TABLE registration;

--@block
ALTER TABLE registration  
MODIFY COLUMN bfp VARCHAR(6),  
MODIFY COLUMN bmr VARCHAR(8);

--@block
SELECT * FROM registration;

--@block
TRUNCATE TABLE registration;

--@block
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL, -- Hashed password
    age TINYINT UNSIGNED NOT NULL,
    weight SMALLINT UNSIGNED NOT NULL,
    height SMALLINT UNSIGNED NOT NULL,
    gender ENUM('m', 'f') NOT NULL,
    bmi FLOAT DEFAULT NULL,
    bmi_category VARCHAR(100) DEFAULT NULL,
    bfp FLOAT(5,2) DEFAULT NULL,
    bmr FLOAT(8.2) DEFAULT NULL,
    breakfast INT DEFAULT 0,
    lunch INT DEFAULT 0,
    dinner INT DEFAULT 0,
    snacks INT DEFAULT 0,
    daily_goal INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--@block
TRUNCATE TABLE users;

--@block
DROP TABLE users;

--@block
SELECT * FROM users;

--@block
desc users;

--@block
INSERT INTO users (id, breakfast, lunch, dinner, snacks) 
VALUES (1, 500, 0, 0, 0) 
ON DUPLICATE KEY UPDATE 
    breakfast = VALUES(breakfast), 
    lunch = VALUES(lunch), 
    dinner = VALUES(dinner), 
    snacks = VALUES(snacks);


--@block
UPDATE users 
SET 
    breakfast = 432, 
    lunch = 546, 
    dinner = 612, 
    snacks = 45 
WHERE id = 1;

--@block
SELECT * FROM users;
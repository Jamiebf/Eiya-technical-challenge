CREATE DATABASE eiya;
USE eiya;
CREATE TABLE cities_cfg(
 id int NOT NULL AUTO_INCREMENT,
 city_a int NOT NULL,
 city_b int NOT NULL,
 city_c int NOT NULL,
 PRIMARY KEY (id)
);

CREATE TABLE cities(
id int NOT NULL AUTO_INCREMENT,
name varchar(50) NOT NULL,
configuration_id int NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (configuration_id) REFERENCES cities_cfg(id) 
);

CREATE TABLE vehicles(
id int NOT NULL AUTO_INCREMENT,
cities_id int NOT NULL,
consume float NOT NULL,
distance int NOT NULL,
consumed float NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (cities_id) REFERENCES cities(id)
);

INSERT INTO cities_cfg (city_a, city_b, city_c) VALUES (0,1,2);
INSERT INTO cities_cfg (city_a, city_b, city_c) VALUES (1,0,4);
INSERT INTO cities_cfg (city_a, city_b, city_c) VALUES (2,4,0);

INSERT INTO cities (name, configuration_id) VALUES ("A",1);
INSERT INTO cities (name, configuration_id) VALUES ("B",2);
INSERT INTO cities (name, configuration_id) VALUES ("C",3);


-- cretae DATABASE hbtn_0d_usa and TABLE cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF OT EXISTS cities (
          id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
          state_id INT NOT NULL,
          FOREIGN KEY(state_id) REFERENCES states(id),
          name VARCHAR(256)
);

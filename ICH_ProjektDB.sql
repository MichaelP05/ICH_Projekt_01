DROP DATABASE dam29_movies_mick;

CREATE DATABASE IF NOT EXISTS dam29_movies_mick;
USE dam29_movies_mick;

DROP TABLE IF EXISTS request_type;
CREATE TABLE IF NOT EXISTS request_type (
		t_id 	INT NOT NULL PRIMARY KEY,
		title 	VARCHAR(30)
);
INSERT INTO request_type (t_id, title) VALUES (1,'By year');
INSERT INTO request_type (t_id, title) VALUES (2,'By genre');
INSERT INTO request_type (t_id, title) VALUES (3,'By year and genre');
INSERT INTO request_type (t_id, title) VALUES (4,'By actor');
INSERT INTO request_type (t_id, title) VALUES (5,'By director');
INSERT INTO request_type (t_id, title) VALUES (6,'By keyword');
INSERT INTO request_type (t_id, title) VALUES (7,'Last month update');
INSERT INTO request_type (t_id, title) VALUES (8,'Popular seeking');
INSERT INTO request_type (t_id, title) VALUES (9,'Popular seeking parameters');

SELECT * FROM request_type;

DROP TABLE IF EXISTS request_journal;
CREATE TABLE IF NOT EXISTS request_journal (
		req_id INT AUTO_INCREMENT 	NOT NULL PRIMARY KEY,
		execute_tmstmp 	DATETIME 	DEFAULT NOW(),
		actor 			VARCHAR(50) DEFAULT NULL,
		director 		VARCHAR(50) DEFAULT NULL,
		genre 			VARCHAR(20) DEFAULT NULL,
		started 		INT DEFAULT NULL,
		keyword 		VARCHAR(25) DEFAULT NULL,
		req_type 		INT
        #, FOREIGN KEY (req_type) REFERENCES request_type(t_id)
);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','',0,'dog',6);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','',0,'cat',6);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','horror',0,'',2);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','comedy',0,'',2);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','drama',0,'',2);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','drama',0,'',2);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','horror',2014,'',3);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','horror',2019,'',3);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','horror',2009,'',3);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','drama',2010,'',3);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','drama',2013,'',3);
INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','comedy',2012,'',3);

# 3 most popular type requests
# ----------------------------
SELECT rt.title, COUNT(rj.req_type)
FROM request_journal AS rj JOIN request_type AS rt ON rt.t_id = rj.req_type
GROUP BY rt.t_id 
ORDER BY rj.req_type DESC
LIMIT 3
;

# 10 most popular sets of requests parameters
# -------------------------------------------
SELECT concat(rt.title,' ', rj.genre,' ', rj.started, ' ', rj.keyword,' ', rj.director,' ', rj.actor) as d, 
	count(*)
FROM request_journal AS rj JOIN request_type AS rt ON rt.t_id = rj.req_type
GROUP BY d 
LIMIT 10
;
# insert into how to :-)
# INSERT INTO request_journal (actor, director, genre, started, keyword, req_type) VALUES ('','','',0,'',1);


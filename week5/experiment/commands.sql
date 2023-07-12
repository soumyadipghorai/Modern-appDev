CREATE TABLE 'article_authors' (
	'article_id' INTEGER, 
	'user_id' INTEGER, 
	PRIMARY KEY('article_id', 'user_id'), 
	FOREIGN KEY('user_id') REFERENCES 'user'('user_id'), 
	FOREIGN KEY('article_id') REFERENCES 'article' ('article_id')
);

CREATE TABLE "article" (
	"article_id"	INTEGER,
	"title"	TEXT,
	"content"	TEXT,
	PRIMARY KEY("article_id" AUTOINCREMENT)
); 

CREATE TABLE "user" (
	"user_id"	INTEGER,
	"user_name"	TEXT UNIQUE,
	"email"	TEXT UNIQUE,
	PRIMARY KEY("user_id" AUTOINCREMENT)
);

SELECT U.user_name AS 'author_username' FROM user AS U, article_authors AS AA 
WHERE AA.article_id = 1 AND AA.user_id = U.user_id
-- author username 
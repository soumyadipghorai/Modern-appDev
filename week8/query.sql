EXPLAIN QUERY PLAN 
SELECT * FROM user 
WHERE user_name = 'ghorai' AND email = 'ghorai@gmail.com';

PRAGMA COMPILE_OPTIONS;

CREATE VIRTUAL TABLE 
    article_search 
USING fts5(title, content, content = article, content_rowid = article_id, tokenize = "porter unicode61");

PRAGMA COMPILE_OPTIONS;

CREATE TRIGGER article_ai AFTER INSERT ON article BEGIN 
    INSERT INTO article_search(rowid, title, content) VALUES (new.article_id, new.title, new.content);
END;

CREATE TRIGGER article_ai AFTER DELETE ON article BEGIN 
    INSERT INTO article_search(article_search, rowid, title, content) 
    VALUES ('delete', old.article_id, old.title, old.content);
END;

CREATE TRIGGER article_ai AFTER UPDATE ON article BEGIN 
    INSERT INTO article_search(article_search, rowid, title, content) 
    VALUES ('delete', old.article_id, old.title, old.content);
    INSERT INTO article_search(rowid, title, content) VALUES (new.article_id, new.title, new.content);
END;

INSERT INTO article_search(article_search) VALUES('rebuild');

SELECT rowid, * FROM article_search WHERE content MATCH 'lorem*';

SELECT * FROM article;
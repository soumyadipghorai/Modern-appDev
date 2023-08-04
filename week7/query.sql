SELECT * FROM table_name WHERE key_col LIKE 'NAME'; 
-- name would be searched in a tree like structure starting with node N then A 
-- sqlalchemy doesn't tell you if a query is poor or not 

-- multicolumn index --> using multiple columns (DOB, NAME, City)

-- friendly 
SELECT * FROM table_name 
WHERE index_part1 = 1 AND index_part2 = 2 AND other_column = 3;
-- indexing based on part1 and 2 

-- index = 1 OR index = 2  
WHERE index = 1 OR A = 10 AND index = 2; 

-- optimized like index part1 = hello 
WHERE index_part1 = 'hello' AND index_part3 = 5;

-- use index on index1 but not on index2 or index3 
WHERE index1 = 1 AND index2 = 2 OR index1 = 3 AND index3 = 3; 

-- unfriendly 
-- index part1 is not used  
WHERE index2 = 1 AND index3 = 2; 

-- index not used in both parts of WHERE
WHERE index = 1 OR A = 10;

-- no index spans all rows 
WHERE index1 = 1 OR index2 = 10;



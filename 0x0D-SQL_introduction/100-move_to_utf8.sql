-- Convert database, table, and column to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET COLLATE utf8mb4_unicode_ci;


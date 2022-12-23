-- Create a new database called 'Exercise14'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
  SELECT name
FROM sys.databases
WHERE name = N'Exercise14'
)
CREATE DATABASE Exercise14
GO

-- Create a new schema called 'exercise14'
IF NOT EXISTS ( SELECT *
FROM sys.schemas
WHERE   name = N'exercise14' )
    EXEC('CREATE SCHEMA [exercise14]');
GO

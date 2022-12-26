-- Create a new database called 'CtCIExercise14'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
  SELECT name
FROM sys.databases
WHERE name = N'CtCIExercise14'
)
CREATE DATABASE CtCIExercise14
GO

-- Create a new schema called 'ctci_exercise14'
IF NOT EXISTS ( SELECT *
FROM sys.schemas
WHERE   name = N'ctci_exercise14' )
    EXEC('CREATE SCHEMA [ctci_exercise14]');
GO

-- Create a new table called 'Apartment' in schema 'ctci_exercise14'
-- Drop the table if it already exists
IF OBJECT_ID('ctci_exercise14.Apartment', 'U') IS NOT NULL
DROP TABLE ctci_exercise14.Apartment
GO
-- Create the table in the specified schema
CREATE TABLE ctci_exercise14.Apartment
(
  AptID INT,
  UnitNumber VARCHAR(100),
  BuildingNumber INT
);
GO

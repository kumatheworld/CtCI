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

-- Create a new table called 'Buildings' in schema 'ctci_exercise14'
-- Drop the table if it already exists
IF OBJECT_ID('ctci_exercise14.Buildings', 'U') IS NOT NULL
DROP TABLE ctci_exercise14.Buildings
GO
-- Create the table in the specified schema
CREATE TABLE ctci_exercise14.Buildings
(
  BuildingID INT,
  ComplexID INT,
  BuildingName VARCHAR(100),
  Address VARCHAR(500)
);
GO

-- Create a new table called 'Requests' in schema 'ctci_exercise14'
-- Drop the table if it already exists
IF OBJECT_ID('ctci_exercise14.Requests', 'U') IS NOT NULL
DROP TABLE ctci_exercise14.Requests
GO
-- Create the table in the specified schema
CREATE TABLE ctci_exercise14.Requests
(
  RequestID INT,
  Status VARCHAR(100),
  AptID INT,
  Description VARCHAR(500)
);
GO

-- Create a new table called 'Complexes' in schema 'ctci_exercise14'
-- Drop the table if it already exists
IF OBJECT_ID('ctci_exercise14.Complexes', 'U') IS NOT NULL
DROP TABLE ctci_exercise14.Complexes
GO
-- Create the table in the specified schema
CREATE TABLE ctci_exercise14.Complexes
(
  ComplexID INT,
  ComplexName VARCHAR(100)
);
GO

-- Create a new table called 'AptTenants' in schema 'ctci_exercise14'
-- Drop the table if it already exists
IF OBJECT_ID('ctci_exercise14.AptTenants', 'U') IS NOT NULL
DROP TABLE ctci_exercise14.AptTenants
GO
-- Create the table in the specified schema
CREATE TABLE ctci_exercise14.AptTenants
(
  TenantID INT,
  AptID INT
);
GO

-- Create a new table called 'Tenants' in schema 'ctci_exercise14'
-- Drop the table if it already exists
IF OBJECT_ID('ctci_exercise14.Tenants', 'U') IS NOT NULL
DROP TABLE ctci_exercise14.Tenants
GO
-- Create the table in the specified schema
CREATE TABLE ctci_exercise14.Tenants
(
  TenantID INT,
  TenantName VARCHAR(100)
);
GO

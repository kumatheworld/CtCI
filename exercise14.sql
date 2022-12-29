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

-- Create a new table called 'Apartments' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('CtCIExercise14.dbo.Apartments', 'U') IS NOT NULL
DROP TABLE CtCIExercise14.dbo.Apartments
GO
-- Create the table in the specified schema
CREATE TABLE CtCIExercise14.dbo.Apartments
(
  AptID INT,
  UnitNumber VARCHAR(100),
  BuildingNumber INT
);
GO

-- Create a new table called 'Buildings' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('CtCIExercise14.dbo.Buildings', 'U') IS NOT NULL
DROP TABLE CtCIExercise14.dbo.Buildings
GO
-- Create the table in the specified schema
CREATE TABLE CtCIExercise14.dbo.Buildings
(
  BuildingID INT,
  ComplexID INT,
  BuildingName VARCHAR(100),
  Address VARCHAR(500)
);
GO

-- Create a new table called 'Requests' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('CtCIExercise14.dbo.Requests', 'U') IS NOT NULL
DROP TABLE CtCIExercise14.dbo.Requests
GO
-- Create the table in the specified schema
CREATE TABLE CtCIExercise14.dbo.Requests
(
  RequestID INT,
  Status VARCHAR(100),
  AptID INT,
  Description VARCHAR(500)
);
GO

-- Create a new table called 'Complexes' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('CtCIExercise14.dbo.Complexes', 'U') IS NOT NULL
DROP TABLE CtCIExercise14.dbo.Complexes
GO
-- Create the table in the specified schema
CREATE TABLE CtCIExercise14.dbo.Complexes
(
  ComplexID INT,
  ComplexName VARCHAR(100)
);
GO

-- Create a new table called 'AptTenants' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('CtCIExercise14.dbo.AptTenants', 'U') IS NOT NULL
DROP TABLE CtCIExercise14.dbo.AptTenants
GO
-- Create the table in the specified schema
CREATE TABLE CtCIExercise14.dbo.AptTenants
(
  TenantID INT,
  AptID INT
);
GO

-- Create a new table called 'Tenants' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('CtCIExercise14.dbo.Tenants', 'U') IS NOT NULL
DROP TABLE CtCIExercise14.dbo.Tenants
GO
-- Create the table in the specified schema
CREATE TABLE CtCIExercise14.dbo.Tenants
(
  TenantID INT,
  TenantName VARCHAR(100)
);
GO

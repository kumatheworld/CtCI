CREATE TABLE apartments (
  AptID INTEGER PRIMARY KEY,
  UnitNumber VARCHAR(10),
  BuildingID INTEGER
);

CREATE TABLE buildings (
  BuildingID INTEGER PRIMARY KEY,
  ComplexID INTEGER,
  BuildingName VARCHAR(100),
  Address VARCHAR(500)
);

CREATE TABLE requests (
  RequestID INTEGER PRIMARY KEY,
  Status VARCHAR(100),
  AptID INTEGER,
  Description VARCHAR(500)
);

CREATE TABLE complexes (
  ComplexID INTEGER PRIMARY KEY,
  ComplexName VARCHAR(100)
);

CREATE TABLE apt_tenants (
  TenantID INTEGER,
  AptID INTEGER,
  PRIMARY KEY (TenantID, AptID)
);

CREATE TABLE tenants (
  TenantID INTEGER PRIMARY KEY,
  TenantName VARCHAR(100)
);

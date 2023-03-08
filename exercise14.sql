CREATE TABLE apartments (
  apt_id INTEGER PRIMARY KEY,
  unit_number VARCHAR(10),
  building_number INTEGER
);

CREATE TABLE buildings (
  building_id INTEGER PRIMARY KEY,
  complex_id INTEGER,
  building_name VARCHAR(100),
  address VARCHAR(500)
);

CREATE TABLE requests (
  request_id INTEGER PRIMARY KEY,
  status VARCHAR(100),
  apt_id INTEGER,
  description VARCHAR(500)
);

CREATE TABLE complexes (
  complex_id INTEGER PRIMARY KEY,
  complex_name VARCHAR(100)
);

CREATE TABLE apt_tenants (
  tenant_id INTEGER,
  apt_id INTEGER,
  PRIMARY KEY (tenant_id, apt_id)
);

CREATE TABLE tenants (
  tenant_id INTEGER PRIMARY KEY,
  tenant_name VARCHAR(100)
);

CREATE TABLE apartments (
  apt_id INTEGER PRIMARY KEY,
  unit_number TEXT,
  building_number INTEGER
);

CREATE TABLE buildings (
  building_id INTEGER PRIMARY KEY,
  complex_id INTEGER,
  building_name TEXT,
  address TEXT
);

CREATE TABLE requests (
  request_id INTEGER PRIMARY KEY,
  status TEXT,
  apt_id INTEGER,
  description TEXT
);

CREATE TABLE complexes (
  complex_id INTEGER PRIMARY KEY,
  complex_name TEXT
);

CREATE TABLE apt_tenants (
  tenant_id INTEGER,
  apt_id INTEGER,
  PRIMARY KEY (tenant_id, apt_id)
);

CREATE TABLE tenants (
  tenant_id INTEGER PRIMARY KEY,
  tenant_name TEXT
);

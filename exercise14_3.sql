DELETE FROM requests
WHERE
  AptID IN (
  SELECT
    AptID
  FROM requests
  JOIN apartments USING (AptID)
  JOIN buildings USING (buildingID)
  where buildingID = 11
);

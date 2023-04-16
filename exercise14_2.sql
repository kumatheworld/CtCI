SELECT
    BuildingId,
    ComplexId,
    BuildingName,
    Address,
    COUNT(RequestID)
FROM buildings
LEFT JOIN apartments USING (BuildingID)
LEFT JOIN requests USING (AptID)
WHERE Status = 'Open'
GROUP BY
	BuildingID;

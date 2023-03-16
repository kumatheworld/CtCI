SELECT
    TenantID,
    TenantName
FROM tenants
JOIN apt_tenants USING (TenantID)
GROUP BY TenantID
HAVING COUNT(TenantID) > 1;

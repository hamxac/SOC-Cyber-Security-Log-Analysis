-- Query 1: Identify the most common attack types targeting the network
SELECT attack_type, COUNT(*) as total_incidents
FROM clean_logs
GROUP BY attack_type
ORDER BY total_incidents DESC;

-- Query 2: Locate the specific Source IPs launching 'High' severity attacks
SELECT source_ip, COUNT(*) as attack_count
FROM clean_logs
WHERE severity_level = 'High'
GROUP BY source_ip
ORDER BY attack_count DESC
LIMIT 10;

-- Query 3: Map the geographic distribution of all network threats
SELECT geo_location, COUNT(*) as total_attacks
FROM clean_logs
GROUP BY geo_location
ORDER BY total_attacks DESC;
-- Just to get a feel for the data 🙂
SELECT * 
FROM traffic
LIMIT 10;

-- The Three functions are identical if there aren't any duplications.
SELECT city, 
    COUNT(*) AS traffic, 
    ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS rowNumber,
    RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk,
    DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS dnsRnk
FROM traffic
GROUP BY city;

-- When there is duplication, the difference is obvious.
SELECT city, DATE(timestamp) AS day, COUNT(*) AS traffic,
    ROW_NUMBER() OVER(PARTITION BY city ORDER BY COUNT(*) DESC) AS rowNumber,
    RANK() OVER(PARTITION BY city ORDER BY COUNT(*) DESC) AS rnk,
    DENSE_RANK() OVER(PARTITION BY city ORDER BY COUNT(*) DESC) AS dnsRnk
FROM traffic
WHERE city = 'AwsomeLand'
GROUP BY city, DATE(timestamp);

-- The top 3 zones per each city with the highest traffic.
WITH trafficByCityAndZone AS (
    SELECT city, zone, COUNT(*) AS traffic, 
        DENSE_RANK() OVER(PARTITION BY city ORDER BY COUNT(*) DESC) AS rnk
    FROM traffic
    GROUP BY city, zone)

SELECT *
FROM trafficByCityAndZone
WHERE rnk <= 3;

-- The top city using each vehicle type.
WITH vehicleTypeByCity AS (
    SELECT city, vehicleType, COUNT(*) AS traffic, 
        RANK() OVER(PARTITION BY vehicleType ORDER BY COUNT(*) DESC) AS rnk
    FROM traffic
    GROUP BY city, vehicleType
)

SELECT vehicleType, city, traffic
FROM vehicleTypeByCity
WHERE rnk = 1;

-- The top 5 days with traffic for each city.
SELECT *
FROM (
    SELECT city, DATE(timestamp) AS day, COUNT(*) AS traffic, DENSE_RANK() OVER(PARTITION BY city ORDER BY COUNT(*) DESC) AS rnk
    FROM traffic
    GROUP BY city, DATE(timestamp)
)
WHERE rnk <= 5;
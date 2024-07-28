-- https://leetcode.com/problems/rising-temperature/
-- select day = some_day + 1 and day has to have higher temp

SELECT w1.id
FROM Weather AS w1
WHERE EXISTS
    (SELECT 1
     FROM Weather AS w2
     WHERE w1.temperature > w2.temperature
       AND w1.recordDate = w2.recordDate + 1 );

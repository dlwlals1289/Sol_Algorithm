SELECT
    CASE 
        WHEN SUM(s.CATEGORY = 'Front End') > 0 
         AND SUM(s.NAME = 'Python') > 0 THEN 'A'
        WHEN SUM(s.NAME = 'C#') > 0 THEN 'B'
        WHEN SUM(s.CATEGORY = 'Front End') > 0 THEN 'C'
        ELSE NULL
    END AS GRADE,
    d.ID,
    d.EMAIL
FROM DEVELOPERS d
JOIN SKILLCODES s 
  ON d.SKILL_CODE & s.CODE > 0
GROUP BY d.ID, d.EMAIL
HAVING GRADE IS NOT NULL
ORDER BY GRADE, d.ID;
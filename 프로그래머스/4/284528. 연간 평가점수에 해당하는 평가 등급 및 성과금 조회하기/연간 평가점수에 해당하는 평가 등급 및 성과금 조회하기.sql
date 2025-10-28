SELECT
    e.EMP_NO,
    e.EMP_NAME,
    sub.GRADE,
    e.SAL * (sub.RATIO / 100) AS BONUS
FROM (
    SELECT 
        EMP_NO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 20
            WHEN AVG(SCORE) >= 90 THEN 15
            WHEN AVG(SCORE) >= 80 THEN 10
            ELSE 0
        END AS RATIO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO    
) sub
JOIN HR_EMPLOYEES AS e ON sub.EMP_NO = e.EMP_NO
ORDER BY e.EMP_NO;
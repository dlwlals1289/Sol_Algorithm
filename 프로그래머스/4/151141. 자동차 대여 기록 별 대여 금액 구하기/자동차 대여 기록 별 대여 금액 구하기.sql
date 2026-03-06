SELECT
    a.HISTORY_ID,
    CASE
        WHEN 7 <= DATEDIFF(a.END_DATE, a.START_DATE) + 1 AND DATEDIFF(a.END_DATE, a.START_DATE) + 1 < 30 
            THEN ROUND(b.DAILY_FEE * (DATEDIFF(a.END_DATE, a.START_DATE) + 1) * (100 - (
                SELECT 
                    DISCOUNT_RATE
                FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '7일 이상'
            )) / 100)
        WHEN 30 <= DATEDIFF(a.END_DATE, a.START_DATE) + 1 AND DATEDIFF(a.END_DATE, a.START_DATE) + 1 < 90 
            THEN ROUND(b.DAILY_FEE * (DATEDIFF(a.END_DATE, a.START_DATE) + 1) * (100 - (
                SELECT 
                    DISCOUNT_RATE
                FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '30일 이상'
            )) / 100)
        WHEN 90 <= DATEDIFF(a.END_DATE, a.START_DATE) + 1 
            THEN ROUND(b.DAILY_FEE * (DATEDIFF(a.END_DATE, a.START_DATE) + 1) * (100 - (
                SELECT 
                    DISCOUNT_RATE
                FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '90일 이상'
            )) / 100)
        ELSE b.DAILY_FEE * (DATEDIFF(a.END_DATE, a.START_DATE) + 1)
    END AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS a
JOIN CAR_RENTAL_COMPANY_CAR AS b 
    ON a.CAR_ID = b.CAR_ID AND b.CAR_TYPE = '트럭'
ORDER BY FEE DESC, a.HISTORY_ID DESC;

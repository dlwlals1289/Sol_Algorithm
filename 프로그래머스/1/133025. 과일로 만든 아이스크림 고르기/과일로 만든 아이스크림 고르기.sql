-- 코드를 입력하세요
SELECT f.FLAVOR
FROM FIRST_HALF f
WHERE f.TOTAL_ORDER > 3000 AND 
    f.FLAVOR IN (SELECT i.FLAVOR
FROM ICECREAM_INFO i
WHERE i.INGREDIENT_TYPE = 'fruit_based');
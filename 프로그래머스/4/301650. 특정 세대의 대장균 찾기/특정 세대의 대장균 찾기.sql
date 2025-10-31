WITH RECURSIVE gen AS (
  SELECT id, parent_id, 1 AS generation
  FROM ECOLI_DATA
  WHERE parent_id IS NULL
  UNION ALL
  SELECT e.id, e.parent_id, g.generation + 1
  FROM ECOLI_DATA e
  JOIN gen g ON e.parent_id = g.id
)
SELECT
    g.id AS ID
FROM gen g
WHERE g.generation = 3
ORDER BY g.id;

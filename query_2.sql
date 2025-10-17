SELECT s.name AS student, sub.name AS subject, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE sub.name = 'Math'
GROUP BY s.id, sub.name
ORDER BY avg_grade DESC
LIMIT 1;

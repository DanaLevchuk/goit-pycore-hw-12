SELECT t.name AS teacher, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN subjects sub ON sub.id = g.subject_id
JOIN teachers t ON t.id = sub.teacher_id
WHERE t.name = 'Mr. Smith'
GROUP BY t.name;

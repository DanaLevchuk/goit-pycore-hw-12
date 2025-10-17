SELECT s.name AS student, sub.name AS subject
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE s.name = 'Anna Ivanova'
GROUP BY s.name, sub.name;

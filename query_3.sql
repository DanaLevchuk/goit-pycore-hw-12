SELECT gr.name AS group_name, sub.name AS subject, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN groups gr ON gr.id = s.group_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE sub.name = 'Math'
GROUP BY gr.name, sub.name;

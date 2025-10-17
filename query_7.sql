SELECT s.name AS student, gr.name AS group_name, sub.name AS subject, g.grade, g.date_received
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN groups gr ON gr.id = s.group_id
JOIN subjects sub ON sub.id = g.subject_id
WHERE gr.name = 'Group A' AND sub.name = 'Math';

SELECT s.name AS student, t.name AS teacher, sub.name AS subject
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects sub ON sub.id = g.subject_id
JOIN teachers t ON t.id = sub.teacher_id
WHERE s.name = 'Anna Ivanova' AND t.name = 'Mr. Smith';

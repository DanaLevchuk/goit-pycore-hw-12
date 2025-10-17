SELECT t.name AS teacher, sub.name AS subject
FROM subjects sub
JOIN teachers t ON t.id = sub.teacher_id
WHERE t.name = 'Mr. Smith';

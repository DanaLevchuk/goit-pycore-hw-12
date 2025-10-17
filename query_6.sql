SELECT s.name AS student, g.name AS group_name
FROM students s
JOIN groups g ON g.id = s.group_id
WHERE g.name = 'Group A';

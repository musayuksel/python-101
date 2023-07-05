-- Mock questions
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 1+1?','Math','Easy');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 2+2?','Math','Easy');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 3+3?','Math','Easy');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 4+4?','Math','Easy');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 5+5?','Math','Medium');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 6+6?','Math','Medium');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 7+7?','Math','Medium');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 8+8?','Math','Medium');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 9+9?','Math','Hard');
INSERT INTO questions (quiz_id,question_text,category,difficulty) VALUES (1,'What is 10+10?','Math','Hard');

-- Mock answers
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (1,'1',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (1,'2',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (1,'3',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (1,'4',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (2,'2',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (2,'3',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (2,'4',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (2,'5',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (3,'5',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (3,'6',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (3,'7',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (3,'8',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (4,'7',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (4,'8',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (4,'9',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (4,'10',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (5,'10',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (5,'11',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (5,'12',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (5,'13',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (6,'12',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (6,'13',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (6,'14',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (6,'15',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (7,'14',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (7,'15',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (7,'16',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (7,'17',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (8,'8',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (8,'16',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (8,'24',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (8,'32',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (9,'18',true);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (9,'19',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (9,'20',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (9,'21',false);

INSERT INTO answers (question_id,answer_text,is_correct) VALUES (10,'10',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (10,'11',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (10,'12',false);
INSERT INTO answers (question_id,answer_text,is_correct) VALUES (10,'20',true);
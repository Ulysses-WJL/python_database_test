USE books;

ALTER TABLE emp5 ADD PRIMARY KEY(employee_id);

ALTER TABLE dept2 ADD PRIMARY KEY(department_id);

ALTER TABLE book ADD COLUMN dept_id INT;

ALTER TABLE book ADD CONSTRAINT fk_book_emp FOREIGN KEY(dept_id) REFERENCES dept2(department_id);


DESC book;

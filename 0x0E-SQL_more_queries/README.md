# 0x0E-SQL_more_queries.
<img width="100%" height = "350px" src="https://tecnologiaenvivo.com/wp-content/uploads/2016/03/mysql-logo900.jpg" />

## Resources
### Read or watch:
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL constraints](https://zetcode.com/mysql/constraints/)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
- [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
- [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
- [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

Extra resources around relational database model design:
- [Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.guru99.com/database-normalization.html)
- [ER Modeling](https://www.guru99.com/er-modeling.html)

## Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Install MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
### Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
# SQL JOINS
<img width="70%" height = "350px" src="http://1.bp.blogspot.com/-SXvf5dWHKKw/Vq0B98oVepI/AAAAAAAA6OU/4wyG1NuJehQ/s1600/450_1000%2B%25281%2529.jpg" />

# Tasks.

### 0. My privileges!
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

---
### 1. Root user.
Write a script that creates the MySQL server user `user_0d_1`.
  - `user_0d_1` should have all privileges on your MySQL server
  - The `user_0d_1` password should be set to `user_0d_1_pwd`
  - If the user `user_0d_1` already exists, your script should not fail
---

### 2. Read user.
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
  - `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
  - The `user_0d_2` password should be set to `user_0d_2_pwd`
  - If the database `hbtn_0d_2` already exists, your script should not fail
  - If the user `user_0d_2` already exists, your script should not fail
---

### 3. Always a name.
Write a script that creates the table `force_name` on your MySQL server.
  - `force_name` description:
    - `id` INT
    - `name` VARCHAR(256) can’t be null
  - The database name will be passed as an argument of the `mysql` command
  - If the table `force_name` already exists, your script should not fail
---

### 4. ID can't be null.
Write a script that creates the table `id_not_null` on your MySQL server.
  - `id_not_null` description:
    - `id` INT with the default value 1
    - `name` VARCHAR(256)
  - The database name will be passed as an argument of the `mysql` command
  - If the table `id_not_null` already exists, your script should not fail
---

### 5. Unique ID.
Write a script that creates the table `unique_id` on your MySQL server.
  - `unique_id` description:
    - `id` INT with the default value 1 and must be unique
    - `name` VARCHAR(256)
  - The database name will be passed as an argument of the `mysql` command
  - If the table `unique_id` already exists, your script should not fail
---


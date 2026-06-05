# 创建表 

create table student(
	stuid int,
	stuname varchar(20),
	score double,
	birdate datetime
);


CREATE TABLE `student` (
  `stuid` int DEFAULT NULL,
  `stuname` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `score` double DEFAULT NULL,
  `birdate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
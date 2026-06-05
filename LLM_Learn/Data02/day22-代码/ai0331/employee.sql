/*
 Navicat Premium Data Transfer

 Source Server         : java1012
 Source Server Type    : MySQL
 Source Server Version : 80026 (8.0.26)
 Source Host           : localhost:3306
 Source Schema         : java1012

 Target Server Type    : MySQL
 Target Server Version : 80026 (8.0.26)
 File Encoding         : 65001

 Date: 09/01/2025 19:04:17
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee`  (
  `empid` int NOT NULL AUTO_INCREMENT COMMENT '员工编号',
  `empname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '员工名称',
  `empage` int NULL DEFAULT NULL COMMENT '员工年龄',
  `empaddress` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '员工地址',
  `empsex` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '员工性别',
  `empbirthday` date NULL DEFAULT NULL COMMENT '员工生日',
  `empsalary` double NULL DEFAULT NULL COMMENT '员工绩效',
  `depid` int NULL DEFAULT NULL COMMENT '部门编号',
  `empemail` varchar(50) NOT NULL COMMENT '员工邮箱',
  `empinfo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '员工备注',
  PRIMARY KEY (`empid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES (1, '小宝', 15, '东莞', '男', '1993-01-01', 6500, 6,'xb888@atguigu.com','力气大');
INSERT INTO `employee` VALUES (2, '赵四', 35, '深圳', '男', '1994-02-01', 7500, 3, 'zs666@atguigu.com','活好');
INSERT INTO `employee` VALUES (3, '云姨', 45, '深圳', '女', '1996-03-01', 8500, 1,'yy666@atguigu.com', NULL);
INSERT INTO `employee` VALUES (4, '赵小四', 25, '深圳', '男', '1995-04-01', 9500, 5,'zxs888@atguigu.com', NULL);
INSERT INTO `employee` VALUES (5, '赵大四', 35, '广州', '男', '1991-05-01', 9600, 2,'12345678@qq.com', NULL);
INSERT INTO `employee` VALUES (6, '四小赵', 28, '佛山', '男', '1992-06-01', 7550, 3, 'sxz888@atguigu.com',NULL);
INSERT INTO `employee` VALUES (7, '赵四思', 15, '东莞', '男', '1993-07-01', 6500, 4, 'zss888@atguigu.com','尬舞天王');
INSERT INTO `employee` VALUES (8, '赵四五', 35, '深圳', '男', '1994-08-01', 8500, 6,'zsw996@atguigu.com', NULL);
INSERT INTO `employee` VALUES (9, '赵五六', 55, '深圳', '女', '1996-09-01', 8500, 3, 'zwl789@atguigu.com',NULL);
INSERT INTO `employee` VALUES (10, '赵云', 23, '深圳', '男', '1984-03-07', 15000, 2, 'zy789@atguigu.com','七进七出');
INSERT INTO `employee` VALUES (11, '刘德华', 24, '广州', '男', '2005-04-09', 25000, 3,'ldh789@163.com', NULL);
INSERT INTO `employee` VALUES (12, '郭德纲', 52, '北京', '男', '1990-03-07', 50000, 4,'gdg123@atguigu.com', NULL);
INSERT INTO `employee` VALUES (16, '郭麒麟', 40, '北京', '男', '1990-02-07', 34000, 2,'gql888@atguigu.com', NULL);
INSERT INTO `employee` VALUES (17, '于谦', 53, '北京', '男', '1898-12-09', 88888, 3, 'yq789@163.com','抽烟喝酒烫头');

SET FOREIGN_KEY_CHECKS = 1;

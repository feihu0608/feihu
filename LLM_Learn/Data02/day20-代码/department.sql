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

 Date: 09/01/2025 19:04:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `depid` int NOT NULL AUTO_INCREMENT COMMENT '部门编号',
  `depname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '部门名称',
  PRIMARY KEY (`depid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES (1, '技术部');
INSERT INTO `department` VALUES (2, '人社部');
INSERT INTO `department` VALUES (3, '后勤部');
INSERT INTO `department` VALUES (4, '安保部');
INSERT INTO `department` VALUES (5, '公关部');
INSERT INTO `department` VALUES (6, '销售部');
INSERT INTO `department` VALUES (7, '业务部');

SET FOREIGN_KEY_CHECKS = 1;

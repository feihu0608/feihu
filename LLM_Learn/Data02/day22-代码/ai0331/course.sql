/*
 Navicat Premium Data Transfer

 Source Server         : 0724conn
 Source Server Type    : MySQL
 Source Server Version : 80026 (8.0.26)
 Source Host           : localhost:3306
 Source Schema         : db0724

 Target Server Type    : MySQL
 Target Server Version : 80026 (8.0.26)
 File Encoding         : 65001

 Date: 28/08/2023 11:41:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `cid` int NULL DEFAULT NULL COMMENT '课程编号',
  `profession` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '专业名称',
  `cname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '课程名称'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1, 'Java', NULL);
INSERT INTO `course` VALUES (2, '1', 'JavaSE');
INSERT INTO `course` VALUES (3, '1', 'Spring');
INSERT INTO `course` VALUES (4, '1', 'MyBatis');
INSERT INTO `course` VALUES (5, '1', 'Hibernate');
INSERT INTO `course` VALUES (6, 'H5', NULL);
INSERT INTO `course` VALUES (7, '6', 'html');
INSERT INTO `course` VALUES (8, '6', 'css');
INSERT INTO `course` VALUES (9, '6', 'js');
INSERT INTO `course` VALUES (10, '6', 'vue');
INSERT INTO `course` VALUES (11, '6', 'bootstrap');

SET FOREIGN_KEY_CHECKS = 1;

-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: 3ddatabase
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `first_comment`
--

DROP TABLE IF EXISTS `first_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `first_comment` (
  `commentId` int NOT NULL,
  `content` varchar(45) NOT NULL,
  `fromUid` varchar(8) NOT NULL,
  `dateTime` date DEFAULT NULL,
  `type` int NOT NULL DEFAULT '0',
  `lastTime` date DEFAULT NULL,
  `replyNum` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`commentId`),
  KEY `fronUid_idx` (`fromUid`),
  CONSTRAINT `fronUid` FOREIGN KEY (`fromUid`) REFERENCES `user` (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `first_comment`
--

LOCK TABLES `first_comment` WRITE;
/*!40000 ALTER TABLE `first_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `first_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_basic`
--

DROP TABLE IF EXISTS `forum_basic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forum_basic` (
  `themeName` int NOT NULL,
  `postNum` int NOT NULL DEFAULT '0',
  `themeType` int NOT NULL DEFAULT '0',
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`themeName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_basic`
--

LOCK TABLES `forum_basic` WRITE;
/*!40000 ALTER TABLE `forum_basic` DISABLE KEYS */;
/*!40000 ALTER TABLE `forum_basic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `projectId` varchar(8) NOT NULL,
  `projectName` varchar(45) NOT NULL,
  `userId` varchar(8) NOT NULL,
  `ply` varchar(45) DEFAULT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `imgdir` varchar(45) DEFAULT NULL,
  `share` tinyint NOT NULL DEFAULT '0',
  `describtion` varchar(45) DEFAULT NULL,
  `createTime` date DEFAULT NULL,
  PRIMARY KEY (`projectId`),
  UNIQUE KEY `projectName_UNIQUE` (`projectName`),
  KEY `userId_idx` (`userId`),
  CONSTRAINT `userId` FOREIGN KEY (`userId`) REFERENCES `user` (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES ('63101d0d','scan1','zk','','','0',NULL,1,'古建筑',NULL),('63101d12','scan2','zk','','',NULL,NULL,0,NULL,NULL),('63101d28','scan3','zss','','','0',NULL,1,'古建筑',NULL),('631c017a','scan7','zk','','','文物','./results/zk_scan7',0,'巴拉巴拉','2022-09-10'),('631d42c8','手残1','zk','','','000','./results/zk_手残1',0,'123','2022-09-11');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `second_comment`
--

DROP TABLE IF EXISTS `second_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `second_comment` (
  `sCommentId` int NOT NULL,
  `fCommentId` int NOT NULL,
  `content` varchar(45) NOT NULL,
  `fromUid2` varchar(8) NOT NULL,
  `dataTime` date DEFAULT NULL,
  PRIMARY KEY (`sCommentId`),
  KEY `fCommentId_idx` (`fCommentId`),
  KEY `fromUid2_idx` (`fromUid2`),
  CONSTRAINT `fCommentId` FOREIGN KEY (`fCommentId`) REFERENCES `first_comment` (`commentId`),
  CONSTRAINT `fromUid2` FOREIGN KEY (`fromUid2`) REFERENCES `user` (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `second_comment`
--

LOCK TABLES `second_comment` WRITE;
/*!40000 ALTER TABLE `second_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `second_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `userId` varchar(8) NOT NULL,
  `userName` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `wxId` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('94c75b93','wy','123123','','','',''),('00000002','zk','123456',NULL,NULL,NULL,NULL),('00000001','zss','zss75510101',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user2`
--

DROP TABLE IF EXISTS `user2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user2` (
  `userId` varchar(8) NOT NULL,
  `userName` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `remarks` varchar(45) DEFAULT NULL,
  `phone` varchar(45) NOT NULL,
  `wxId` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user2`
--

LOCK TABLES `user2` WRITE;
/*!40000 ALTER TABLE `user2` DISABLE KEYS */;
INSERT INTO `user2` VALUES ('0001','G4SS','zss75510101',NULL,'18811710955',NULL,NULL),('0002','zk','123456','','18811710955',NULL,NULL);
/*!40000 ALTER TABLE `user2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database '3ddatabase'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-11 10:14:27

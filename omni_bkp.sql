-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: omni
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_inv`
--

DROP TABLE IF EXISTS `tbl_inv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_inv` (
  `prod_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `prod_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `store_count` bigint(20) NOT NULL DEFAULT '0',
  `price` bigint(20) NOT NULL DEFAULT '0',
  `create_time` date DEFAULT NULL,
  `last_order` bigint(20) DEFAULT '0',
  `last_topup` bigint(20) DEFAULT '0',
  PRIMARY KEY (`prod_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_inv`
--

LOCK TABLES `tbl_inv` WRITE;
/*!40000 ALTER TABLE `tbl_inv` DISABLE KEYS */;
INSERT INTO `tbl_inv` VALUES (1,'chocolate',332,2,'2018-12-20',11,0),(2,'biscuit',45,2,'2018-12-20',0,2),(3,'alphenlibe',4578,2,'2018-12-20',0,0),(4,'fivestar',80,5,'2018-12-23',13,0);
/*!40000 ALTER TABLE `tbl_inv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_ord_details`
--

DROP TABLE IF EXISTS `tbl_ord_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_ord_details` (
  `order_id` bigint(20) NOT NULL,
  `prod_id` bigint(20) NOT NULL,
  `quant` bigint(20) DEFAULT NULL,
  `sold_price` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`order_id`,`prod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_ord_details`
--

LOCK TABLES `tbl_ord_details` WRITE;
/*!40000 ALTER TABLE `tbl_ord_details` DISABLE KEYS */;
INSERT INTO `tbl_ord_details` VALUES (1,1,5,2),(1,2,5,2),(2,1,5,2),(2,2,5,2),(3,1,5,2),(3,2,5,2),(4,1,5,2),(4,2,5,2),(7,1,9,2),(8,1,9,2),(10,1,9,2),(11,1,5,2),(12,4,5,5),(13,4,5,5);
/*!40000 ALTER TABLE `tbl_ord_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_orders`
--

DROP TABLE IF EXISTS `tbl_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_orders` (
  `order_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `order_date` date DEFAULT NULL,
  `total_count` bigint(20) DEFAULT '0',
  `order_value` bigint(20) DEFAULT '0',
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_orders`
--

LOCK TABLES `tbl_orders` WRITE;
/*!40000 ALTER TABLE `tbl_orders` DISABLE KEYS */;
INSERT INTO `tbl_orders` VALUES (1,2,'2018-12-20',10,20),(2,2,'2018-12-20',10,20),(3,3,'2018-12-20',10,20),(4,2,'2018-12-20',10,20),(7,1,'2018-12-23',9,18),(8,1,'2018-12-23',9,18),(10,1,'2018-12-23',9,18),(11,1,'2018-12-23',5,10),(12,1,'2018-12-23',5,25),(13,1,'2018-12-23',5,25);
/*!40000 ALTER TABLE `tbl_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_topups`
--

DROP TABLE IF EXISTS `tbl_topups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_topups` (
  `topup_id` bigint(20) NOT NULL,
  `prod_id` bigint(20) NOT NULL,
  `topup_date` date DEFAULT NULL,
  `count` bigint(20) DEFAULT '0',
  PRIMARY KEY (`topup_id`,`prod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_topups`
--

LOCK TABLES `tbl_topups` WRITE;
/*!40000 ALTER TABLE `tbl_topups` DISABLE KEYS */;
INSERT INTO `tbl_topups` VALUES (1,2,'2018-12-20',5),(2,2,'2018-12-23',45);
/*!40000 ALTER TABLE `tbl_topups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_users`
--

DROP TABLE IF EXISTS `tbl_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_users` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_users`
--

LOCK TABLES `tbl_users` WRITE;
/*!40000 ALTER TABLE `tbl_users` DISABLE KEYS */;
INSERT INTO `tbl_users` VALUES (1,'user 1oo','user1@la.al','1usr'),(2,'user oo','user2@la.al','us2r'),(3,'u3er oo','user3@la.al','us2r33');
/*!40000 ALTER TABLE `tbl_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-23  4:49:22

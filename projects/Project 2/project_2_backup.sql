-- MySQL dump 10.13  Distrib 8.4.5, for Win64 (x86_64)
--
-- Host: localhost    Database: project_2
-- ------------------------------------------------------
-- Server version	8.4.5

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `sr_num` int NOT NULL,
  `city_name` varchar(20) DEFAULT NULL,
  `x_coordinate` int DEFAULT NULL,
  `y_coordinate` int DEFAULT NULL,
  PRIMARY KEY (`sr_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (1,'Srinagar',153,80),(2,'Jammu',154,111),(3,'Shimla',196,151),(4,'Chandigarh',189,160),(5,'Dehradun',211,170),(6,'New Delhi',199,206),(7,'Gangtok',425,233),(8,'Itanagar',531,229),(9,'Jaipur',167,246),(10,'Lucknow',271,251),(11,'Dispur',497,253),(12,'Kohima',544,261),(13,'Shillong',499,265),(14,'Patna',359,277),(15,'Manipur',542,280),(16,'Agartala',491,309),(17,'Aizawl',521,309),(18,'Gandhinagar',96,327),(19,'Bhopal',198,329),(20,'Ranchi',365,327),(21,'Kolkata',428,342),(22,'Chhattisgarh',287,379),(23,'Bhubaseswar',381,396),(24,'Mumbai',98,428),(25,'Hyderabad',220,466),(26,'Panaji',117,510),(27,'Begaluru',198,568),(28,'Amaravati',256,489),(29,'Chennai',259,567),(30,'Puducherry',247,593),(31,'Thiruvananthapuram',180,673),(32,'Dadra & Nagar Haveli',96,394);
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coach_types`
--

DROP TABLE IF EXISTS `coach_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coach_types` (
  `sr_no` int NOT NULL,
  `coach_type` varchar(20) DEFAULT NULL,
  `coach_fee` smallint DEFAULT NULL,
  PRIMARY KEY (`sr_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coach_types`
--

LOCK TABLES `coach_types` WRITE;
/*!40000 ALTER TABLE `coach_types` DISABLE KEYS */;
INSERT INTO `coach_types` VALUES (1,'BOX CAR',10000),(2,'FLAT CAR',8000),(3,'GONDOLA',13000),(4,'REFRIGERATED BOX CAR',20000),(5,'TANK CAR',20000);
/*!40000 ALTER TABLE `coach_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `false_business_booking_sheet`
--

DROP TABLE IF EXISTS `false_business_booking_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `false_business_booking_sheet` (
  `train_number` smallint DEFAULT NULL,
  `number_of_coaches` int DEFAULT NULL,
  `type_of_coaches` varchar(25) DEFAULT NULL,
  `journey_status` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `false_business_booking_sheet`
--

LOCK TABLES `false_business_booking_sheet` WRITE;
/*!40000 ALTER TABLE `false_business_booking_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `false_business_booking_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `false_freight_coach_sheet`
--

DROP TABLE IF EXISTS `false_freight_coach_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `false_freight_coach_sheet` (
  `coach_num` varchar(2) NOT NULL,
  `coach_type` varchar(20) DEFAULT NULL,
  `status` varchar(6) DEFAULT NULL,
  `booked_for` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`coach_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `false_freight_coach_sheet`
--

LOCK TABLES `false_freight_coach_sheet` WRITE;
/*!40000 ALTER TABLE `false_freight_coach_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `false_freight_coach_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `false_passenger_coach_sheet`
--

DROP TABLE IF EXISTS `false_passenger_coach_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `false_passenger_coach_sheet` (
  `coach_num` varchar(2) NOT NULL,
  `coach_type` varchar(7) DEFAULT NULL,
  `coach_fee` smallint DEFAULT NULL,
  `seats_available` int DEFAULT NULL,
  `total_seats` int DEFAULT NULL,
  PRIMARY KEY (`coach_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `false_passenger_coach_sheet`
--

LOCK TABLES `false_passenger_coach_sheet` WRITE;
/*!40000 ALTER TABLE `false_passenger_coach_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `false_passenger_coach_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `train_sheet`
--

DROP TABLE IF EXISTS `train_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train_sheet` (
  `train_num` smallint DEFAULT NULL,
  `start_point` varchar(20) DEFAULT NULL,
  `destination` varchar(20) DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  `departure_time` time DEFAULT NULL,
  `arrival_date` date DEFAULT NULL,
  `coach_sheet` varchar(30) DEFAULT NULL,
  `status` varchar(8) DEFAULT NULL,
  `train_type` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train_sheet`
--

LOCK TABLES `train_sheet` WRITE;
/*!40000 ALTER TABLE `train_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `train_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_list`
--

DROP TABLE IF EXISTS `user_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_list` (
  `user_id` int NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `aadhar_num` varchar(12) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `user_booking` varchar(31) DEFAULT NULL,
  `sus_val` tinyint DEFAULT NULL,
  `account` varchar(8) DEFAULT NULL,
  `company_name` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_list`
--

LOCK TABLES `user_list` WRITE;
/*!40000 ALTER TABLE `user_list` DISABLE KEYS */;
INSERT INTO `user_list` VALUES (1000000001,'kapil','123','123456789012','2006-09-15',NULL,0,'Personal',NULL);
/*!40000 ALTER TABLE `user_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-11 19:23:14

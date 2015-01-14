-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 19, 2014 at 04:05 PM
-- Server version: 5.5.40-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `intertug`
--

-- --------------------------------------------------------

--
-- Table structure for table `datos`
--

CREATE TABLE IF NOT EXISTS `datos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rm` varchar(15) DEFAULT NULL,
  `fechahora` datetime DEFAULT NULL,
  `codvariable` varchar(10) DEFAULT NULL,
  `valor` float DEFAULT NULL,
  `respuesta` tinyint(1) NOT NULL DEFAULT '0',
  `enviado` datetime DEFAULT NULL,
  `recibido` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `gps`
--

CREATE TABLE IF NOT EXISTS `gps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rm` varchar(15) DEFAULT NULL,
  `fechahora` datetime DEFAULT NULL,
  `latitud` float(10,5) DEFAULT NULL,
  `latitudNS` varchar(1) DEFAULT NULL,
  `longitud` float(10,5) DEFAULT NULL,
  `longitudEW` varchar(1) DEFAULT NULL,
  `velocidad` float DEFAULT NULL,
  `direccion` float DEFAULT NULL,
  `pdop` float DEFAULT NULL,
  `hdop` float DEFAULT NULL,
  `respuesta` tinyint(1) NOT NULL DEFAULT '0',
  `enviado` datetime DEFAULT NULL,
  `recibido` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `parametros`
--

CREATE TABLE IF NOT EXISTS `parametros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) NOT NULL,
  `valor` varchar(200) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=28 ;

--
-- Dumping data for table `parametros`
--

INSERT INTO `parametros` (`id`, `titulo`, `valor`, `nombre`, `estado`) VALUES
(1, 'ping', 'http://190.242.119.122:82/SioServices/SioGeneralService.asmx?WSDL', 'PARAM_WEB_SERVICES', 1),
(2, 'periocidad', '1', 'CONFIG_SYSTEM', 1),
(3, 'username', '', 'PARAM_SESSION', 1),
(4, 'password', '', 'PARAM_SESSION', 1),
(5, 'ApplicationId', 'A252662D-7EA6-46C5-8BD6-1E014DAD1F06', 'PARAM_SESSION', 1),
(6, 'DeviceId', '57aedf29-92e1-48c2-8adb-07597d8d42ce', 'PARAM_SESSION', 1),
(7, 'createSession', 'http://190.242.119.122:82/SioServices/SioGeneralService.asmx?WSDL', 'PARAM_WEB_SERVICES', 1),
(8, 'log', 'a', 'CONFIG_SYSTEM', 1),
(9, 'cantidad_gps', '50', 'CONFIG_SYSTEM', 1),
(10, 'cantidad_datos', '2', 'CONFIG_SYSTEM', 1),
(12, 'fechahora', 'D', 'XML_STRUCTURE_DATOS', 1),
(13, 'codvariable', 'C', 'XML_STRUCTURE_DATOS', 1),
(14, 'valor', 'V', 'XML_STRUCTURE_DATOS', 1),
(16, 'fechahora', 'D', 'XML_STRUCTURE_GPS', 1),
(17, 'latitud', 'LA', 'XML_STRUCTURE_GPS', 1),
(18, 'latitudNS', 'NS', 'XML_STRUCTURE_GPS', 1),
(19, 'longitud', 'LO', 'XML_STRUCTURE_GPS', 1),
(20, 'longitudEW', 'EW', 'XML_STRUCTURE_GPS', 1),
(21, 'velocidad', 'S', 'XML_STRUCTURE_GPS', 1),
(22, 'direccion', 'B', 'XML_STRUCTURE_GPS', 1),
(23, 'pdop', 'P', 'XML_STRUCTURE_GPS', 1),
(24, 'hdop', 'H', 'XML_STRUCTURE_GPS', 1),
(25, 'datos', 'D', 'ENTITY_NAME', 1),
(26, 'gps', 'G', 'ENTITY_NAME', 1),
(27, 'sending_data', 'http://190.242.119.122:82/SioServices/DaqOnBoardService.asmx?WSDL', 'PARAM_WEB_SERVICES', 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

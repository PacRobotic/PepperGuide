-- phpMyAdmin SQL Dump
-- version 3.3.5
-- http://www.phpmyadmin.net
--
-- Serveur: localhost:3308
-- Généré le : Jeu 25 Avril 2019 à 17:59
-- Version du serveur: 5.1.47
-- Version de PHP: 5.2.11

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `picardap`
--

-- --------------------------------------------------------

--
-- Structure de la table `Salles`
--

CREATE TABLE IF NOT EXISTS `Salles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `localisation` varchar(5) DEFAULT NULL,
  `type` varchar(20) NOT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=101;

--
-- Contenu de la table `Salles`
--

INSERT INTO `Salles` (`id`, `localisation`, `type`, `description`) VALUES
(1, 'A201', 'Autre', 'Couloir'),
(2, 'A202', 'Projet', 'decription'),
(3, 'A203', 'Projet', 'decription'),
(4, 'A204', 'Projet', 'decription'),
(5, 'A205', 'Projet', 'decription'),
(6, 'A206', 'Bureau', 'decription'),
(7, 'A207', 'Bureau', 'decription'),
(8, 'A208', 'Bureau', 'decription'),
(9, 'A209', 'Bureau', 'decription'),
(10, 'A210', 'Bureau', 'decription'),
(11, 'A211', 'Bureau', 'decription'),
(12, 'A212', 'Bureau', 'decription'),
(13, 'A213', 'Bureau', 'decription'),
(14, 'A214', 'Bureau', 'decription'),
(15, 'A215', 'Bureau', 'decription'),
(16, 'A216', 'Bureau', 'decription'),
(17, 'A217', 'Projet', 'decription'),
(18, 'A218', 'Projet', 'decription'),
(19, 'A219', 'Autre', 'decription'),
(20, 'A220', 'Autre', 'decription'),
(21, 'A221', 'Bureau', 'decription'),
(22, 'A222', 'Bureau', 'decription'),
(23, 'A223', 'Bureau', 'decription'),
(24, 'A224', 'Bureau', 'decription'),
(25, 'A225', 'Bureau', 'decription'),
(26, 'A226', 'Bureau', 'decription'),
(27, 'A227', 'Bureau', 'decription'),
(28, 'A228', 'Bureau', 'decription'),
(29, 'A229', 'Bureau', 'decription'),
(30, 'A230', 'Autre', 'decription'),
(31, 'A231', 'Autre', 'decription'),
(32, 'B201', 'Autre', 'Couloir'),
(33, 'B202', 'Autre', 'decription'),
(34, 'B203', 'Autre', 'decription'),
(35, 'B204', 'Autre', 'decription'),
(36, 'B205', 'Club', 'decription'),
(37, 'B206', 'Projet', 'decription'),
(38, 'B207', 'Autre', 'decription'),
(39, 'B208', 'Administration', 'decription'),
(40, 'B209', 'Administration', 'decription'),
(41, 'B210', 'Administration', 'decription'),
(42, 'B211', 'Administration', 'decription'),
(43, 'B212', 'Administration', 'decription'),
(44, 'B213', 'Administration', 'decription'),
(45, 'C201', 'Autre', 'Couloir'),
(46, 'C202', 'TP', 'decription'),
(47, 'C203', 'Cours', 'decription'),
(48, 'C204', 'Cours', 'decription'),
(49, 'C205', 'Informatique', 'decription'),
(50, 'C206', 'Cours', 'decription'),
(51, 'C207', 'Cours', 'decription'),
(52, 'C208', 'Cours', 'decription'),
(53, 'C209', 'Informatique', 'decription'),
(54, 'C210', 'Informatique', 'decription'),
(55, 'C211', 'Autre', 'decription'),
(56, 'C212', 'Autre', 'decription'),
(57, 'C213', 'Informatique', 'decription'),
(58, 'C214', 'Informatique', 'decription'),
(59, 'C215', 'Informatique', 'decription'),
(60, 'C216', 'Informatique', 'decription'),
(61, 'C217', 'Informatique', 'decription'),
(62, 'C218', 'Informatique', 'decription'),
(63, 'C219', 'Autre ', 'decription');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

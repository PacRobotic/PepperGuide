-- phpMyAdmin SQL Dump
-- version 3.3.5
-- http://www.phpmyadmin.net
--
-- Serveur: localhost:3308
-- Généré le : Ven 03 Mai 2019 à 08:36
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
-- Structure de la table `Personnels`
--

CREATE TABLE IF NOT EXISTS `Personnels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `civilite` varchar(4) NOT NULL,
  `nom` varchar(40) NOT NULL,
  `prenom` varchar(40) DEFAULT NULL,
  `localisation` varchar(5) DEFAULT NULL,
  `type` varchar(20) NOT NULL,
  `description` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=102 ;

--
-- Contenu de la table `Personnels`
--

INSERT INTO `Personnels` (`id`, `civilite`, `nom`, `prenom`, `localisation`, `type`, `description`) VALUES
(1, 'Mme', 'Alloui', 'Ilham', 'A229', 'Enseignant', 'Enseignante chercheuse'),
(2, 'Mr', 'Monnet', 'Sébastien', 'A228', 'Enseignant', 'Enseignant chercheur'),
(3, 'Mr', 'Vernier', 'Flavien', 'A227', 'Enseignant', 'Enseignant chercheur'),
(4, 'Mme', 'Cimpan', 'Sorana', 'A226', 'Enseignant', 'Enseignante chercheuse'),
(5, 'Mme', 'Galichet', 'Sylvie', 'A225', 'Enseignant', 'Enseignante chercheuse'),
(6, 'Mr', 'Raoui', 'Rizlène', 'A224', 'Enseignant', 'Enseignant chercheur'),
(7, 'Mr', 'Benoit', 'Alexandre', 'A223', 'Enseignant', 'Enseignant chercheur'),
(8, 'Mr', 'Lesniewska-choquet', 'Charles', 'A222', 'Enseignant', 'Enseignant chercheur'),
(9, 'Mr', 'X1', 'X1', 'A222', 'Administratif', 'decription'),
(10, 'Mr', 'X2', 'X2', 'A222', 'Autre', 'decription'),
(11, 'Mr', 'X3', 'X3', 'A222', 'Administratif', 'decription'),
(12, 'Mr', 'X4', 'X4', 'A222', 'Autre', 'decription'),
(13, 'Mr', 'Pichon', 'Pascal', 'B203', 'Enseignant', 'Enseignant chercheur'),
(14, 'Mr', 'Mandallay', 'Patrick', 'B202', 'Enseignant', 'Enseignant chercheur'),
(15, 'Mr', 'Lesniewska-choquet', 'Charles', 'A222', 'Enseignant', 'Enseignant chercheur'),
(16, 'Mme', 'Degeneve', 'Sophie', 'A210', 'Enseignant', 'Enseignante chercheuse'),
(17, 'Mme', 'X4', 'X4', 'A210', 'Enseignant', 'decription'),
(18, 'Mme', 'Degeneve', 'Sophie', 'A210', 'Enseignant', 'Enseignante chercheuse'),
(19, 'Mr', 'Damas', 'Luc', 'A227', 'Enseignant', 'Enseignant chercheur'),
(20, 'Mr', 'A', 'Test 203', 'A203', 'Enseignant', 'C''est ici'),
(101, 'Mme', 'A', 'Test 204', 'A204', 'Enseignant', 'C''est ici'),
(21, 'Mr', 'A', 'Test 205', 'A205', 'Enseignant', 'C''est ici'),
(22, 'Mme', 'A', 'Test 217', 'A217', 'Enseignant', 'C''est ici');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

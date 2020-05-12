-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 12, 2020 at 06:46 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `QR`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `password`, `type`, `name`) VALUES
('admin@gmail.com', '1234', 'admin', 'Dhara Singh');

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `Deptid` int(11) NOT NULL,
  `Dname` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`Deptid`, `Dname`, `location`) VALUES
(6, 'ECE', '2nd');

-- --------------------------------------------------------

--
-- Table structure for table `entity`
--

CREATE TABLE `entity` (
  `Entityid` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `fathername` varchar(200) NOT NULL,
  `Designation` varchar(200) NOT NULL,
  `Starttime` varchar(50) NOT NULL,
  `Endtime` varchar(50) NOT NULL,
  `coverphoto` varchar(500) NOT NULL,
  `typeofentry` varchar(100) NOT NULL,
  `Deptid` int(11) NOT NULL,
  `Status` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `pdf` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `entity`
--

INSERT INTO `entity` (`Entityid`, `name`, `fathername`, `Designation`, `Starttime`, `Endtime`, `coverphoto`, `typeofentry`, `Deptid`, `Status`, `email`, `password`, `pdf`) VALUES
(9, 'Rana Mccormick', 'Abdul Newman', 'Qui nihil dignissimo', '00:15', '03:30', 'entity/Screenshot from 2020-04-28 17-15-55.png', 'Employee', 6, 'Grant', 'rkb9874@gmail.com', '1234', 'static/pdf/9RanaMccormick.pdf'),
(10, 'Christen Morris', 'Amy Neal', 'Amy Neal', '00:15', '03:30', 'entity/images.jpeg', 'Employee', 6, 'Grant', 'rkb6280@gmail.com', '1234', 'static/pdf/10ChristenMorris.pdf'),
(11, 'Emery Stephenson', 'Hedy Richard', 'Hedy Richard', '00:15', '19:15', 'entity/Screenshot from 2020-04-09 11-00-48.png', 'Employee', 6, 'Grant', 'ravikantgautamjazz@gmail.com', '1234', 'static/pdf/11EmeryStephenson.pdf'),
(13, 'Blossom Duran', 'Candace Marks', 'Aliquid dicta et exe', '00:15', '00:15', 'entity/featured_110.jpg', 'Employee', 6, 'Grant', 'rkb9878@gmail.com', '1234', 'static/pdf/13BlossomDuran.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `Entity_entry`
--

CREATE TABLE `Entity_entry` (
  `Eeid` int(11) NOT NULL,
  `Entityid` int(11) NOT NULL,
  `Dateofentry` date DEFAULT NULL,
  `Timeofentry` time DEFAULT NULL,
  `Exittime` time DEFAULT NULL,
  `exitdate` date DEFAULT NULL,
  `remarks` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Entity_entry`
--

INSERT INTO `Entity_entry` (`Eeid`, `Entityid`, `Dateofentry`, `Timeofentry`, `Exittime`, `exitdate`, `remarks`) VALUES
(6, 10, '2020-05-10', '12:37:53', '11:34:31', '2020-05-11', NULL),
(7, 10, '2020-05-10', '12:39:13', '11:34:31', '2020-05-11', NULL),
(8, 10, '2020-05-10', '12:40:07', '11:34:31', '2020-05-11', NULL),
(9, 10, '2020-05-10', '12:40:48', '11:34:31', '2020-05-11', NULL),
(10, 10, '2020-05-10', '12:41:20', '11:34:31', '2020-05-11', NULL),
(11, 10, '2020-05-10', '12:41:53', '11:34:31', '2020-05-11', NULL),
(12, 13, '2020-05-10', '14:16:12', '14:16:23', '2020-05-10', NULL),
(13, 13, '2020-05-10', '14:33:41', NULL, NULL, NULL),
(14, 10, '2020-05-11', '11:34:08', '11:34:31', '2020-05-11', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `newsid` int(11) NOT NULL,
  `title` varchar(500) NOT NULL,
  `description` longtext NOT NULL,
  `dateofnews` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`newsid`, `title`, `description`, `dateofnews`) VALUES
(3, '\"All Countries Will Face This\": WHO After China Revises COVID-19 Deaths', '<p><span class=987ewqplace_cont987ewq style=987ewq-webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; font-weight: bolder; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Geneva, Switzerland:&nbsp;</span></p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; display: inline; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>The World Health Organization said Friday that many countries would likely follow China in revising up their death counts once they start getting the coronavirus crisis under control.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin: 1.5rem 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Wuhan, the COVID-19 epicentre, admitted missteps in tallying its death toll, abruptly raising the city789qwes count by 50 percent -- following growing world doubts about Chinese transparency over the outbreak.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>The WHO said Wuhan had been overwhelmed by the virus, which emerged in the city in December, and the authorities had been too swamped to ensure every death and infection was properly recorded.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Authorities in Wuhan initially tried to cover up the outbreak, punishing doctors who had raised the alarm online, and there have been questions about the government789qwes recording of infections as it repeatedly changed its counting criteria at the peak of the crisis.<img src=987ewqhttp://i.ndtvimg.com/i/2015-07/world-health-organisation_650x400_81436277251.jpg987ewq style=987ewqwidth: 650px;987ewq></p>', '2020-04-18'),
(4, '\"No Real Evidence\": Chinas Wuhan Lab At Core Of Coronavirus Controversy', '<p><span class=987ewqplace_cont987ewq style=987ewq-webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; font-weight: bolder; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Wuhan:&nbsp;</span></p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; display: inline; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Nestled in the hilly outskirts of Wuhan, the city at the heart of the coronavirus crisis, a Chinese high-security biosafety laboratory is now the subject of US claims it may be the cradle of the pandemic.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin: 1.5rem 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Chinese scientists have said the virus likely jumped from an animal to humans in a market that sold wildlife in Wuhan, but the existence of the lab has fuelled conspiracy theories that the germ spread from the facility.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq><a href=987ewqhttps://www.ndtv.com/world-news/donald-trump-urged-to-work-with-us-allies-on-covid-19-probe-appoint-high-level-envoy-2213254987ewq target=987ewq_self987ewq style=987ewq-webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; cursor: pointer; transition-duration: 200ms; transition-timing-function: linear; transition-delay: 0ms;987ewq>The United States</a>&nbsp;has now brought the allegations into the mainstream, with Secretary of State Mike Pompeo saying US officials are doing a 987ewqfull investigation987ewq into how the virus 987ewqgot out into the world987ewq.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Here are some key questions about the Wuhan Institute of Virology (WIV):</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq><span style=987ewq-webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; font-weight: bolder;987ewq>What is it?</span></p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>The institute is home to the China Centre for Virus Culture Collection, the largest virus bank in Asia which preserves more than 1,500 strains, according to its website.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>The complex contains Asia789qwes first maximum security lab equipped to handle Class 4 pathogens (P4) -- dangerous viruses that pose a high risk of person-to-person transmission, such as Ebola.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>The 300-million-yuan ($42 million) lab was completed in 2015, and finally opened in 2018, with the founder of a French bioindustrial firm, Alain Merieux, acting as a consultant in its construction.<img src=987ewqhttps://c.ndtvimg.com/2020-04/th9chuk_wuhan-institute-of-virology-china-lab_625x300_18_April_20.jpg987ewq style=987ewqwidth: 650px;987ewq></p>', '2020-04-18'),
(5, '987ewqNo Real Evidence987ewq: China789qwes Wuhan Lab At Core Of Coronavirus Controversy', '<p><span class=987ewqplace_cont987ewq style=987ewq-webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; font-weight: bolder; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Wuhan:&nbsp;</span></p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; display: inline; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Nestled in the hilly outskirts of Wuhan, the city at the heart of the coronavirus crisis, a Chinese high-security biosafety laboratory is now the subject of US claims it may be the cradle of the pandemic.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin: 1.5rem 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Chinese scientists have said the virus likely jumped from an animal to humans in a market that sold wildlife in Wuhan, but the existence of the lab has fuelled conspiracy theories that the germ spread from the facility.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq><a href=987ewqhttps://www.ndtv.com/world-news/donald-trump-urged-to-work-with-us-allies-on-covid-19-probe-appoint-high-level-envoy-2213254987ewq target=987ewq_self987ewq style=987ewq-webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; cursor: pointer; transition-duration: 200ms; transition-timing-function: linear; transition-delay: 0ms;987ewq>The United States</a>&nbsp;has now brought the allegations into the mainstream, with Secretary of State Mike Pompeo saying US officials are doing a 987ewqfull investigation987ewq into how the virus 987ewqgot out into the world987ewq.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>Here are some key questions about the Wuhan Institute of Virology (WIV):</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq><span style=987ewq-webkit-tap-highlight-color: transparent; margin: 0px; padding: 0px; font-weight: bolder;987ewq>What is it?</span></p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>The institute is home to the China Centre for Virus Culture Collection, the largest virus bank in Asia which preserves more than 1,500 strains, according to its website.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>The complex contains Asia789qwes first maximum security lab equipped to handle Class 4 pathogens (P4) -- dangerous viruses that pose a high risk of person-to-person transmission, such as Ebola.</p><p style=987ewq-webkit-tap-highlight-color: transparent; margin-right: 0px; margin-bottom: 1.5rem; margin-left: 0px; padding: 0px; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;987ewq>The 300-million-yuan ($42 million) lab was completed in 2015, and finally opened in 2018, with the founder of a French bioindustrial firm, Alain Merieux, acting as a consultant in its construction.<img src=987ewqhttps://c.ndtvimg.com/2020-04/th9chuk_wuhan-institute-of-virology-china-lab_625x300_18_April_20.jpg987ewq style=987ewqwidth: 650px;987ewq></p>', '2020-04-18');

-- --------------------------------------------------------

--
-- Table structure for table `Vehicles`
--

CREATE TABLE `Vehicles` (
  `Vehicleid` int(11) NOT NULL,
  `Stickered` text NOT NULL,
  `vehiclenumber` varchar(200) NOT NULL,
  `Starttime` varchar(100) NOT NULL,
  `Endtime` varchar(100) NOT NULL,
  `Entityid` int(11) NOT NULL,
  `Status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Vehicles`
--

INSERT INTO `Vehicles` (`Vehicleid`, `Stickered`, `vehiclenumber`, `Starttime`, `Endtime`, `Entityid`, `Status`) VALUES
(3, 'static/QR_Code/11pb101547.png', 'pb101547', '00:15', '00:15', 11, 'Grant'),
(5, 'static/QR_Code/12pb104.png', 'pb 104', '00:15', '03:45', 12, 'Grant'),
(6, 'static/QR_Code/9BH-4534g43.png', 'BH-4534 g43', '00:15', '08:30', 9, 'Grant');

-- --------------------------------------------------------

--
-- Table structure for table `Vehicle_Entry`
--

CREATE TABLE `Vehicle_Entry` (
  `Entryid` int(11) NOT NULL,
  `Vehicleid` int(11) NOT NULL,
  `Entrytime` time NOT NULL,
  `Exittime` time DEFAULT NULL,
  `Dateofentry` date NOT NULL,
  `dateofexit` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Vehicle_Entry`
--

INSERT INTO `Vehicle_Entry` (`Entryid`, `Vehicleid`, `Entrytime`, `Exittime`, `Dateofentry`, `dateofexit`) VALUES
(8, 3, '18:56:35', '11:35:16', '2020-05-10', '2020-05-11'),
(17, 3, '19:12:24', '11:35:16', '2020-05-10', '2020-05-11'),
(18, 3, '19:16:18', '11:35:16', '2020-05-10', '2020-05-11'),
(19, 3, '19:18:30', '11:35:16', '2020-05-10', '2020-05-11'),
(20, 3, '11:34:58', '11:35:16', '2020-05-11', '2020-05-11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`Deptid`);

--
-- Indexes for table `entity`
--
ALTER TABLE `entity`
  ADD PRIMARY KEY (`Entityid`);

--
-- Indexes for table `Entity_entry`
--
ALTER TABLE `Entity_entry`
  ADD PRIMARY KEY (`Eeid`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`newsid`);

--
-- Indexes for table `Vehicles`
--
ALTER TABLE `Vehicles`
  ADD PRIMARY KEY (`Vehicleid`);

--
-- Indexes for table `Vehicle_Entry`
--
ALTER TABLE `Vehicle_Entry`
  ADD PRIMARY KEY (`Entryid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `departments`
--
ALTER TABLE `departments`
  MODIFY `Deptid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `entity`
--
ALTER TABLE `entity`
  MODIFY `Entityid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `Entity_entry`
--
ALTER TABLE `Entity_entry`
  MODIFY `Eeid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `newsid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Vehicles`
--
ALTER TABLE `Vehicles`
  MODIFY `Vehicleid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Vehicle_Entry`
--
ALTER TABLE `Vehicle_Entry`
  MODIFY `Entryid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

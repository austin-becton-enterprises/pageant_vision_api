-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Host: database-2.cluster-cx8iuou6u8bi.us-east-2.rds.amazonaws.com:3306
-- Generation Time: Aug 17, 2025 at 06:59 AM
-- Server version: 8.0.39
-- PHP Version: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pv`
--

-- --------------------------------------------------------

--
-- Table structure for table `access`
--

CREATE TABLE `access` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `category_id` varchar(50) DEFAULT NULL,
  `video_id` varchar(50) DEFAULT NULL,
  `grant_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `purchase_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `access_removed`
--

CREATE TABLE `access_removed` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `category_id` varchar(255) NOT NULL,
  `video_id` varchar(255) NOT NULL,
  `grant_time` varchar(255) NOT NULL,
  `purchase_id` int NOT NULL,
  `remove_time` varchar(255) NOT NULL,
  `remove_reason` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `group_cost` varchar(8) DEFAULT NULL,
  `startdate` varchar(255) DEFAULT NULL,
  `pvtv_cat` int DEFAULT NULL,
  `num_contestants` int DEFAULT NULL,
  `net_percentage` varchar(5) DEFAULT NULL,
  `dir_split` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT 'What Director Keeps',
  `logo` varchar(255) DEFAULT NULL,
  `group_only` varchar(8) DEFAULT NULL,
  `background_image` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `dl_access`
--

CREATE TABLE `dl_access` (
  `id` int NOT NULL,
  `uid` int NOT NULL,
  `token` int NOT NULL,
  `expiry` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `dl_access_log`
--

CREATE TABLE `dl_access_log` (
  `id` int NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `ip` varchar(255) NOT NULL,
  `url` text NOT NULL,
  `useragent` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `dl_code_log`
--

CREATE TABLE `dl_code_log` (
  `id` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `useragent` text,
  `token` int DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `time` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `dl_entitlements`
--

CREATE TABLE `dl_entitlements` (
  `id` int NOT NULL,
  `file_id` int NOT NULL,
  `uid` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `dl_files`
--

CREATE TABLE `dl_files` (
  `id` int NOT NULL,
  `filename` varchar(255) NOT NULL,
  `group_id` int NOT NULL,
  `bucket_id` varchar(255) NOT NULL,
  `b2_file_id` text NOT NULL,
  `bucket_name` varchar(255) NOT NULL,
  `size` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `dl_groups`
--

CREATE TABLE `dl_groups` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `bucket_id` varchar(255) NOT NULL,
  `bucket_name` varchar(255) NOT NULL,
  `status` varchar(1) NOT NULL DEFAULT '1' COMMENT '1 = working, 2 = finished'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `dl_log`
--

CREATE TABLE `dl_log` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `file_id` int NOT NULL,
  `entitlement_id` int NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ip` varchar(255) NOT NULL,
  `useragent` text NOT NULL,
  `url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `dl_users`
--

CREATE TABLE `dl_users` (
  `id` int NOT NULL,
  `email` varchar(255) NOT NULL,
  `group_id` int NOT NULL,
  `file_expire` int DEFAULT NULL COMMENT 'Download permitted until',
  `access_expire` int DEFAULT NULL COMMENT 'First login permitted until',
  `reminder_sent` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `drm_disable`
--

CREATE TABLE `drm_disable` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `video_id` int NOT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `time` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `emergency`
--

CREATE TABLE `emergency` (
  `id` int NOT NULL,
  `vid_id` int NOT NULL,
  `text` text NOT NULL,
  `time` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `force_refresh`
--

CREATE TABLE `force_refresh` (
  `id` int NOT NULL,
  `vid_id` varchar(255) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `limited_access`
--

CREATE TABLE `limited_access` (
  `id` int NOT NULL,
  `token` varchar(55) NOT NULL,
  `expiration` varchar(10) NOT NULL,
  `expires_on` int DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `content` text NOT NULL,
  `note` text,
  `tv` varchar(15) NOT NULL DEFAULT 'false'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `live_events`
--

CREATE TABLE `live_events` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `embed` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci COMMENT 'Cloudflare',
  `embed2` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT 'Mux DRM',
  `embed3` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT 'MUX DRM Environment Signing Only',
  `forceShow` int DEFAULT '2',
  `start` varchar(55) NOT NULL,
  `end` varchar(55) NOT NULL,
  `category` int NOT NULL,
  `cost` varchar(10) NOT NULL,
  `location` varchar(55) NOT NULL,
  `timezone` varchar(55) DEFAULT NULL,
  `pvtv` varchar(255) DEFAULT NULL,
  `stream_key` varchar(255) DEFAULT NULL,
  `stream_key2` varchar(255) DEFAULT NULL,
  `muxStreamID` varchar(255) DEFAULT NULL,
  `vote_category` int DEFAULT NULL,
  `vote_end` int DEFAULT NULL,
  `viewable_date` int NOT NULL DEFAULT '1' COMMENT 'Date event is viewable on home page',
  `drm` int NOT NULL DEFAULT '0' COMMENT '0 = no drm, 1 = has drm',
  `replay` varchar(8) DEFAULT NULL,
  `sub_category` int NOT NULL DEFAULT '0',
  `thumb` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `login_log`
--

CREATE TABLE `login_log` (
  `id` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `ip` varchar(255) NOT NULL,
  `time` int NOT NULL,
  `success` varchar(100) NOT NULL,
  `user_token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `packages`
--

CREATE TABLE `packages` (
  `id` int NOT NULL,
  `package` varchar(55) NOT NULL,
  `package_group` int NOT NULL,
  `price` int NOT NULL,
  `subtext` text NOT NULL,
  `subtextstyle` varchar(55) NOT NULL,
  `square_link` varchar(255) NOT NULL,
  `point1` varchar(255) DEFAULT NULL,
  `point2` varchar(255) DEFAULT NULL,
  `point3` varchar(255) DEFAULT NULL,
  `point4` varchar(255) DEFAULT NULL,
  `button` varchar(55) DEFAULT NULL,
  `available` int NOT NULL DEFAULT '1',
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `package_clicks`
--

CREATE TABLE `package_clicks` (
  `id` int NOT NULL,
  `link_id` int NOT NULL,
  `ip` varchar(255) NOT NULL,
  `time` varchar(255) DEFAULT NULL,
  `referrer` varchar(255) DEFAULT NULL,
  `browser` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `package_groups`
--

CREATE TABLE `package_groups` (
  `id` int NOT NULL,
  `pageant_cat_id` int NOT NULL,
  `promo` text,
  `promo_end` int DEFAULT NULL,
  `expire` int DEFAULT NULL,
  `delivery_timeframe` varchar(255) NOT NULL DEFAULT 'Files will be delivered (or shipped, if applicable) within approximately 2-8 weeks of finals or ordering (whichever is latest). Please ensure your personal information entered at time of ordering is correct to avoid delays.',
  `license` varchar(255) NOT NULL DEFAULT 'All video files are licensed for personal use only. Please see our full license terms at <a href="https://pageant.vision/license" class="text-decoration-underline text-light" target="_blank">pageant.vision/license</a>.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `purchases`
--

CREATE TABLE `purchases` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `email` varchar(55) NOT NULL,
  `time` int NOT NULL,
  `stripe_purchase_session_id` varchar(255) NOT NULL,
  `amount` varchar(10) NOT NULL,
  `cat_id` varchar(5) NOT NULL,
  `video_id` varchar(5) NOT NULL,
  `stripe_customer_link` varchar(255) NOT NULL,
  `charge_id` varchar(255) NOT NULL,
  `invoice_id` varchar(255) NOT NULL,
  `discount_applied` varchar(255) DEFAULT NULL,
  `discount_id` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `recently_aired`
--

CREATE TABLE `recently_aired` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `link` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `recently_aired_clicks`
--

CREATE TABLE `recently_aired_clicks` (
  `id` int NOT NULL,
  `link_id` int NOT NULL,
  `ip` varchar(255) NOT NULL,
  `date` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `referrer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `browser` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sub_categories`
--

CREATE TABLE `sub_categories` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `cat_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `email` varchar(155) NOT NULL,
  `password` varchar(255) NOT NULL,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `verified` int NOT NULL DEFAULT '0',
  `token` varchar(155) DEFAULT NULL,
  `pwtoken` varchar(155) DEFAULT NULL,
  `pwtokenexpire` varchar(25) DEFAULT NULL,
  `admin` int NOT NULL DEFAULT '0',
  `allaccess_exp` int DEFAULT NULL,
  `register_time` int NOT NULL,
  `stripe_customer_id` varchar(255) DEFAULT NULL,
  `pvtv_stripe_customer_id` varchar(255) DEFAULT NULL,
  `pvtv_sub_expire` varchar(255) DEFAULT NULL,
  `pvtv_db_user_id` varchar(255) DEFAULT NULL,
  `session_version` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `user_tokens`
--

CREATE TABLE `user_tokens` (
  `id` int NOT NULL,
  `token` varchar(255) NOT NULL,
  `user_id` int NOT NULL,
  `set_time` int NOT NULL,
  `user_agent` text NOT NULL,
  `ip_address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `votes`
--

CREATE TABLE `votes` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `video_id` int NOT NULL,
  `contestant_id` int NOT NULL,
  `ip_address` varchar(255) NOT NULL,
  `user_agent` text NOT NULL,
  `time` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `vote_categories`
--

CREATE TABLE `vote_categories` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `disabled` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `vote_contestants`
--

CREATE TABLE `vote_contestants` (
  `id` int NOT NULL,
  `cat_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `division` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `vote_divisions`
--

CREATE TABLE `vote_divisions` (
  `id` int NOT NULL,
  `cat_id` int NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `waitlist`
--

CREATE TABLE `waitlist` (
  `id` int NOT NULL,
  `package_id` varchar(25) NOT NULL,
  `email` varchar(255) NOT NULL,
  `time` int NOT NULL,
  `ip` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `watch_log`
--

CREATE TABLE `watch_log` (
  `id` int NOT NULL,
  `vid_id` varchar(55) NOT NULL,
  `user_id` int NOT NULL,
  `time` int NOT NULL,
  `ip` varchar(255) NOT NULL,
  `useragent` text NOT NULL,
  `user_token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `watch_log_ping`
--

CREATE TABLE `watch_log_ping` (
  `id` int NOT NULL,
  `vid_id` varchar(55) NOT NULL,
  `user_id` int NOT NULL,
  `time` int NOT NULL,
  `ip` varchar(255) NOT NULL,
  `useragent` text NOT NULL,
  `user_token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `access`
--
ALTER TABLE `access`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`,`category_id`,`video_id`);

--
-- Indexes for table `access_removed`
--
ALTER TABLE `access_removed`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dl_access`
--
ALTER TABLE `dl_access`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dl_access_log`
--
ALTER TABLE `dl_access_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dl_code_log`
--
ALTER TABLE `dl_code_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dl_entitlements`
--
ALTER TABLE `dl_entitlements`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dl_files`
--
ALTER TABLE `dl_files`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dl_groups`
--
ALTER TABLE `dl_groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dl_log`
--
ALTER TABLE `dl_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dl_users`
--
ALTER TABLE `dl_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `drm_disable`
--
ALTER TABLE `drm_disable`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`video_id`),
  ADD KEY `idx_user_id` (`user_id`),
  ADD KEY `idx_video_id` (`video_id`);

--
-- Indexes for table `emergency`
--
ALTER TABLE `emergency`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_emergency_vidid_idid` (`vid_id`,`id`);

--
-- Indexes for table `force_refresh`
--
ALTER TABLE `force_refresh`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `limited_access`
--
ALTER TABLE `limited_access`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `live_events`
--
ALTER TABLE `live_events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `end` (`end`,`viewable_date`),
  ADD KEY `start` (`start`);

--
-- Indexes for table `login_log`
--
ALTER TABLE `login_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `packages`
--
ALTER TABLE `packages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `package_group` (`package_group`);

--
-- Indexes for table `package_clicks`
--
ALTER TABLE `package_clicks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `package_groups`
--
ALTER TABLE `package_groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchases`
--
ALTER TABLE `purchases`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_charge_id` (`charge_id`),
  ADD KEY `user_id` (`user_id`,`cat_id`,`video_id`);

--
-- Indexes for table `recently_aired`
--
ALTER TABLE `recently_aired`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recently_aired_clicks`
--
ALTER TABLE `recently_aired_clicks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sub_categories`
--
ALTER TABLE `sub_categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`),
  ADD KEY `idx_users_id` (`id`);

--
-- Indexes for table `user_tokens`
--
ALTER TABLE `user_tokens`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `votes`
--
ALTER TABLE `votes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `contestant_id` (`contestant_id`);

--
-- Indexes for table `vote_categories`
--
ALTER TABLE `vote_categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vote_contestants`
--
ALTER TABLE `vote_contestants`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cat_id` (`cat_id`),
  ADD KEY `title` (`title`);

--
-- Indexes for table `vote_divisions`
--
ALTER TABLE `vote_divisions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `waitlist`
--
ALTER TABLE `waitlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `watch_log`
--
ALTER TABLE `watch_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `watch_log_ping`
--
ALTER TABLE `watch_log_ping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vid_id` (`vid_id`,`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `access`
--
ALTER TABLE `access`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `access_removed`
--
ALTER TABLE `access_removed`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dl_access`
--
ALTER TABLE `dl_access`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dl_access_log`
--
ALTER TABLE `dl_access_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dl_code_log`
--
ALTER TABLE `dl_code_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dl_entitlements`
--
ALTER TABLE `dl_entitlements`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dl_files`
--
ALTER TABLE `dl_files`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dl_groups`
--
ALTER TABLE `dl_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dl_log`
--
ALTER TABLE `dl_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dl_users`
--
ALTER TABLE `dl_users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `drm_disable`
--
ALTER TABLE `drm_disable`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `emergency`
--
ALTER TABLE `emergency`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `force_refresh`
--
ALTER TABLE `force_refresh`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `limited_access`
--
ALTER TABLE `limited_access`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `live_events`
--
ALTER TABLE `live_events`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `login_log`
--
ALTER TABLE `login_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `packages`
--
ALTER TABLE `packages`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `package_clicks`
--
ALTER TABLE `package_clicks`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `package_groups`
--
ALTER TABLE `package_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `purchases`
--
ALTER TABLE `purchases`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `recently_aired`
--
ALTER TABLE `recently_aired`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `recently_aired_clicks`
--
ALTER TABLE `recently_aired_clicks`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sub_categories`
--
ALTER TABLE `sub_categories`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_tokens`
--
ALTER TABLE `user_tokens`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `votes`
--
ALTER TABLE `votes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vote_categories`
--
ALTER TABLE `vote_categories`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vote_contestants`
--
ALTER TABLE `vote_contestants`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vote_divisions`
--
ALTER TABLE `vote_divisions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `waitlist`
--
ALTER TABLE `waitlist`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `watch_log`
--
ALTER TABLE `watch_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `watch_log_ping`
--
ALTER TABLE `watch_log_ping`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

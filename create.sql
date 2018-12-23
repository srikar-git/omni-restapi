CREATE DATABASE omni1; 

USE omni1;

CREATE TABLE `tbl_users` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tbl_inv` (
  `prod_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `prod_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `store_count` bigint(20) NOT NULL DEFAULT 0,
  `price` bigint(20) NOT NULL DEFAULT 0,
  `create_time` DATE DEFAULT NULL,
  `last_order` bigint(20) DEFAULT 0,
  `last_topup` bigint(20) DEFAULT 0,
  PRIMARY KEY (`prod_id`)
) AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tbl_orders` (
  `order_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `order_date` DATE DEFAULT NULL,
  `total_count` bigint(20) DEFAULT 0,
  `order_value` bigint(20) DEFAULT 0,
  PRIMARY KEY (order_id)
) AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tbl_ord_details` (
  `order_id` bigint(20) NOT NULL,
  `prod_id` bigint(20) NOT NULL,
  `quant` bigint(20) DEFAULT 0,
  `sold_price` bigint(20) NOT NULL DEFAULT 0,
  PRIMARY KEY (order_id,prod_id)
) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `tbl_topups` (
  `topup_id` bigint(20) NOT NULL,
  `prod_id` bigint(20) NOT NULL,
  `topup_date` DATE DEFAULT NULL,
  `count` bigint(20) DEFAULT 0,
  PRIMARY KEY (topup_id,prod_id)
) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

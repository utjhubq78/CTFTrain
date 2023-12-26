-- MySQL Script generated by MySQL Workbench
-- Thu Nov 30 16:42:09 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema MBD
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema MBD
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `MBD` DEFAULT CHARACTER SET utf8 ;
USE `MBD` ;

-- -----------------------------------------------------
-- Table `MBD`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MBD`.`User` (
  `id` INT NOT NULL,
  `login` VARCHAR(45) NULL,
  `pass` VARCHAR(45) NULL,
  `auth` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MBD`.`Flags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MBD`.`Flags` (
  `id` INT NOT NULL,
  `flag` VARCHAR(45) NULL,
  `time` TIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `MBD`.`Send_flags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `MBD`.`Send_flags` (
  `id` INT NULL,
  `id_usr` INT NULL,
  `id_flag` INT NULL,
  `time` TIME NULL,
  INDEX `usr_idx` (`id_usr` ASC) VISIBLE,
  INDEX `flg_idx` (`id_flag` ASC) VISIBLE,
  CONSTRAINT `usr`
    FOREIGN KEY (`id_usr`)
    REFERENCES `MBD`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `flg`
    FOREIGN KEY (`id_flag`)
    REFERENCES `MBD`.`Flags` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

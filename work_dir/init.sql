CREATE DATABASE wordpress;
USE wordpress;

CREATE TABLE User (
  `id` INT NULL,
  `login` VARCHAR(45) NULL,
  `pass` VARCHAR(45) NULL,
  `auth` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE Flags (
  `id` INT AUTO_INCREMENT,
  `flag` VARCHAR(45) NULL,
  `time` TIME NULL,
  PRIMARY KEY (`id`));

CREATE TABLE Send_flags (
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
    ON UPDATE NO ACTION);
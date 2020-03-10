CREATE TABLE `Device` (
	`SerialNumber`	INTEGER NOT NULL UNIQUE,
	`Type`	TEXT NOT NULL,
	`Model`	TEXT NOT NULL,
	`Location`	TEXT NOT NULL,
	`DateOfPurchase`	TEXT NOT NULL,
	`WrittenOff`	TEXT NOT NULL,
	PRIMARY KEY(`SerialNumber`)
);

CREATE TABLE `Monitor` (
	`DateCleaned`	TEXT NOT NULL,
	`SerialNumber`	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY(`SerialNumber`),
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);

CREATE TABLE `Laptop` (
	`WeightKg`	TEXT NOT NULL,
	`SerialNumber`	INTEGER NOT NULL UNIQUE,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`),
	PRIMARY KEY(`SerialNumber`)
);

CREATE TABLE `Printer` (
	`SerialNumber`	INTEGER NOT NULL UNIQUE,
	`Toner`	TEXT NOT NULL,
	`DateChanged`	TEXT NOT NULL,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`),
	PRIMARY KEY(`SerialNumber`)
);
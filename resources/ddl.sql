CREATE DATABASE "Flight-Waypoints";

CREATE TABLE "Canada-Waypoints" (
    wpname varchar(5) PRIMARY KEY,
    lat varchar(25) NOT NULL,
    lon varchar(25) NOT NULL
)

CREATE TABLE "UnitedStates-Waypoints" (
    wpname varchar(5) PRIMARY KEY,
    lat varchar(25) NOT NULL,
    lon varchar(25) NOT NULL
)
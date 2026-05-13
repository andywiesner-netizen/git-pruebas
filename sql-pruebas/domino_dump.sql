PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE equipos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    ciudad TEXT
);
INSERT INTO equipos VALUES(1,'Venezuela','Caracas');
INSERT INTO equipos VALUES(2,'Hebraica','Caracas');
INSERT INTO equipos VALUES(3,'Italo','Caracas');
INSERT INTO equipos VALUES(4,'Portugues','Caracas');
INSERT INTO equipos VALUES(5,'Marina','La Guaira');
CREATE TABLE jugadores (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    equipo_id INTEGER NOT NULL,
    partidas_jugadas INTEGER DEFAULT 0,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id)
);
INSERT INTO jugadores VALUES(1,'Andy',1,12);
INSERT INTO jugadores VALUES(2,'Carlos',2,0);
INSERT INTO jugadores VALUES(3,'María',2,13);
INSERT INTO jugadores VALUES(4,'Pedro',3,30);
INSERT INTO jugadores VALUES(5,'Luisa',4,0);
COMMIT;

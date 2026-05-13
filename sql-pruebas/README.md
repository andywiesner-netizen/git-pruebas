# SQL Pruebas — Fase 2

Mini base de datos de dominó usada para aprender SQL básico.

## Tablas

- **equipos**: id, nombre (unique), ciudad
- **jugadores**: id, nombre, equipo_id (FK → equipos.id), partidas_jugadas

## Recrear la base de datos

```bash
sqlite3 domino.db < domino_dump.sql
```

## Conceptos cubiertos

- CREATE TABLE con constraints (PRIMARY KEY, NOT NULL, UNIQUE, FOREIGN KEY)
- INSERT, UPDATE, DELETE
- SELECT con WHERE, ORDER BY, LIMIT, aliases
- INNER JOIN y LEFT JOIN
- Funciones de agregación: COUNT, SUM, AVG, MAX, MIN
- GROUP BY y HAVING
- COALESCE para manejar NULL
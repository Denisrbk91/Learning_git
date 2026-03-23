

**`GROUP BY`** → **объединяет строки в группы**
**`ORDER BY`** → **сортирует результат**


Запросы выполняются в таком порядке :
SELECT ...
FROM ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...;

## Пример : общие годы работы по зданию

`SELECT building, SUM(years_employed) AS total_years FROM employees GROUP BY building;`

👉 Что делает:

- группирует по `building`
    
- суммирует стаж всех сотрудников в каждом здании


## Пример : сортировка фильмов по году и названию

`SELECT title, year FROM movies ORDER BY year ASC, title ASC;`

👉 Сначала по году,  
👉 если год одинаковый — по названию.
SELECT
    area
FROM 
    ct_database.cell_towers
WHERE
    mcc = 250 AND radio != 'LTE'
GROUP BY 
    area
HAVING 
    count(cell) > 2000;

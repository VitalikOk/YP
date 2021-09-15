SELECT week_number, ticket_amount, festival_week, festival_name
FROM
    (SELECT 
        EXTRACT('week' FROM  arrival_time) AS week_number,
        COUNT(ticket_no) AS ticket_amount
    FROM flights 
    INNER JOIN airports ON airports.airport_code =  flights.arrival_airport
    INNER JOIN ticket_flights ON ticket_flights.flight_id = flights.flight_id 
    WHERE CAST(arrival_time AS date) BETWEEN '2018-07-23' AND '2018-09-30'
        AND city LIKE 'Москва'
    GROUP BY week_number) AS flights
    LEFT JOIN
        (SELECT festival_name, EXTRACT('week' FROM  festival_date) AS festival_week
        FROM festivals
        WHERE festival_city LIKE 'Москва'
            AND CAST(festival_date AS date) BETWEEN '2018-07-23' AND '2018-09-30') AS fest
      ON week_number = festival_week
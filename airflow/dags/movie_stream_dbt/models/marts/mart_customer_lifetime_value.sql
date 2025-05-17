--valor total gasto por cliente e tempo desde a primeira locação.
-- This model calculates the total amount spent by each customer and the time since their first rental.

-- models/marts/mart_customer_lifetime_value.sql

with rental_data as (
    select
        customer_id,
        min(rental_date) as first_rental_date,
        max(rental_date) as last_rental_date
    from {{ ref('stg_rental') }}
    group by customer_id
),

payments as (
    select
        customer_id,
        sum(amount) as total_spent
    from {{ ref('stg_payment') }}
    group by customer_id
)

select
    p.customer_id,
    total_spent,
    first_rental_date,
    current_date - first_rental_date as customer_lifetime_days
from payments p
join rental_data r on p.customer_id = r.customer_id
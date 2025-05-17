-- performance de cada loja (quantidade de locações, receita, etc).

-- models/marts/mart_store_performance.sql

select
    s.store_id,
    count(distinct r.rental_id) as total_rentals,
    sum(p.amount) as total_revenue
from {{ source('public', 'store') }} s
join {{ source('public', 'staff') }} st on s.store_id = st.store_id
join {{ ref('stg_payment') }} p on st.staff_id = p.staff_id
join {{ ref('stg_rental') }} r on p.rental_id = r.rental_id
group by s.store_id
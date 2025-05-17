-- ranking de filmes mais alugados por período (mês/ano).
-- This model ranks the most rented films by month/year.

-- models/staging/stg_payment.sql

with source as (
    select * from {{ source('public', 'payment') }}
),

renamed as (
    select
        payment_id,
        customer_id,
        staff_id,
        rental_id,
        amount,
        payment_date
    from source
)

select * from renamed

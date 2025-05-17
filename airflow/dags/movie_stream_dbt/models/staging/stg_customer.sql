-- models/staging/stg_customer.sql

with source as (

    select * from {{ source('public', 'customer') }}

),

renamed as (

    select
        customer_id,
        first_name,
        last_name,
        email,
        address_id,
        active,
        create_date,
        last_update
    from source

)

select * from renamed
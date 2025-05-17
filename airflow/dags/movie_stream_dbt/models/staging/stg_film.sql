-- models/staging/stg_film.sql

with source as (
    select * from {{ source('public', 'film') }}
),

renamed as (
    select
        film_id,
        title,
        description,
        release_year,
        language_id,
        rental_duration,
        rental_rate,
        length,
        replacement_cost,
        rating,
        last_update
    from source
)

select * from renamed
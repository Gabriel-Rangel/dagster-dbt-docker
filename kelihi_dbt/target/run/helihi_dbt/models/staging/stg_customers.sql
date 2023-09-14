
  create view "dbt_dev"."dagster-dbt"."stg_customers__dbt_tmp"
    
    
  as (
    with source as (
    select * from "dbt_dev"."dagster-dbt"."raw_customers"

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name

    from source

)

select * from renamed
  );
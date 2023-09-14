
  
    

  create  table "dbt_dev"."dagster-dbt"."stg_orders__dbt_tmp"
  
  
    as
  
  (
    with source as (
    select * from "dbt_dev"."dagster-dbt"."raw_orders"

),

renamed as (

    select
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from source

)

select * from renamed
  );
  
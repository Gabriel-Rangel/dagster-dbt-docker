# from dagster_dbt import dbt_run_op
from dagster import job
from ..ops import ops
from ..assets import assets
# from dagster_dbt import dbt_run_op

@job
def job1():
	ops.hello()

@job
def job2():
	ops.hello()

@job
def job3():
	ops.hello()

# @job(resource_defs={
#     "dbt": ops.dbt_assets
# })
# def my_dbt_job():
#     dbt_run_op()
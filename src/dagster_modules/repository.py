from dagster import repository, job
from .assets import assets
from .jobs import jobs
from .schedules import schedules
from .sensors import sensors
from .ops import ops
# from dagster_dbt import dbt_run_op


# @job(resource_defs={
#     "dbt": ops.dbt_assets
# })
# def my_dbt_job():
#     dbt_run_op()

@repository
def dagster_modules():
	return [
			assets.asset1,
			assets.asset2,
			assets.asset3,
			schedules.job1_schedule,
			sensors.job2_sensor,
			jobs.job3
			# my_dbt_job
	]
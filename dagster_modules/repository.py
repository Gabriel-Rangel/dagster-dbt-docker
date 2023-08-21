from dagster import repository, job
from .assets import assets
from .jobs import jobs
from .schedules import schedules
from .sensors import sensors
from .ops import ops


@repository
def dagster_modules():
	return [
			assets.asset1,
			assets.asset2,
			assets.asset3,
			schedules.job1_schedule,
			sensors.job2_sensor,
			jobs.job3
	]
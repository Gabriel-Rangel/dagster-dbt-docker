from dagster import op
# from dagster_dbt import load_assets_from_dbt_project


@op
def hello():
	pass

# @op
# def dbt_assets():
# 	return load_assets_from_dbt_project(project_dir="/opt/dagster/app/kelihi_dbt", profiles_dir="/root/.dbt")


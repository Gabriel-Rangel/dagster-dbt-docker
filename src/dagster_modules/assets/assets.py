from dagster import asset
# from dagster_dbt.asset_defs import load_assets_from_dbt_project


@asset
def asset1():
	pass

@asset
def asset2():
	pass

@asset(group_name="mygroup")
def asset3():
	pass


# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

DA = DBAcademyHelper(course_config, lesson_config)
DA.reset_lesson()
DA.init()

print()

DA.clone_source_table("sales", f"{DA.paths.datasets}/ecommerce/delta", "sales_hist")
DA.clone_source_table("users", f"{DA.paths.datasets}/ecommerce/delta", "users_hist")
DA.clone_source_table("events", f"{DA.paths.datasets}/ecommerce/delta", "events_hist")

DA.clone_source_table("users_update", f"{DA.paths.datasets}/ecommerce/delta")
DA.clone_source_table("events_update", f"{DA.paths.datasets}/ecommerce/delta")

DA.conclude_setup()


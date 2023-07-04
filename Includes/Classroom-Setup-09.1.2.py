# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

lesson_config.name = "jobs_demo_91"

DA = DBAcademyHelper(course_config, lesson_config)
DA.reset_lesson()  # Second in series, but requires reset
DA.init()

DA.paths.stream_path = f"{DA.paths.working_dir}/stream"
DA.data_factory = DltDataFactory(DA.paths.stream_path)

DA.conclude_setup()


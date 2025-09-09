import os

utils_path = os.path.join("app", "utils")

# DATABASE
database_path = os.path.join("app", "database")
images_files_db_path = os.path.join(database_path, "images_files")
images_data_db_path = os.path.join(database_path, "images_data")
labels_db_path = os.path.join(database_path, "labels.json")
models_db_path = os.path.join(database_path, "models.json")


# TEMPORARY DIR
tmp_dir_path = os.path.join("app", "tmp")


# FILES
tfod_xml_template_path = os.path.join(utils_path, "labelling_template.xml")

def write_config_to_file(config_data):
    file_path = ".streamlit/config.toml"

    with open(file_path, "w") as file:
        file.write(config_data)
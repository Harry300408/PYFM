from configparser import ConfigParser

def save_settings(language, res_width, res_height, is_fullscreen, ticspeed) -> ConfigParser:
    
    settings = ConfigParser()

    settings["SETTINGS"] = {
        "NoSettings": "False",
        "language": language,
        "width": res_width,
        "height": res_height,
        "is_fullscreen": is_fullscreen,
        "ticspeed": ticspeed
    }

    with open("././settings.ini", "w") as f:
        settings.write(f)
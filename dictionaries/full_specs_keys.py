
class full_specs_keys:
    fullspecs_keys = dict
    def __init__(self) -> None:
        self.fullspecs_keys = {
            "Model Name" : "",
            "General": {
                "Operating System": "",
                "Custom UI": "",
                "Dimensions": "",
                "Weight": ""
            },
            "Display & Design": {
                "Size": "",
                "Resolution": "",
                "Pixel Density": "",
                "Touch Screen": "",
                "Type": "",
                "Screen To Body Ratio": "",
                "Aspect Ratio": "",
                "Refresh Rate": "",
                "Screen Protection": "",
                "Design": "",
                "Colour Options": [","],
                "Water Resistance": ""
            },
            "Hardware": {
                "Chipset": "",
                "CPU": [],
                "GPU": "",
                "Architecture": "",
                "RAM": "",
                "Internal Storage": "",
                "MicroSD Card Slot": ""
            },
            "Main Camera": {
                "Number of Cameras": "",
                "Resolution": [],
                "Flash": "",
                "Video": [],
                "Features": [","]
            },
            "Front Camera": {
                "Number of Cameras": "",
                "Resolution": "",
                "Flash": "",
                "Video": [","],
                "Features": [","]
            },
            "Battery": {
                "Capacity": "",
                "Type": "",
                "Wireless Charging": "",
                "Fast Charging": ""
            },
            "Security & Sensors": {
                "Fingerprint Sensor": "",
                "Sensors": [","]
            },
            "Connectivity & Audio": {
                "Network": [","],
                "SIM 1 Bands": {
                    "4G Bands":  {
                        "TD-LTE": ["/"],
                        "FD-LTE": ["/"]
                    },
                    "3G Bands": ["/"],
                    "2G Bands": ["/"],
                    "GPRS": "",
                    "EDGE": ""
                },
                "SIM 1 Bands": {
                    "4G Bands":  {
                        "TD-LTE": ["/"],
                        "FD-LTE": ["/"]
                    },
                    "3G Bands": ["/"],
                    "2G Bands": ["/"],
                    "GPRS": "",
                    "EDGE": ""
                },
                "SIM card slots": "",
                "SIM card type": "",
                "Charging Port": "",
                "USB OTG": "",
                "Wi-Fi": "",
                "Wi-Fi Calling": "",
                "Bluetooth": "",
                "NFC": "",
                "GPS": "",
                "FM Radio": "",
                "Loudspeaker": "",
                "3.5mm headphone jack": ""
            }
        }
    def get_dict(self) -> dict:
        return self.fullspecs_keys
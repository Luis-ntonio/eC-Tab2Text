class keys:
    keys = dict

    def __init__(self) -> None:
        self.keys = {
            "Model": "",
            "Operating System": "",
            "Display": [],
            "Design": [],
            "Performance": [],
            "Camera": [],
            "Battery": [],
            "Connectivity": [],
            "Special Features": []
        }
    def get_dict(self) -> dict:
        return self.keys
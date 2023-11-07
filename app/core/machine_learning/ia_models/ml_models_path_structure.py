from typing import Dict

from configuration.configs import settings

app_root_path: str = settings.ROOT_PATH_FOR_DYNACONF + "/app"
ml_models_path: str = f"{app_root_path}/core/machine_learning/ia_models"
detection_path: str = f"{app_root_path}/core/machine_learning/ia_models/detection"

ml_models_dict_path_structure: Dict = {
    "classification": {
    },
    "detection": {
        "scanned_wbc_model": {
            "weights_file_name": "scanned_wbc_model.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "microscope_wbc_model": {
            "weights_file_name": "microscope_wbc_model.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
    },
    "pose": {
    }
}

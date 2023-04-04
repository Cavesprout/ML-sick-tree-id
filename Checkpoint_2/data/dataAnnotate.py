import os
import json

class tree_img:
    def __init__(self, file_name: str, attrs: dict):
        self.file_name = file_name
        self.attrs = attrs

    def get_as_dict(self) -> dict:
        this = {"file_name" : self.file_name}
        this.update(self.attrs)
        return this

data_dict = {}

for file in os.listdir("healthy"):
    tree_data = tree_img(file, {
        "classification" : "healthy"
    })
    data_dict[file] = tree_data.get_as_dict()

for file in os.listdir("sick"):
    tree_data = tree_img(file, {
        "classification" : "sick"
    })
    data_dict[file] = tree_data.get_as_dict()

for file in os.listdir("sick_features"):
    tree_data = tree_img(file, {
        "classification" : "sick_feature"
    })
    data_dict[file] = tree_data.get_as_dict()


# Read annotations into attributes of files
with open("Sick_Tree_Annotations.json") as annotations:
    sick_regions_json = json.load(annotations)
    for img in sick_regions_json["_via_img_metadata"]:
        for region in sick_regions_json["_via_img_metadata"][img]["regions"]:
            data_dict[sick_regions_json["_via_img_metadata"][img]["filename"]]["x"] = region["shape_attributes"]["x"]
            data_dict[sick_regions_json["_via_img_metadata"][img]["filename"]]["y"] = region["shape_attributes"]["y"]
            data_dict[sick_regions_json["_via_img_metadata"][img]["filename"]]["width"] = region["shape_attributes"]["width"]
            data_dict[sick_regions_json["_via_img_metadata"][img]["filename"]]["height"] = region["shape_attributes"]["height"]
            # data_dict[sick_regions_json["_via_img_metadata"][img]["filename"]]["sick_regions"].append(
            #     {
            #     "x" : region["shape_attributes"]["x"],
            #     "y" : region["shape_attributes"]["y"],
            #     "width" : region["shape_attributes"]["width"],
            #     "height" : region["shape_attributes"]["height"]
            #     }
            # )
            # Ensure only one bounding box is captured
            break


data_list = []

for key in data_dict:
    if "x" not in data_dict[key]:
        data_dict[key]["x"] = -1
    if "y" not in data_dict[key]:
        data_dict[key]["y"] = -1
    if "width" not in data_dict[key]:
        data_dict[key]["width"] = -1
    if "height" not in data_dict[key]:
        data_dict[key]["height"] = -1
    data_list.append(data_dict[key])

data_json = json.dumps(data_list)

with open("img_metadata.json", 'w') as of:
    of.write(data_json)
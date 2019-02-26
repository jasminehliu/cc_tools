import cc_dat_utils
import cc_data
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

# Save Data to DAT


# Convert Data
def make_level_library_from_json( json_data ):
    
    level_library = cc_data.CCDataFile()
    
    for level_data in json_data["levels"]:
        level = cc_data.CCLevel()
        
        level.level_number = level_data["level"]
        level.time = level_data["time"]
        level.num_chips = level_data["chipNum"]
        level.upper_layer = level_data["Upper_layer"]
        level.lower_layer = level_data["Lower_layer"]
        
        optional_fields = level_data["optional"]
        hint = cc_data.CCMapHintField(optional_fields["hint"])
        level.add_field(hint)
        title = cc_data.CCMapTitleField(optional_fields["title"])
        level.add_field(title)
        
        
        level_library.add_level(level)
    
    return level_library

# Load Custom Data
input_json_file = "data/jhliu_cc1.json"

with open(input_json_file, "r") as reader:
    json_data = json.load(reader)
level_data = make_level_library_from_json(json_data)

# Save Data to DAT
cc_dat_utils.write_cc_data_to_dat(level_data, "jhliu_cc1.dat")









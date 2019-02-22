import cc_dat_utils
import cc_data

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

# Save Data to DAT


# Convert Data
def make_game_library_from_json( json_data ):
    
    level_library = cc_data.CCDataFile()
    
    for level_data in json_data["games"]:
        game = test_data.Game()
        game.title = game_data["title"]
        game.year = game_data["Year"]
        
        platform_data = game_data["platform"]
        platform = test_data.Platform()
        platform.name = platform_data["name"]
        platform.launch_year = platform_data["year"]
        
        game.platform = platform
        
        game_library.add_game(game)

    
    ### End Add Code Here ###

    return game_library

# Load Custom Data
input_json_file = "data/jhliu_cc1.json"

with open(input_json_file, "r") as reader:
    json_data = json.load(reader)
game_data = make_game_library_from_json(json_data)










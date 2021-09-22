COLOR_TO_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "black": "#000000", "BlueViolet": "#8a2be2",
                "CadetBlue": "#5f9ea0", "coral": "#ff7f50",
                "CornflowerBlue": "#6495ed", "DarkGreen": "#006400",
                "DarkOrchid": "#9932cc", "salmon": "#fa8072"}

for key, value in COLOR_TO_HEX.items():
    print("{:14} is {}".format(key, value))

color_name = input("Enter color name: ")
while color_name != "":
    if color_name in COLOR_TO_HEX:
        print(color_name, "is", COLOR_TO_HEX[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ")

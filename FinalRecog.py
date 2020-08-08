import numpy as np
from skimage import color
from colorthief import ColorThief
import Algorithmia


Imagio = 'C:/Users/12489/Downloads/BlueShirtTest.jpg'
color_thief = ColorThief(Imagio)

main_color = color_thief.get_color(quality=1)

rgb = main_color
hex_code = "".join([format(val, '02X') for val in rgb])

clothing_color = f"#{hex_code}"

color_list = {
    "B0171F": "Red",
    "DC143c": "Red",
    "FFB6C1": "Pink",
    "FFAEB9": "Pink",
    "EEA2AD": "Pink",
    "CD8C95": "Pink",
    "8B5F65": "Brown",
    "FFC0CB": "Pink",
    "FFB5C5": "Pink",
    "EEA9B8": "Pink",
    "CD919E": "Pink",
    "8B636C": "Pink",
    "DB7093": "Pink",
    "FF82AB": "Pink",
    "EE799F": "Pink",
    "CD6889": "Red",
    "8B475D": "Red",
    "FFF0F5": "Pink",
    "EEE0E5": "Pink",
    "CDC1C5": "Grey",
    "8B8386": "Grey",
    "FF3E96": "Pink",
    "EE3A8C": "Pink",
    "CD3278": "Red",
    "8B2252": "Red",
    "FF69B4": "Pink",
    "FF6EB4": "Pink",
    "EE6AA7": "Pink",
    "CD6090": "Pink",
    "8B3A62": "Red",
    "872657": "Red",
    "FF1493": "Pink",
    "EE1289": "Pink",
    "CD1076": "Pink",
    "8B0A50": "Purple",
    "FF34B3": "Pink",
    "EE30A7": "Pink",
    "CD2990": "Pink",
    "8B1C62": "Red",
    "C71585": "Purple",
    "D02090": "Purple",
    "DA70D6": "Purple",
    "FF83FA": "Purple",
    "EE7AE9": "Purple",
    "CD69C9": "Purple",
    "8B4789": "Purple",
    "D8BFD8": "Grey",
    "FFE1FF": "Pink",
    "EED2EE": "Pink",
    "CDB5CD": "Grey",
    "8B7B8B": "Grey",
    "FFBBFF": "Purple",
    "EEAEEE": "Purple",
    "CD96CD": "Purple",
    "8B668B": "Grey",
    "DDA0DD": "Purple",
    "EE82EE": "Purple",
    "FF00FF": "Purple",
    "EE00EE": "Purple",
    "CD00CD": "Purple",
    "8B008B": "Purple",
    "800080": "Purple",
    "BA55D3": "Purple",
    "E066FF": "Purple",
    "D15FEE": "Purple",
    "B452CD": "Purple",
    "7A378B": "Purple",
    "9400D3": "Purple",
    "9932CC": "Purple",
    "BF3EFF": "Purple",
    "B23AEE": "Purple",
    "9A32CD": "Purple",
    "68228B": "Purple",
    "4B0082": "Purple",
    "8A2BE2": "Purple",
    "9B30FF": "Purple",
    "912CEE": "Purple",
    "7D26CD": "Purple",
    "551A8B": "Purple",
    "9370DB": "Purple",
    "AB82FF": "Purple",
    "9F79EE": "Purple",
    "8968CD": "Purple",
    "5D478B": "Grey",
    "483D8B": "Grey",
    "8470FF": "Purple",
    "7B68EE": "Purple",
    "6A5ACD": "Purple",
    "836FFF": "Purple",
    "7A67EE": "Purple",
    "6959CD": "Purple",
    "473C8B": "Purple",
    "F8F8FF": "White",
    "E6E6FA": "Grey",
    "0000FF": "Blue",
    "0000EE": "Blue",
    "0000CD": "Blue",
    "00008B": "Blue",
    "000080": "Blue",
    "191970": "Blue",
    "3D59AB": "Blue",
    "4169E1": "Blue",
    "4876FF": "Blue",
    "436EEE": "Blue",
    "3A5FCD": "Blue",
    "27408B": "Blue",
    "6495ED": "Blue",
    "B0C4DE": "Blue",
    "CAE1FF": "Blue",
    "BCD2EE": "Blue",
    "A2B5CD": "Blue",
    "6E7B8B": "Grey",
    "778899": "Grey",
    "708090": "Grey",
    "C6E2FF": "Blue",
    "B9D3EE": "Blue",
    "9FB6CD": "Blue",
    "6C7B8B": "Grey",
    "1E90FF": "Blue",
    "1C86EE": "Blue",
    "1874CD": "Blue",
    "104E8B": "Blue",
    "F0F8FF": "White",
    "4682B4": "Blue",
    "63B8FF": "Blue",
    "5CACEE": "Blue",
    "4F94CD": "Blue",
    "36648B": "Blue",
    "87CEFA": "Blue",
    "B0E2FF": "Blue",
    "A4D3EE": "Blue",
    "8DB6CD": "Blue",
    "607B8B": "Grey",
    "87CEFF": "Blue",
    "7EC0EE": "Blue",
    "6CA6CD": "Blue",
    "4A708B": "Blue",
    "87CEEB": "Blue",
    "00BFFF": "Blue",
    "00B2EE": "Blue",
    "009ACD": "Blue",
    "00688B": "Blue",
    "33A1C9": "Blue",
    "ADD8E6": "Blue",
    "BFEFFF": "Blue",
    "B2DFEE": "Blue",
    "9AC0CD": "Blue",
    "68838B": "Grey",
    "B0E0E6": "Blue",
    "98F5FF": "Blue",
    "8EE5EE": "Blue",
    "7AC5CD": "Blue",
    "53868B": "Blue",
    "00F5FF": "Blue",
    "00E5EE": "Blue",
    "00C5CD": "Blue",
    "00868B": "Blue",
    "5F9EA0": "Blue",
    "00CED1": "Blue",
    "F0FFFF": "White",
    "E0EEEE": "Grey",
    "C1CDCD": "Grey",
    "838B8B": "Grey",
    "E0FFFF": "Blue",
    "D1EEEE": "Blue",
    "B4CDCD": "Blue",
    "7A8B8B": "Blue",
    "BBFFFF": "Blue",
    "AEEEEE": "Blue",
    "96CDCD": "Blue",
    "668B8B": "Blue",
    "2F4F4F": "Grey",
    "97FFFF": "Blue",
    "8DEEEE": "Blue",
    "79CDCD": "Blue",
    "528B8B": "Blue",
    "00FFFF": "Blue",
    "00EEEE": "Blue",
    "00CDCD": "Blue",
    "008B8B": "Blue",
    "008080": "Blue",
    "48D1CC": "Blue",
    "20B2AA": "Blue",
    "03A89E": "Blue",
    "40E0D0": "Blue",
    "808A87": "Grey",
    "00C78C": "Green",
    "7FFFD4": "Green",
    "76EEC6": "Green",
    "66CDAA": "Green",
    "458B74": "Green",
    "00FA9A": "Green",
    "F5FFFA": "White",
    "00FF7F": "Green",
    "00EE76": "Green",
    "00CD66": "Green",
    "008B45": "Green",
    "3CB371": "Green",
    "54FF9F": "Green",
    "4EEE94": "Green",
    "43CD80": "Green",
    "2E8B57": "Green",
    "00C957": "Green",
    "BDFCC9": "Green",
    "3D9140": "Green",
    "F0FFF0": "Green",
    "E0EEE0": "Grey",
    "C1CDC1": "Grey",
    "838B83": "Grey",
    "8FBC8F": "Green",
    "C1FFC1": "Green",
    "B4EEB4": "Green",
    "9BCD9B": "Green",
    "698B69": "Green",
    "98FB98": "Green",
    "9AFF9A": "Green",
    "90EE90": "Green",
    "7CCD7C": "Green",
    "548B54": "Green",
    "32CD32": "Green",
    "228B22": "Green",
    "00FF00": "Green",
    "00EE00": "Green",
    "00CD00": "Green",
    "008B00": "Green",
    "008000": "Green",
    "006400": "Green",
    "308014": "Green",
    "7CFC00": "Green",
    "7FFF00": "Green",
    "76EE00": "Green",
    "66CD00": "Green",
    "458B00": "Green",
    "ADFF2F": "Green",
    "CAFF70": "Green",
    "BCEE68": "Green",
    "2CD5A": "Green",
    "6E8B3D": "Green",
    "556B2F": "Green",
    "6B8E23": "Green",
    "C0FF3E": "Green",
    "B3EE3A": "Green",
    "9ACD32": "Green",
    "698B22": "Green",
    "FFFFF0": "White",
    "EEEEE0": "Grey",
    "CDCDC1": "Grey",
    "8B8B83": "Grey",
    "F5F5DC": "Grey",
    "FFFFE0": "White",
    "EEEED1": "Grey",
    "CDCDB4": "Grey",
    "B8B7A": "Grey",
    "FAFAD2": "Grey",
    "FFFF00": "Yellow",
    "EEEE00": "Yellow",
    "CDCD00": "Yellow",
    "8B8B00": "Yellow",
    "808069": "Yellow",
    "808000": "Yellow",
    "BDB76B": "Yellow",
    "FFF68F": "Yellow",
    "EEE685": "Yellow",
    "CDC673": "Yellow",
    "8B864E": "Yellow",
    "F0E68C": "Yellow",
    "EEE8AA": "Yellow",
    "FFFACD": "White",
    "EEE9BF": "Yellow",
    "CDC9A5": "Yellow",
    "8B8970": "Grey",
    "FFEC8B": "Yellow",
    "EEDC82": "Yellow",
    "CDBE70": "Yellow",
    "8B814C": "Brown",
    "E3CF57": "Yellow",
    "FFD700": "Yellow",
    "EEC900": "Yellow",
    "CDAD00": "Yellow",
    "8B7500": "Brown",
    "FFF8DC": "White",
    "EEE8CD": "Grey",
    "CDC8B1": "Grey",
    "8B8878": "Grey",
    "DAA520": "Yellow",
    "FFC125": "Yellow",
    "EEB422": "Yellow",
    "CD9B1D": "Yellow",
    "8B6914": "Brown",
    "B8860B": "Brown",
    "FFB90F": "Yellow",
    "EEAD0E": "Yellow",
    "CD950C": "Yellow",
    "8B6508": "Brown",
    "FFA500": "Orange",
    "EE9A00": "Orange",
    "CD8500": "Orange",
    "8B5A00": "Brown",
    "FFFAF0": "White",
    "FDF5E6": "White",
    "F5DEB3": "Yellow",
    "FFE7BA": "Yellow",
    "EED8AE": "Yellow",
    "CDA96": "Grey",
    "8B7E66": "Grey",
    "FFE4B5": "Yellow",
    "FFEFD5": "Pink",
    "FFEBCD": "Pink",
    "FFDEAD": "Yellow",
    "EECFA1": "Yellow",
    "CDB38B": "Grey",
    "8B795E": "Grey",
    "FCE6C9": "Pink",
    "D2B48C": "Brown",
    "9C661F": "Brown",
    "FF9912": "Orange",
    "FAEBD7": "White",
    "FFEFDB": "White",
    "EEDFCC": "White",
    "CDC0B0": "Grey",
    "8B8378": "Grey",
    "DEB887": "Brown",
    "FFD39B": "Brown",
    "EEC591": "Brown",
    "CDAA7D": "Brown",
    "8B7355": "Brown",
    "FFE4C4": "Pink",
    "EED5B7": "Grey",
    "CDB79E": "Brown",
    "8B7D6B": "Grey",
    "E3A869": "Orange",
    "ED9121": "Orange",
    "FF8C00": "Orange",
    "FF7F00": "Orange",
    "EE7600": "Orange",
    "CD6600": "Orange",
    "8B4500": "Orange",
    "FF8000": "Orange",
    "FFA54F": "Orange",
    "EE9A49": "Orange",
    "CD853F": "Orange",
    "8B5A2B": "Brown",
    "FAF0E6": "White",
    "FFDAB9": "Orange",
    "EECBAD": "Orange",
    "CDAF95": "Brown",
    "8B7765": "Brown",
    "FFF5EE": "White",
    "EEE5DE": "White",
    "CDC5BF": "Grey",
    "8B8682": "Grey",
    "F4A460": "Orange",
    "C76114": "Orange",
    "D2691E": "Orange",
    "FF7F24": "Orange",
    "EE7621": "Orange",
    "CD661D": "Orange",
    "8B4513": "Brown",
    "292421": "Black",
    "FF7D40": "Orange",
    "FF6103": "Orange",
    "8A360F": "Orange",
    "A0522D": "Orange",
    "FF8247": "Orange",
    "EE7942": "Orange",
    "CD6839": "Orange",
    "8B4726": "Orange",
    "FFA07A": "Orange",
    "EE9572": "Orange",
    "CD8162": "Orange",
    "8B5742": "Orange",
    "FF7F50": "Orange",
    "FF4500": "Orange",
    "EE4000": "Red",
    "CD3700": "Red",
    "8B2500": "Red",
    "5E2612": "Brown",
    "E9967A": "Orange",
    "FF8C69": "Orange",
    "EE8262": "Orange",
    "CD7054": "Orange",
    "8B4C39": "Brown",
    "FF7256": "Orange",
    "EE6A50": "Orange",
    "CD5B45": "Orange",
    "8B3E2F": "Orange",
    "8A3324": "Orange",
    "FF6347": "Orange",
    "EE5C42": "Orange",
    "CD4F39": "Orange",
    "8B3626": "Orange",
    "FA8072": "Orange",
    "FFE4E1": "Pink",
    "EED5D2": "Pink",
    "CDB7B5": "Grey",
    "8B7D7B": "Grey",
    "FFFAFA": "White",
    "EEE9E9": "White",
    "CDC9C9": "Grey",
    "8B8989": "Grey",
    "BC8F8F": "Brown",
    "FFC1C1": "Pink",
    "EEB4B4": "Pink",
    "CD9B9B": "Brown",
    "8B6969": "Brown",
    "F08080": "Pink",
    "CD5C5C": "Pink",
    "FF6A6A": "Pink",
    "EE6363": "Pink",
    "8B3A3A": "Red",
    "CD5555": "Red",
    "A52A2A": "Red",
    "FF4040": "Red",
    "EE3B3B": "Red",
    "CD3333": "Red",
    "8B2323": "Red",
    "B22222": "Red",
    "FF3030": "Red",
    "EE2C2C": "Red",
    "CD2626": "Red",
    "8B1A1A": "Red",
    "FF0000": "Red",
    "EE0000": "Red",
    "CD0000": "Red",
    "8B0000": "Red",
    "800000": "Red",
    "8E388E": "Purple",
    "7171C6": "Blue",
    "7D9EC0": "Blue",
    "388E8E": "Green",
    "71C671": "Green",
    "8E8E38": "Green",
    "C5C1AA": "Grey",
    "C67171": "Pink",
    "555555": "Grey",
    "1E1E1E": "Black",
    "282828": "Black",
    "515151": "Grey",
    "5B5B5B": "Grey",
    "848484": "Grey",
    "8E8E8E": "Grey",
    "AAAAAA": "Grey",
    "B7B7B7": "Grey",
    "C1C1C1": "Grey",
    "EAEAEA": "White",
    "F4F4F4": "White",
    "FFFFFF": "White",
    "F5F5F5": "White",
    "DCDCDC": "Grey",
    "D3D3D3": "Grey",
    "C0C0C0": "Grey",
    "A9A9A9": "Grey",
    "808080": "Grey",
    "696969": "Grey",
    "000000": "Black",
    "FCFCFC": "White",
    "FAFAFA": "White",
    "F7F7F7": "White",
    "F5F5F5": "White",
    "F2F2F2": "White",
    "F0F0F0": "Grey",
    "EDEDED": "Grey",
    "EBEBEB": "Grey",
    "E8E8E8": "Grey",
    "E5E5E5": "Grey",
    "E3E3E3": "Grey",
    "E0E0E0": "Grey",
    "DEDEDE": "Grey",
    "DBDBDB": "Grey",
    "D9D9D9": "Grey",
    "D6D6D6": "Grey",
    "D4D4D4": "Grey",
    "D1D1D1": "Grey",
    "CFCFCF": "Grey",
    "CCCCCC": "Grey",
    "C9C9C9": "Grey",
    "C7C7C7": "Grey",
    "C4C4C4": "Grey",
    "C2C2C2": "Grey",
    "BFBFBF": "Grey",
    "BDBDBD": "Grey",
    "BABABA": "Grey",
    "B8B8B8": "Grey",
    "B5B5B5": "Grey",
    "B3B3B3": "Grey",
    "B0B0B0": "Grey",
    "ADADAD": "Grey",
    "ABABAB": "Grey",
    "A8A8A8": "Grey",
    "A6A6A6": "Grey",
    "A3A3A3": "Grey",
    "A1A1A1": "Grey",
    "9E9E9E": "Grey",
    "9C9C9C": "Grey",
    "999999": "Grey",
    "969696": "Grey",
    "949494": "Grey",
    "919191": "Grey",
    "8F8F8F": "Grey",
    "8C8C8C": "Grey",
    "8A8A8A": "Grey",
    "878787": "Grey",
    "858585": "Grey",
    "828282": "Grey",
    "7F7F7F": "Grey",
    "7D7D7D": "Grey",
    "7A7A7A": "Grey",
    "787878": "Grey",
    "757575": "Grey",
    "737373": "Grey",
    "707070": "Grey",
    "6E6E6E": "Grey",
    "6B6B6B": "Grey",
    "696969": "Grey",
    "666666": "Grey",
    "636363": "Grey",
    "616161": "Grey",
    "5E5E5E": "Grey",
    "5C5C5C": "Grey",
    "595959": "Grey",
    "575757": "Grey",
    "545454": "Grey",
    "525252": "Grey",
    "4F4F4F": "Black",
    "4D4D4D": "Black",
    "4A4A4A": "Black",
    "474747": "Black",
    "454545": "Black",
    "424242": "Black",
    "404040": "Black",
    "3D3D3D": "Black",
    "3B3B3B": "Black",
    "383838": "Black",
    "363636": "Black",
    "333333": "Black",
    "303030": "Black",
    "2E2E2E": "Black",
    "2B2B2B": "Black",
    "292929": "Black",
    "262626": "Black",
    "242424": "Black",
    "212121": "Black",
    "1F1F1F": "Black",
    "1C1C1C": "Black",
    "1A1A1A": "Black",
    "171717": "Black",
    "141414": "Black",
    "121212": "Black",
    "0F0F0F": "Black",
    "0D0D0D": "Black",
    "0A0A0A": "Black",
    "080808": "Black",
    "050505": "Black",
    "030303": "Black",
}

hex_rgb_colors = list(color_list.keys())

r = [int(hex[0:2], 16) for hex in hex_rgb_colors]
g = [int(hex[2:4], 16) for hex in hex_rgb_colors]
b = [int(hex[4:6], 16) for hex in hex_rgb_colors]

r = np.asarray(r, np.uint8)
g = np.asarray(g, np.uint8)
b = np.asarray(b, np.uint8)

rgb = np.dstack((r, g, b))
lab = color.rgb2lab(rgb)

clothing_rgb = np.asarray([int(clothing_color[1:3], 16), int(clothing_color[3:5], 16), int(clothing_color[5:7], 16)],
                          np.uint8)
clothing_rgb = np.dstack((clothing_rgb[0], clothing_rgb[1], clothing_rgb[2]))
clothing_lab = color.rgb2lab(clothing_rgb)

lab_dist = ((lab[:, :, 0] - clothing_lab[:, :, 0]) ** 2 + (lab[:, :, 1] - clothing_lab[:, :, 1]) ** 2 + (
            lab[:, :, 2] - clothing_lab[:, :, 2]) ** 2) ** 0.5

min_index = lab_dist.argmin()

clothing_closest_hex = hex_rgb_colors[min_index]

clothing_color_name = color_list[clothing_closest_hex]

input = {
    "image": [
        "https://www-cdn.champion.com/catalog/product/h/n/hns_t23898_hns_t23898_frontierblue_front.jpg?quality=85&bg-color=255,255,255&fit=bounds&height=940&width=750&canvas=750:940"
    ],
    "model": "small",
    "tags_only": False
}
client = Algorithmia.client('simoRA7ehGxR5RjQKBmc6Aan+L61')
algo = client.algo('algorithmiahq/DeepFashion/1.5.1')
algo.set_options(timeout=300)  # optional

list = algo.pipe(input).result
x = list[0]
y = str(x)
z = y.split("'")

file = open(Imagio + ' Info.txt', 'w')
file.write("Clothing Color: " + clothing_color_name + "\n")
file.write("Clothing Type: " + z[5])
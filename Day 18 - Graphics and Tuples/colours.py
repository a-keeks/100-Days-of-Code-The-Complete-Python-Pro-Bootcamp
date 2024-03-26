import matplotlib.colors as mcolors


all_colours = list(mcolors.CSS4_COLORS)

white_colours = {"aliceblue", 
"antiquewhite", 
"azure", 
"beige", 
"bisque", 
"blanchedalmond", 
"cornsilk", 
"floralwhite", 
"ghostwhite",  
"gray", 
"grey", 
"honeydew", 
"ivory", 
"lavender", 
"lavenderblush", 
"lemonchiffon", 
"lightgoldenrodyellow", 
"lightyellow", 
"linen", 
"mintcream", 
"mistyrose", 
"moccasin", 
"navajowhite", 
"oldlace",  
"palegoldenrod", 
"papayawhip", 
"peachpuff", 
"rebeccapurple", 
"seashell", 
"snow", 
"white", 
"whitesmoke"}

all_colours_wthout_white = [ele for ele in all_colours if ele not in white_colours]
def travel_distance(height, co, times):
    if times == None:
        height = 2*height/(1+co)/(1-co)
    else:
        while times > 0:
            height += (height*co)
            times -= 1
    return height

print(travel_distance(100, 0.5, 10))
    
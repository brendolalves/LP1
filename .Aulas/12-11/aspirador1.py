def lerSensor(pos, ambiente):
    x = pos[0]
    y = pos[1]

    for i in (x-1,3):
        
        for j in (y-1,3):
            print(ambiente[i])


ambiente = [ 
    [0, 0, 0], 
    [0, 0, 1], 
    [1, 0, 1] 
    ]

ambiente[1][2] = 0
pos = [1,1]

lerSensor(pos, ambiente)

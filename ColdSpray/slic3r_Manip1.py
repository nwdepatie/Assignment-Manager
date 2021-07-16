import json
from matplotlib import pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

#hardcoded values
layerIncrement = .4     #distance between each layer
startuperror = 0
x_points = list()       # empty list to append x values to and plot
y_points = list()       # same but for y values
coordList = list()      # x/y points grouped into coordinates
x_hullPoints = list()
y_hullPoints = list()
master_hullvertices=list()
master_extendedhullvertices=list()
data_file = str()


adjustablelength=20   #millimeters the rastor path travels above and below the cross section



# Potential parsed JSON files (switch between when loading JSON)
filePath_out = "C:/Users/nwdep/OneDrive/Documents/!Desktop/Folders/RIVeR/ColdSpray/ColdSpray/Parsed_GCode/out.json"  # smaller increments between points
filePath_cylinder = "c:/Users/nwdep/OneDrive/Documents/!Desktop/Folders/RIVeR/ColdSpray/ColdSpray/Parsed_GCode/cylinder.json"
filePath_testCube = "c:/Users/nwdep/OneDrive/Documents/!Desktop/Folders/RIVeR/ColdSpray/ColdSpray/Parsed_GCode/test_cube.json"

# loads JSON file
with open(filePath_testCube) as data_file:      #file path can be switched out using paths above 
    stl = json.load(data_file)



#function that retrieves x,y values in json file
def pointRetrieve(stl, layer, pos):
    x1 = stl[layer][pos][0]    #point 1
    y1 = stl[layer][pos][1]

    x2 = stl[layer][pos-1][0]  #point 2
    y2 = stl[layer][pos-1][1]
    
    x3 = stl[layer][pos-2][0]  #point 3
    y3 = stl[layer][pos-2][1]
    return x1, y1, x2, y2, x3, y3



# add x&y points to list as they come through
def appendPoints(x1, y1):
    x_points.append(x1)
    y_points.append(y1)



def ConvexHullPlot(x_points, y_points):
    coordList = zip(x_points, y_points)     # joins x/y point lists into coordinates
    coords = set(coordList)
    coords = list(coords)
    coords = np.array(coords)   # converts list of coordinates to array to pass to plotter


    # attempts to create a convex hull
    hull = ConvexHull(coords)
    
    ##  Plotting for viewing purposes  **make sure plt.show is uncommented**

    #plt.plot(coords[:,0], coords[:,1], 'o')
        
    #for simplex in hull.simplices:
    #    plt.plot(coords[simplex, 0], coords[simplex, 1], 'k-')
    
    plt.plot(coords[hull.vertices,0], coords[hull.vertices,1], 'r--', lw=2)        
    plt.plot(coords[hull.vertices[0],0], coords[hull.vertices[0],1], 'ro')



    x_hullPoints=coords[hull.vertices,0]       #records the x coordinates of the hull vertices
    y_hullPoints=coords[hull.vertices,1]       #records the y coordinates of the hull vertices
    hull_coordList = list(zip(x_hullPoints, y_hullPoints))      

    enlargedhull_coordList=enlargehull(x_hullPoints,y_hullPoints)    #creates a hull that is expanded in the y direction
    
    return coords, hull_coordList, enlargedhull_coordList


#creates a hull that is expanded in the y direction
def enlargehull(x_hullPoints,y_hullPoints):

    y1_points=list()
    x1_points=list()

    for a in range(len(y_hullPoints)):
        
        y_position=y_hullPoints[a]    #indexing the x and y coordinates of each vertex in the main hull
        x_position=x_hullPoints[a]
        
        y_below=y_position-adjustablelength         #adding a certain length below the vertex
        y_above=y_position+adjustablelength         #adding a certain length above the vertex

        x1_points.extend((x_position,x_position,x_position))
        y1_points.extend((y_below,y_position,y_above))
        

    enlarged_coordList=list(zip(x1_points,y1_points))
    enlarged_coords = set(enlarged_coordList)
    enlarged_coords = list(enlarged_coords)
    enlarged_coords = np.array(enlarged_coords)

    enlarged_hull=ConvexHull(enlarged_coords)      #creating a new, larger convex hull to expand in y direction

    ## Plotting for viewing purposes  **make sure plt.show is uncommented**

    #plt.plot(enlarged_coords[:,0], enlarged_coords[:,1], 'g')

    plt.plot(enlarged_coords[enlarged_hull.vertices,0], enlarged_coords[enlarged_hull.vertices,1], 'b--', lw=2)        
    plt.plot(enlarged_coords[enlarged_hull.vertices[0],0], enlarged_coords[enlarged_hull.vertices[0],1], 'go')



    x1_hullPoints=enlarged_coords[enlarged_hull.vertices,0]
    y1_hullPoints=enlarged_coords[enlarged_hull.vertices,1]

    enlargedhull_coordList = list(zip(x1_hullPoints, y1_hullPoints))

    return enlargedhull_coordList


def coordOutput(data):                        #outputs coordinate data to a .json file

    filename="c:/Users/nwdep/OneDrive/Documents/ColdSpray/coordsList.json"
    data=json.dumps(data)

    try:
        f = open(filename, "x")
    except:
        f = open(filename, "w")
    finally:
        data=str(data)
        f.write(data)
        f.close()
    

#for loop that iterates through json file to graph layer shape
layers = sorted([float(z) for z in stl.keys()])
for layer in layers:
    layer = str(layer)
    for pos in range(len(stl[layer])):
        x1, y1, x2, y2, x3, y3 = pointRetrieve(stl, layer, pos)

        # call append function to create list
        appendPoints(x1, y1)
        
        # create plot once all points have been added to a list
        if pos == len(layers):
            try:
                coords, hull_coordList, enlargedhull_coordList = ConvexHullPlot(x_points, y_points)  # call function to create surrounding convexHull

                master_hullvertices.append(hull_coordList)  #creates a master coordinate list of hull points
                master_extendedhullvertices.append(enlargedhull_coordList)   #creates a master coordinate list of expanded hull points
                plt.show()  # output all plots

            except:
                startuperror = startuperror + 1   #indicates how many layers contained bad data, e.g. straight line only
                continue

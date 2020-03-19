import imageio
import glob
import os
from os import listdir
from os.path import isfile, join

filenames = glob.glob("Outputs/New_Cases_Per_Day/*.png")
filenames.sort()
images = []

for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('Outputs/Gif_Dir/new_cases_per_day.gif', images, duration=1)




filenames = glob.glob("Outputs/New_Cases_Per_Day_Density/*.png")
filenames.sort()
images = []

for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('Outputs/Gif_Dir/new_cases_per_day_density.gif', images, duration=1)
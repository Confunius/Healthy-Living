from zipfile import ZipFile
import os, sys

#unzip Healthy-Living.zip
zipref = ZipFile('/workspaces/Healthy-Living/EcoFashion-Hub-main (2).zip', 'r')
zipref.extractall()
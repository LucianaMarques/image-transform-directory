# Image Trasformation script

This is a python script for image transformation to images within a certain folder. It applies the given transformation and saves the result into another folder.

## Usage

First, create a folder with the images to be transformed and copy its path. 

Next, run the following command for erosion:

```
$ python script.py --origin='[path_to_image_source]' --destiny='[path_to_image_transformation_results] --trans='erosion'
```

And this for dilating:

```
$ python script.py --origin='[path_to_image_source]' --destiny='[path_to_image_transformation_results]' --trans='dilating'
```

## Basic information

The command has three required prefixes:

* origin: the images' source folder
* destiny: the images' transformation folder
* trans: the desired image transformation to be applied to the source

The path to the images' source should be previously created, but the destination folder not necessarily has to be. The script will handle the case in which the destination directory is not previously created. 
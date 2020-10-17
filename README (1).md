## FREESPACE SEGMENTATION WITH FULLY CONVOLUTIONAL NEURAL NETWORKS
In this project, we aim to detect drivable areas using python, pytorch, opencv etc. technologies.
### The result we will get at the end of the project;
![result](https://i.hizliresim.com/lTGPiq.jpg)
---
### Json to Mask
As a result of labeled the images, we obtain json files.
These Json files contain the exterior point locations of the freespace class.
In our annotation files, json files have the structure as in the following;


![json](https://i.hizliresim.com/tFMgms.png)

It was determined which pixel belongs to which object.
Json files were converted to mask images in order to determine the locations with freespace in the image.

The ***fillPoly*** function of the **cv2** library was used to draw a mask.

    cv2.fillPoly(mask,np.array([obj['points']['exterior']]),color=1)
Mask example; 

![mask](https://i.hizliresim.com/Ezwl4s.png)

You can find the line by line explanations of the codes of this section from the [json2mask.py](src/json2mask.py) file.
### Mask on Image


import cv2
import os
from flojoy import flojoy, JobResultBuilder, DataContainer
from PIL import Image
import numpy as np

@flojoy
def CAMERA(v, params):
    '''
    Take a picture from a connected camera using OpenCV.
    If no camera is connected, this will load the example image: "object_detection.png".
    Perhaps after testing is finished, an error should be thrown if no camera was detected.
    '''
    print('parameters passed to CAMERA: ', params)
    red_channel = []
    green_channel = []
    blue_channel = []
    alpha_channel = []
    try:
        camera = cv2.VideoCapture(int(params['camera_ind']))  # Camera indicator for selection of specific camera
        return_value, image = camera.read()  # Read camera
        if image is None:
            raise cv2.error
        filePath = "camera.png"
        # f = Image.open(image)
        img_array = image #np.array(f.convert('RGBA'))
        camera.release()  # Release the camera for further use.
        del(camera)
        if img_array.shape[2] == 4:
            red_channel = img_array[:,:,0]
            green_channel = img_array[:,:,1]
            blue_channel = img_array[:,:,2]
            alpha_channel = img_array[:,:,3]
        else:
            red_channel = img_array[:,:,0]
            green_channel = img_array[:,:,1]
            blue_channel = img_array[:,:,2]
            alpha_channel = None
        
    except cv2.error as camera_error:  # Catch error for when a camera isn't detected.
        print('OpenCV cannot read the specified camera.')
        # Get the absolute path of the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the asset file
        filePath= os.path.join(current_dir, 'assets', 'object_detection.png') # Load example image instead. Should it throw an error?
        print ("File to be loaded: " + filePath)
        f = Image.open(filePath)
        img_array = np.array(f.convert('RGBA'))
        if img_array.shape[2] == 4:
            red_channel = img_array[:,:,0]
            green_channel = img_array[:,:,1]
            blue_channel = img_array[:,:,2]
            alpha_channel = img_array[:,:,3]
        else:
            red_channel = img_array[:,:,0]
            green_channel = img_array[:,:,1]
            blue_channel = img_array[:,:,2]
            alpha_channel = None
    
    data_container = DataContainer(type = 'image',r=red_channel, g=green_channel, b=blue_channel, a=alpha_channel)
    
    return JobResultBuilder().from_data(data_container).to_plot(plot_type='image')
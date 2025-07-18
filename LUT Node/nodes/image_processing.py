import numpy as np
import cv2
import torch
def tensor_to_opencv(batch):
    image = batch[0].numpy()
    image = (image * 255).astype(np.uint8)

    return image

def opencv_to_tensor(opencv_image):
    image_float = opencv_image.astype(np.float32) / 255
    tensor = torch.from_numpy(image_float)
    tensor = tensor.unsqueeze(0)

    return tensor

def adjust_brightness(image, brightness):
    brightness_value = brightness * 0.5

    return cv2.add(image, brightness_value)

def adjust_contrast(image, contrast):
    contrast_value = 1.0 + (contrast / 100)

    return cv2.convertScaleAbs(image, alpha=contrast_value)

def adjust_saturation(image, saturation):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    saturation_value = 1.0 + (saturation / 100)
    hsv[:, :, 1] = hsv[:, :, 1] * saturation_value
    hsv[:, :, 1] = np.clip(hsv[:, :, 1], 0, 255) 

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

def adjust_shadows(image, shadows):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    shadow_mask = hsv[:, :, 2] < 128
    shadow_value = 1.0 + (shadows / 100)
    hsv[:, :, 2][shadow_mask] = hsv[:, :, 2][shadow_mask] * shadow_value
    hsv[:, :, 2] = np.clip(hsv[:, :, 2], 0, 255)

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

def process_image(image_tensor, brightness, contrast, saturation, shadows):
    opencv_image = tensor_to_opencv(image_tensor)

    opencv_image = adjust_brightness(opencv_image, brightness)
    opencv_image = adjust_contrast(opencv_image, contrast)
    opencv_image = adjust_saturation(opencv_image, saturation)
    opencv_image = adjust_shadows(opencv_image, shadows)

    tensor_image = opencv_to_tensor(opencv_image)
    return tensor_image

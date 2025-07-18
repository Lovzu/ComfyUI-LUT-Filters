
class LUTNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "brightness": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
                "saturation": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
                "shadows": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1}),
                "contrast": ("INT", {"default": 0, "min": -100, "max": 100, "step": 1})
            }
        }
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_lut"
    CATEGORY = "image/filters"
    def apply_lut(self, image, brightness, contrast, saturation, shadows):
        from .image_processing import process_image
        finally_image = process_image(image, brightness, contrast, saturation, shadows)
        return (finally_image, )
NODE_CLASS_MAPPINGS = {
    "LUTNode": LUTNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LUTNode": "LUT Filters",
}
        
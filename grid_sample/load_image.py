import nibabel as nib
import torch




def load_image(img_path, to_torch=True):
    
    

    # Load the NIfTI file
    img = nib.load(img_path)

    # Access the image data
    data = img.get_fdata()
    
    return torch.tensor(data) if to_torch else data

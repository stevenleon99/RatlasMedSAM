########################################
# Normalize the image from 0 to 1 (0 to 12000)
# Convert the nii (image & label into npz (numpy data structure))
########################################
import numpy as np
import os
import numpy as np
import nibabel as nib
import nrrd

Base = "D:/Ratlas/Rat_Atlas_2520Project"
list = "D:/Ratlas/RatlasTransUNet/list"
npz = "D:/Ratlas/RatlasTransUNet/npz"

def generateDataList():
    image_dir = {}
    label_dir = {}
    for dir in os.listdir(Base):
        subdir = os.path.join(Base, dir)
        dict_name = dir.split("_")
        separater = ''
        dict_name = separater.join(dict_name)
        if (os.path.isdir(subdir)):
            for item in os.listdir(subdir):
                type = item.split('.')[-1]
                if type == "nii":
                    image_dir[dict_name] = os.path.join(subdir, item) # use the same dict keys
                elif type == "nrrd":
                    label_dir[dict_name] = os.path.join(subdir, item)
    return image_dir, label_dir
                    
def writelist(l, name:str):
    with open(os.path.join(list, name), "w") as f:
        for i in l.values():
            f.write(i+"\n")
    f.close()

def transform2npz(image_dir, label_dir):
    assert len(image_dir) == len(label_dir), "Number of ImageDir != Number of LabelDir"
    name_list = {}
    for k in image_dir.keys(): # transform to npz
        img = np.array(nib.load(image_dir[k]).dataobj)
        # print(img.shape) # (200, 200, 160, 1) (w, h, d, c)
        label, header = nrrd.read(label_dir[k])
        if len(img.shape) == 4:
            img = img.squeeze() # (200, 200, 160) (w, h, d)
        if len(label.shape) == 4:
            label = label.squeeze() # (200, 200, 160) (w, h, d)
        assert img.shape[0:2] == label.shape[0:2], "Shape of Img != Shape of Label"
        for i in range(img.shape[-1]):
            im = img[:, :, i]
            im = normalize(im)
            la = label[:, :, i]
            name = f"case{k}_slice{i}.npz"
            name_list[f"{k}_{i}"] = name
            np.savez_compressed(os.path.join(npz, name), image=im, label=la)
    writelist(name_list, "npz.txt")



def normalize(img):
    # u_limit = 12000
    # l_limit = 0
    max = img.max()
    min = img.min()
    img = (img - min)/(max - min)
    return img
    

def readNpz():
    train_npz_dir = "/home/steve/RatlasLiteMedSAM/inference_test/test_result/preds/MR_cral"
    name = 'MR_cral_IMG8_Week10_processed.npz'
    path = os.path.join(train_npz_dir, name)
    npz_data = np.load(path)
    print(type(npz_data)) # <class 'numpy.lib.npyio.NpzFile'>
    print(npz_data.keys())
    # print(npz_data['imgs'].shape)
    # print(npz_data['gts'].shape)

    # # Create a NIfTI image from the numpy array
    # img = nib.Nifti1Image(npz_data["segs"], affine=np.eye(4))
    affine = [[ 0, 1, 0, 0],
              [-1, 0, 0, 0],
              [ 0, 0, 1, 0],
              [ 0, 0, 0, 1]]
    img = nib.Nifti1Image(npz_data["segs"].transpose(1,2,0), affine=affine) # (slice, h, w) to (h, w, slice)

    # Save the NIfTI image to a file
    nib.save(img, 'MR_cral_IMG8_Week10_processed_seg.nii')

def generateSegsNpz(npz_data):
    # change gts to segs
    if ("segs" not in npz_data.keys()):
        segs = npz_data["gts"]
    np.savez_compressed("/home/steve/RatlasLiteMedSAM/evaluation/data/segs/IMG8_week10_seg.npz", segs=segs)
    



if __name__ == "__main__":
    
    
    # image_dir, label_dir = generateDataList()
    # writelist(image_dir, "image_dir.txt")
    # writelist(label_dir, "label_dir.txt")
    # assert len(image_dir) == len(label_dir), "Number of ImageDir != Number of LabelDir"
    # transform2npz(image_dir, label_dir)
    readNpz()
    
    pass
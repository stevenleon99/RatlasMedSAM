## Workstream with litSAM

### Prepare reckless segmentation .rrd file with 3D slice
<img src="asset/img1.png" width="400" alt="3D slicer">

### Transform .rrd file to .nii
```
./addon/nrrd_2_nii.py
```

### Transform .nii of Image and reckless segmentaion into .npz
```
sh preprocessdata.sh
```

### Predict
```
sh inference.sh
```

### Tranform the image and final segmentation into .nii
```
./addon/npzConverter.py
```
> transform image because the *nib.Nifti1Image* will change the orientation, will be fixed


### Result
<img src="asset/MR_cral_IMG8_Week10_processed.png" width="400" alt="result">
>
> MR_cral_IMG8_Week10_processed.npz dsc value: 0.862131
> MR_cral_IMG8_Week10_processed.npz,dsc value: 0.8643 (two more training cases)
> MR_cral_IMG8_Week10_processed.npz,dsc value: 0.875 (earlystop)
> MR_cral_IMG8_Week10_processed.npz,dsc value: 0.863877 (dedicated mask)
> MR_cral_IMG8_Week10_processed.npz dsc value: 0.969804 (limit lower boundary to 6000)
>
### Validation
<img src="asset/img2.png" width="400" alt="validation">


### LimitLowerBoundary
<img src="asset/img4.png" width="400" alt="validation">


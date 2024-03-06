python train_one_gpu.py \
    -data_root ./data/npy \
    -pretrained_checkpoint lite_medsam.pth \
    -work_dir work_dir \
    -num_workers 1 \
    -batch_size 4 \
    -num_epochs 50
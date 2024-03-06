python inference_3D.py \
    -data_root /home/steve/RatlasLiteMedSAM/inference_test/data/npz/MedSAM_train/MR_cral \
    -pred_save_dir /home/steve/RatlasLiteMedSAM/inference_test/test_result/preds \
    -medsam_lite_checkpoint_path work_dir/medsam_lite_best_new.pth \
    -num_workers 1 \
    --save_overlay \
    -png_save_dir /home/steve/RatlasLiteMedSAM/inference_test/test_result/preds/MR_cral_overlay \
    --overwrite

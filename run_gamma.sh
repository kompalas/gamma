mkdir -p outdir/
cd ./src/GAMMA
python main.py \
	--model resnet50 \
	--fitness1 area \
	--fitness2 energy \
	--num_pop 100 \
	--epochs 50 \
	--num_pe -1 \
	--l1_size -1 \
	--l2_size -1 \
	--area_budget 10000000 \
	--pe_limit 10000 \
	--NocBW 81920000 \
	--offchipBW 1073741824 \
	--log_level 2 \
	2>&1 | tee ../../outdir/last_run.log
cd ../../







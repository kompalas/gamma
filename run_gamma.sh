#!/bin/bash
model="${1?}"

mkdir -p outdir/
cd ./src/GAMMA
python main.py \
	--model $model \
	--fitness1 energy \
	--fitness2 latency \
	--num_pop 100 \
	--epochs 200 \
	--num_pe -1 \
	--l1_size -1 \
	--l2_size -1 \
	--pe_limit 100000 \
	--area_budget 1000000 \
	--log_level 2 \
	2>&1 | tee ../../outdir/last_run.log
	#--NocBW 81920000 \
	#--offchipBW 1073741824 \
cd ../../







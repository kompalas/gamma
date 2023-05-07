#!/bin/bash

resdir=${1:-"outdir/GAMMA_resnet50_SL-2-2_F1-area_GEN-50_POP-100_Area-10000000.0_MaxPEs-10000_CostModelCstr-maestro_cstr/"}

python3 evaluation/evaluate.py \
	--resdir $resdir

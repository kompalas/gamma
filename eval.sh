#!/bin/bash

resdir=${1?}

python3 evaluation/evaluate.py \
	--resdir $resdir

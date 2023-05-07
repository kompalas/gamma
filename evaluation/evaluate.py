import pandas as pd
import argparse
import re
import os
import logging
from glob import glob


def cfg_logger(resdir, filename=None, filehandler_mode='w'):
    """Create a logging file saved in the results directory
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    stdout_formatter = logging.Formatter('%(levelname)s: %(message)s')
    ch.setFormatter(stdout_formatter)
    logger.addHandler(ch)

    fh = logging.FileHandler(filename=os.path.join(resdir, filename or f'evaluation.log'),
                             mode=filehandler_mode, encoding='utf-8',)
    fh.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s [%(name)s] (%(processName)s) %(levelname)s: %(message)s')
    fh.setFormatter(file_formatter)
    logger.addHandler(fh)

    return logger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", "--resdir", required=True, dest='resdir',
                        help="Directory of experiment results")
    args = parser.parse_args()

    if args.resdir[-1] != '/':
        args.resdir += '/'
    logger = cfg_logger(args.resdir)
    logger.info(f"Reading results from directory {args.resdir}")

    area, runtime, throughput, power, energy = 0, 0, 0, 0, 0
    resfiles = sorted(glob(args.resdir + 'result_c_layer*.csv'),
                      key=lambda resfile: int(re.search('layer(\d+)[.]', resfile).group(1)))

    for resfile in resfiles:
        df = pd.read_csv(resfile)
        layer_idx = int(re.search('layer(\d+)[.]', resfile).group(1))
        logger.debug(f"Read results for layer {layer_idx} from: {resfile}")
        for column in df.columns:
            if not isinstance(df[column].iloc[0], str) and (df[column].iloc[0] >= 100 or df[column].iloc[0] < 1):
                logger.debug(f"Name: {column} - Value: {df[column].iloc[0]:.3e}")
            else:
                logger.debug(f"Name: {column} - Value: {df[column].iloc[0]}")
        logger.info("Layer {} HW parameters: PEs={}, L1 size={:.3e}, L2 size={:.3e}".format(
                    layer_idx, df['PE'].iloc[0], df['L1_size'].iloc[0], df['L2_size'].iloc[0]))
        logger.debug("Layer {} dataflow: {}".format(layer_idx, df['best_sol'].iloc[0]))

        area += df['area'].iloc[0]
        runtime += df['runtime'].iloc[0]
        throughput += df['throughput'].iloc[0]
        power += df['power'].iloc[0]
        energy += df['energy'].iloc[0]

    logger.info("*" + "-" * 50 + "*")
    logger.info(f"Area: {area:.3e} - Runtime: {runtime:.3e} - Throughput: {throughput:.3e} - "
                f"Power: {power:.3e} - Energy: {energy:.3e}")


if __name__ == "__main__":
    main()


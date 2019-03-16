# import your packages
import yaml

import prepro

# do not rename the functions
import train


def main(dataset_path, output_path):
    """
    main entry point of training function
    :param dataset_path: path to the directory contains dataset
    :param output_path: path to a directory for outputs
    :return:
    """
    print("start running training job")
    with open("./config.yaml", 'r') as f:
        config = yaml.load(f)
    # invoke your training function
    prepro.main(dataset_path)
    train.main(output_path, config)


# to test your code locally, you can either run main.py directly
# such as "python main.py --dataset_path=<path> --output_path=<path>"
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--dataset_path',
        type=str,
        required=True,
        help='Path to the directory contains dataset')
    parser.add_argument(
        '-o',
        '--output_path',
        type=str,
        required=True,
        help='Path to a directory for outputs')
    
    FLAGS, _ = parser.parse_known_args()
    main(FLAGS.dataset_path, FLAGS.output_path)

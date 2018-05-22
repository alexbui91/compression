import argparse
from static_huffman import HuffmanCoding as StaticHuffman
import adaptive_huffman_compress as AdaptiveHuffman
import arithmetic_compress as Arithmetic


if __name__ == "__main__";
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--task", default="sh", help="specify compression type: sh, ah, ac, gc, ts")
    parser.add_argument("-b", "--binary", type=int, default=0, help="Whether input file is binary format? 0 is not")
    parser.add_argument("-i", "--input_path", help="Input file path")
    parser.add_argument("-o", "--output_name", help="Output file name")
    args = parser.parse_args()

    if args.task == "sh":
        h = StaticHuffman(args.input_path)
        _ = h.compress()
    elif args.task == "ah":
        AdaptiveHuffman.main([args.input_path, args.output_name])
    elif args.task == "ac":
        Arithmetic.main([args.input_path, args.output_name])
    elif args.task == "gc":
        
    elif args.task == "ts":
        

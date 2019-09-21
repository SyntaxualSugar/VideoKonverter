#! /usr/bin/env python
import os
import argparse
import subprocess

name = "script"


def file_dir_exists(name):
    if os.path.exists(name):
        return name
    else:
        name = "./"+name
        if os.path.exists(name):
            return name
        else:
            raise FileNotFoundError


def process_file(inarg, outarg, outtype, overwrite):
    if os.path.splitext(inarg)[1] == "."+outtype or os.path.splitext(inarg)[1] == outtype:
        return
    inarg = inarg.replace(' ', '\\ ')
    outarg = remove_extension(outarg)
    ffmpegCommand = "ffmpeg " + should_overwrite(overwrite) + " -i " + inarg + " -codec copy " + outarg + "." + outtype
    subprocess.run(ffmpegCommand.split(), stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def process_file_no_outarg(inarg, outtype, overwrite):
    process_file(inarg, inarg, outtype, overwrite)


def run(args):
    inarg = args.input
    outarg = args.output if args.output else remove_extension(args.input)
    outtype = args.outtype
    overwrite = args.overwrite
    if os.path.isdir(inarg):
        for file in os.listdir(args.input):
            filename = os.fsdecode(file)
            process_file_no_outarg(os.path.join(args.input, filename), outtype, overwrite)
    else:
        process_file(inarg, os.path.dirname(inarg) + "/" + outarg, outtype, overwrite)


def remove_extension(filename):
    return os.path.splitext(filename)[0]


def should_overwrite(overwrite):
    str = "-y" if overwrite == True else ""
    return str


def str_to_bool(potential_bool):
    if isinstance(potential_bool, bool):
        return potential_bool
    if potential_bool.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif potential_bool.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main():
    parser = argparse.ArgumentParser(description="Convert video files using ffmpeg.")
    parser.add_argument("-i", "--in", help="Input file name or directory.", dest="input", type=file_dir_exists, required=True)
    parser.add_argument("-o", "--out", help="Output file name. Ignored with multiple files.", dest="output", type=str, required=False)
    parser.add_argument("-f", "--format", help="File type to convert to.", dest="outtype", type=str, required=True)
    parser.add_argument("-v", "--overwrite", help="Overwrite existing file.", dest="overwrite", type=str_to_bool, required=False, default=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__=="__main__":
    main()
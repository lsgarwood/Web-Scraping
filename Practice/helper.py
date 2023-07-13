import argparse

parser=argparse.ArgumentParser(
    description='''''',
    epilog="""All is well that ends well.""")
parser.add_argument('--foo', type=int, default=42, help='FOO!')
parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
args=parser.parse_args()
"""log_redaction_cli

Usage:
  log_redaction_cli.py --tarfile <tarfile> --working-dir <working-dir> --output-dir <output-dir>
  log_redaction_cli.py (-h | --help)
  log_redaction_cli.py --version

Options:
  -h --help     Pass in a string: example command: python log_redaction_cli.py --tarfile "test/files/test_output.tar.gz"  --working-dir "/home/kalab/github/stringer/test/files" --output-dir  log_redataction_example
  --version     v version


"""
from docopt import docopt
import stringer.utils.log_redaction_utils as log_redact


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.9')

    perm_list = log_redact.process_gz(file=arguments.get("<tarfile>"),working_dir=arguments.get("<working-dir>"), output_gz_dir=arguments.get("<output-dir>"))

    print(str(perm_list))

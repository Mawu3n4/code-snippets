import os
import sys
import unittest2
import warnings

warnings.filterwarnings('ignore', category=UserWarning)


def main(sdk_path, test_path):
    sys.path.insert(0, sdk_path)

    import dev_appserver

    dev_appserver.fix_sys_path()
    sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
    sys.path.insert(1, os.path.join(os.path.abspath('.'), 'application'))

    suite = unittest2.loader.TestLoader().discover(test_path)
    unittest2.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    try:
        # Path to google app engine SDK
        SDK_PATH = sys.argv[1]
        # Path to tests folder
        TEST_PATH = os.path.join(
            os.path.dirname(os.path.abspath(__name__)),'tests'
        )

        main(SDK_PATH, TEST_PATH)
    except IndexError:
        print("Please specify path to GAE SDK")

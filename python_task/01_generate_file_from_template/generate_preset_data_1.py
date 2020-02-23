import sys
import generate_file_from_template


def main():
    generate_file_from_template.generate('PresetData1', 'PresetData1', 'list', 'template')


if __name__ == '__main__':
    sys.exit(main())


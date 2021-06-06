# folderstack :card_file_box: :partying_face:

Generate directory structure documentation in Markdown.

## Example

`folderstack` is a simple way to generate Markdown documentation of a repository's file structure.

```
├── README.md                                     # Project README document
├── folderstack.py                                # folderstack source code
└── setup.py                                      # Python package installation instructions
```

## Installation

Install `folderstack` from GitHub:

```{shell}
pip install git+https://github.com/hamishgibbs/folderstack.git@main
```

## Quickstart

Use `folderstack` from the command line as a final documentation step when preparing a repository for release.

Enter the repository you want to document:

```{shell}
cd ~/cool/project
```

Run `folderstack` to output Markdown documentation for your project.

```{shell}
folderstack
```

`folderstack` will output documentation in a `folderstack.md` file. Migrate the contents of this file into your documentation as needed.

## Options

*--outfile*

Output file destination, default: "./folderstack.md".

*--docspace*

Spacing for custom documentation (the number of space characters), default: 50.

## Developers

`folderstack` is a tiny library to make it easier to generate project documentation. Some custom documentation is still required (say what each file does). Contributions are welcome.

See a problem with the library? Please [open an issue](https://github.com/hamishgibbs/folderstack/issues/new).

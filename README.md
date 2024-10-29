# File Utils

`file_utils.py` is a simple Python module providing basic file-handling functions. This tool helps in reading, writing, appending, and managing files with ease. It can be extended or modified for additional file management utilities.

## Features

- **Read File**: Reads and returns the contents of a specified file.
- **Write to File**: Writes (and overwrites) specified content to a file.
- **Append to File**: Appends content to the end of a file.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/file-utils.git
    ```

2. Navigate to the project directory:

    ```bash
    cd file-utils
    ```

3. Import `file_utils` in your Python scripts:

    ```python
    from file_utils import read_file, write_to_file, append_to_file
    ```

## Usage

### 1. Reading a File

```python
content = read_file("example.txt")
print(content)

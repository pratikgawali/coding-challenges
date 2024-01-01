# The Challenge - Building wc
This challenge is to build your own version of the Unix command line tool `wc`!

The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

- Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
- Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.

Following these philosophies has made the simple unix command line tools some of the most widely used software engineering tools - allowing us to create very complex text data processing pipelines from simple command line tools.


# Implement the word count script
Implemented the word count script in python as `ccwc.py` with following functionalities:
1. Count bytes `-c`
2. Count lines `-l`
3. Count words `-w`
4. Count characters `-m`

Refer `ccwc.py` to understand the implementation of each.

# Make it a command line utility
Once the word count script is implemented in `ccwc.py`, we must add it as a native command line utility by undertaking the following steps:

### 1. Add Shebang line
Add the following shebang `#!` line at the beginning of the script to indicate macOS to use python interpreter while executing the script.
```python
#!/usr/bin/env python3 
```  

### 2. Make the script executable:
Make the python script executable by running the following command:
```sh
chmod +x ccwc.py
```

### 3. Create a symbolic link (symlink):
Create a symbolic link (symlink) to the python script ty running the following command. This allows the script to be accessible from `/usr/local/bin` location.
```sh
sudo ln ccwc.py /usr/local/bin/ccwc
```

### 4. Run the newly created command line utility:
Run the following command to test the newly created command line utility:
```sh
ccwc -wlcm test.txt
```

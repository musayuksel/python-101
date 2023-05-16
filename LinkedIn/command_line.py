from argparse import ArgumentParser  #ArgumentParser class 

parser = ArgumentParser(description="In the -h section, you can add a description of the program") 
parser.add_argument('--output','-o', help='Some helper explanation about this command', required=True)
#  python3 command_line.py -h
    ## usage: command_line.py [-h] --output OUTPUT
    ## In the -h section, you can add a description of the program
    ## options:
    ##   -h, --help       show this help message and exit
    ##   --output OUTPUT  Some helper explanation


parser.add_argument('--text', '-t', required=True, help='The text to write to the file')


args = parser.parse_args() # parse_args() method returns a Namespace object

with open(args.output, 'w') as f:
    f.write(args.text+'\n')


# python3 command_line.py -o test.txt -t "This is a test"
print(f'Wrote "{args.text}" to file "{args.output}"')   
print(args.output) # output is an attribute of the Namespace object, same name as the argument


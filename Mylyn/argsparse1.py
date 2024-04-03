import  argparse  

def main():
    parser = argparse.ArgumentParser(description ="A simple command line application" )
    parser.add_argument('filename',help='The name of the file to precess')
    parser.add_argument('--verbose','-v',action ='store_true',help='Print verbose output')
    parser.add_argument('--output','-o',help="Output file path")
    args = parser.parse_args()
    
    if args.verbose:
        print("Verbose is activated!")
    if args.output:
        print("Output file specified:",args.output)
    print("Porcessing file",args.filename)

if __name__ =='__main__':
    main()
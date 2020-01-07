from add_rm_startup import *

def main():

    ch = raw_input("Embedded the file or remove:[E|R]")

    if(ch == 'E'):
        
        a = Start()
        a.add_to_startup()
    
    elif(ch == 'R'):
        
        rm_strt()
        
    else:

        pass
    
if __name__ == "__main__":
    
    main()

    

    

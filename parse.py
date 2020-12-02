
# Python3 program to check if a string 
# contains any special character 
  
# import required package 
import re 
  
# Function checks if the string 
# contains any special character 
def run(string): 
  
    # Make own character set and pass  
    # this as argument in compile method 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
    if(regex.search(string) == None): 
        print(type(regex.search(string))) 
          
    else: 
        info = regex.search(string)
        print(type(info)) 
      
  
# Driver Code 
if __name__ == '__main__' : 
      
    # Enter the string 
    string = "Geeks$For$Geeks"
      
    # calling run function  
    run(string) 
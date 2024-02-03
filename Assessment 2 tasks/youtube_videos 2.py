# TODO: Define the YouTubeVideo class here.

class YouTubeVideo: # Create the class for the class.
    def __init__(self, title, url): # initalize the class with the title and url fields.
        self.title = title # set the title to the title field for the class.
        self.url = url # set the url to the url field for the class.
        
    def print_details(self): # create the function to print the details of the class.
        output_string = (self.title + ' ' + '('  + self.url + ')')     # Add a space and opening parenthesis to the output string
        print(output_string) # print the output to the console.

video1 = YouTubeVideo('THANTS', 'https://www.youtube.com/watch?v=9jtU9BbReQk') # input for the example provided
video2 = YouTubeVideo('Skydiving!', 'https://www.youtube.com/watch?v=NXCjZESUeFg') # input for the example provided

video1.print_details() # this will print the example value to the console.
video2.print_details() # this will print the example value to the console.

input_title = input("What is the Title of your Youtube video: ") # get the users input for the title
input_url = input("what video do you want to do next, URL ") # get the users input for the url 

video3 = YouTubeVideo(input_title, input_url) # with the class call the 'YoutubeVideo' function with the user input for the title and url.

video3.print_details() # print the users output to the console
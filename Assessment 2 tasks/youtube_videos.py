class YouTubeVideo: # Create the class for the class.
    def __init__(self, title, url): # initalize the class with the title and url fields.
        self.title = title # set the title to the title field for the class
        self.url = url # set the url to the url field for the class
        
    def print_details(self): # create the function to print the details of the class.
        output_string = self.title + ' ' + self.url     # Add a space and opening parenthesis to the output string
        print(output_string) # print the output to the console.

# Test instances
video1 = YouTubeVideo("THANTS", "https://www.youtube.com/watch?v=9jtU9BbReQk")
video2 = YouTubeVideo("Skydiving!", "https://www.youtube.com/watch?v=NXcjZJESUeFg")

# Test the output of print_details method for both instances
video1.print_details()
video2.print_details()
video3 = input("what video do you want to do next")

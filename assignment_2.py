from sys import exit as abort
from urllib.request import urlopen
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar
from re import *
from webbrowser import open as urldisplay
from sqlite3 import *

def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        print("\nCannot find requested document '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print("\nAccess denied to document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except URLError as message: # probably the wrong server address
        print("\nCannot access web server at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except Exception as message: # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              "the document at URL '" + str(url) + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters")
        print("Error message was:", message, "\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("\nUnable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents


# Create the main window
from tkinter.font import Font
from tkinter import ttk
from html.parser import HTMLParser
import urllib.request
import codecs


#html links
IMDB_TV_Content = 'https://www.imdb.com/chart/tvmeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=VE6M00452G2A9PQ9J6EK&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_5'
IMDB_Movies_Content ='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
Aria_Content ="https://www.aria.com.au/charts/singles-chart/2023-05-15"

#sets the filenames of webpages downloaded
IMDB_TV_Save = "TV.html"
IMDB_Movies_Save = "Movies.html"
Aria_Save = "Aria.html"


#functions for opening the webpage and displaying in the status box
def open_IMDB_TV():
    Status_info.config(text="Showing TV show details in your browswer")
    urldisplay('https://www.imdb.com/chart/tvmeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=VE6M00452G2A9PQ9J6EK&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_5')

def open_IMDB_Movies():
    Status_info.config(text="Showing movie details in your browswer")
    urldisplay("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")  


def open_Aria():
    Status_info.config(text="Showing song details in your browswer")
    urldisplay("https://www.aria.com.au/charts/singles-chart/2023-05-15")

#downloads and saves the html files
urllib.request.urlretrieve(IMDB_TV_Content,filename = IMDB_TV_Save)
urllib.request.urlretrieve(IMDB_Movies_Content,filename = IMDB_Movies_Save)
urllib.request.urlretrieve(Aria_Content,filename = Aria_Save)

#opens the files and sets the format    
file = codecs.open("TV.html",'r',"utf-8") 
file2 = codecs.open("Movies.html",'r',"utf-8") 
file3 = codecs.open("Aria.html",'r','utf-8')

#reads the downloaded html files
content = file.readlines()
content2 = file2.readlines()
content3 = file3.readlines()

#variables set to read the files
tv = file.read()
movies = file2.read()
music = file3.read()


#function for finding specific line and removing the empty spaces
def find_line(file_path, target_line, offset):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if target_line in line:
                desired_line = lines[i + offset]
                return desired_line.strip()  

    return None  # Line not found

#asigns the html save files to variables
Movie_file = 'Movies.html'
TV_file = "TV.html"
Music_file = "Aria.html"

#sets the target lines to search for
target_line = '<div class="velocity">1'
target_line2 = '<div class="c-chart-item__details">'

#sets the lines before or after the called upon line
offset1 = -2  
offset2 = -1
offset3 = 5
offset4 = 7
offset5 = 2
offset6 = 5

#finds the lines based on the div tags and reads the text values before and after that line
Movie_title = find_line(Movie_file, target_line, offset1)
Year_produced_Movie_Value = find_line(Movie_file, target_line, offset2)
Movie_rating_Value = find_line(Movie_file, target_line, offset3)

TV_Title = find_line(TV_file, target_line, offset1)
Year_produced_TV_Value = find_line(TV_file, target_line, offset2)
TV_rating_Value = find_line(TV_file, target_line, offset4)

Music_Title = find_line(Music_file, target_line2, offset5)
Artist_name_Music_Value = find_line(Music_file, target_line2, offset6)
  
#removes the html tags from extracted text
def remove_html_tags(line):
    
    tags_to_remove = ['<strong>', '<em>', '<a href=".*?">', '</strong>', '</em>', '</a>','<.*?>']
    html_tags_pattern = '|'.join(map(escape, tags_to_remove))
    html_tags_pattern = compile(r'<.*?>')
    # Remove HTML tags using the pattern
    line_without_tags = sub(html_tags_pattern, '', line)
    return line_without_tags

def print_html_after_greater_than(html):
    greater_than_index = html.find(">")
    # Check if ">" exists in the HTML string
    if greater_than_index != -1:
        # Extract the substring starting from after the ">" character and print it
        html_to_print = html[greater_than_index + 1:]
        result = html_to_print.replace("</a>", "")
        return result 

#removes the html tags and clears the text up
Produced1 = remove_html_tags(Year_produced_TV_Value)
Rating1 = remove_html_tags(TV_rating_Value)
TV_Title_proper = print_html_after_greater_than(TV_Title)

Produced2 = remove_html_tags(Year_produced_Movie_Value)
Rating2 = remove_html_tags(Movie_rating_Value)
Movie_Title_proper = print_html_after_greater_than(Movie_title)

Artist_name = remove_html_tags(Artist_name_Music_Value)
Music_Title_proper = remove_html_tags(Music_Title)

#removes large spacing between text on lines
def remove_spacing(text):
    return text.replace(" ", "")

#creates the tkinter window and configures the resolution, application name and backgroud colour
task_2_main_window = Tk()
task_2_main_window.title("Liam's Media Reviews")
task_2_main_window.geometry("950x450")
task_2_main_window.configure(bg="mistyrose")

#creates image frame and imports the image to certain width and height
frame = Frame(task_2_main_window, width = 300, height = 200)
frame.pack()
frame.configure(bg = "mistyrose")
frame.grid(row = 0, column = 0, sticky = W)
img = PhotoImage(file = "22.png")

#creates the borderwidth and sets the grid orientation of the frame
l = Label(frame,image = img, background="black",borderwidth=2)
l.grid(row = 1, column = 0, sticky = N, padx=20)

#creates 3 different fonts to use
header_font = Font(
    family = 'Times',
    size = 15,
    weight = 'bold',
    slant = 'roman',
    
)

Sub_header_font = Font(
    family = 'Times',
    size = 12,
    weight = 'bold',
    slant = 'roman',
)

Body_Font = Font(
    family = 'Times',
    size = 11,
    weight = 'bold',
    slant = 'roman',
)
#Creates the title at the bottom left of the window with the specified fonts and colouring
text = Label(text="Liam's Media Reviews",fg = "mediumblue", font = header_font,background="#F09216",highlightthickness=2, highlightbackground="black", width = 33, height = 3, justify = "center")
text.grid(row = 1, column = 0, sticky = N, padx=20)

#creates the media options labelframe, configures the colours and sets it to grid orientation
Media_options = LabelFrame(task_2_main_window, font = Sub_header_font, text="Media Options", padx=50, pady=29)
Media_options.configure(bg = "#E74A55", highlightthickness= 2, highlightbackground= "black")
Media_options.grid(row = 0, column = 1, sticky = N, pady = 34,padx=10)

#creates a combobox with the different media values and configures it to a certain width and orientation in grid
Dropdown_media = ttk.Combobox(Media_options, values = ['Movies - Most Popular', 'TV Shows - Most Popular', 'Music - ARIA Top 50 Singles'])
Dropdown_media.config(width = 25)
Dropdown_media.grid(row = 1, column = 0, sticky = N)

#creates the buttons and rating combobox, along with the combobox titles
Summary = Button(Media_options, text = "Show summary")
Details = Button(Media_options, text = "Show details")
Ratings = ttk.Combobox(Media_options, values = ["1","2","3","4","5"])
Rating_label = Label(Media_options, text = "Rating", font = Sub_header_font ,bg = "#E74A55")
Rating_save = Button(Media_options, text = "Save review", padx = 5)
Media_type = Label(Media_options, text = "Media Type", font = Sub_header_font ,bg = "#E74A55")

#creates the status labelframe that shows what is selected and shows the media summary
Status = LabelFrame(task_2_main_window, font = Sub_header_font, padx = 10, pady = 10)
Status.grid(row = 1, column = 1, sticky = N)
Status.configure(bg = "#E74A55", highlightthickness= 2, highlightbackground= "black")

#automatically sets the text to say that nothing is selected and orientate it into the grid
Status_info = Label(Status, text = "Nothing currently selected" )
Status_info.grid(row = 0, column = 0, sticky = N)
Status_info.config(font = Body_Font ,bg = "#E74A55")

#connects to the database
database_connect = connect('media_reviews.db')
cursor = database_connect.cursor()

#lists the desired output of the table and creates it if required
create_table_query = '''
CREATE TABLE IF NOT EXISTS Reviews (
	"Media Type"	TEXT NOT NULL,
	"Details"	TEXT NOT NULL,
    "URL" TEXT NOT NULL,
	"Rating"	INTEGER NOT NULL  

)
'''
cursor.execute(create_table_query)

#removes the spacing between the tags and beginning of the text for the tv html file
spacing_removal_TV1 = remove_spacing(Produced1)

#function for showing the summary of the read tv file
def reading_TV():

    
    spacing_removal2 = remove_spacing(Rating1)
    
    trending_show = (("The most popular show is '" + str (TV_Title_proper)) + "',"  "\n" + " released in '" + str(spacing_removal_TV1) + "'," + " with a rating of '" + str(spacing_removal2) + "'")
    Status_info.config(text=trending_show)

spacing_removal_movie1 = remove_spacing(Produced2)


#function for showing the summary of the read movies file
def reading_movies():
    
    spacing_removal2 = remove_spacing(Rating2)
    
    trending_movie = (("The most popular movie is '" + str (Movie_Title_proper)) + "'," + "\n" + " released in '" + str(spacing_removal_movie1) + "'," + " with a rating of '" + str(spacing_removal2) + "'")
    Status_info.config(text=trending_movie)

#removes the spacing of the line
spacing_removal_music1 = remove_spacing(Music_Title_proper) 
spacing_removal_music1 = Music_Title_proper.lstrip() 
spacing_removal_music2 = remove_spacing(Artist_name)  
spacing_removal_music2 = Artist_name.lstrip()

#function for showing the summary of the read music file
def reading_music():
    trending_music = (("The most popular song is '" + str (spacing_removal_music1)) + "'" +  " by '" + str(spacing_removal_music2) + "'")
    Status_info.config(text=trending_music)

#details the database uses for music
Music_details = ((str (spacing_removal_music1)) +  " by " + str(spacing_removal_music2))

#generic form for inserting a query    
insert_query = '''
INSERT INTO Reviews ("Media Type", "Details", "Rating", "URL") VALUES (?, ?, ?,?)
'''

#details for movies for database to use
Movie_details = str (Movie_Title_proper) + ", released in " + str (spacing_removal_movie1) 

#details for tv shows for database to use
TV_details = str (TV_Title_proper) + ", released in " + str (spacing_removal_TV1)

#function for updating the buttons and status text box when a new combobox value is selected
def update_details(*args):
    if Dropdown_media.get() == "Movies - Most Popular":
        values = ("Movie", Movie_details,(Ratings.get()), IMDB_Movies_Content)
        #function for executing the insert query
        def Movies_review():
            database_connect = connect('media_reviews.db')
            cursor = database_connect.cursor()
            Rating_save.config(command = cursor.execute(insert_query, values))
            database_connect.commit()
            cursor.close()
            database_connect.close()


        #sets the buttons commands to the defined functions
        Details.config(command = open_IMDB_Movies)
        Summary.config(command = reading_movies)
        Status_info.config(text="Movies - Most Popular is currently selected")


    elif Dropdown_media.get() == "TV Shows - Most Popular":
        values = ("TV Show", TV_details,(Ratings.get()), IMDB_TV_Content)
        def TV_review():
            database_connect = connect('media_reviews.db')
            cursor = database_connect.cursor()
            Rating_save.config(command = cursor.execute(insert_query, values))
            database_connect.commit()
            cursor.close()
            database_connect.close()


        Details.config(command = open_IMDB_TV)
        Summary.config(command = reading_TV)
        Status_info.config(text="TV Shows - Most Popular is currently selected")





    elif Dropdown_media.get() == "Music - ARIA Top 50 Singles":
        values = ("Music", Music_details,(Ratings.get()), Aria_Content)
        def music_review():
            database_connect = connect('media_reviews.db')
            cursor = database_connect.cursor()
            Rating_save.config(command = cursor.execute(insert_query, values))
            database_connect.commit()
            cursor.close()
            database_connect.close()

        Details.config(command = open_Aria)
        Summary.config(command = reading_music)
        Status_info.config(text="Music - ARIA Top 50 Singles is currently selected")
    
      
#function for updating the rating value, as the original update function would cause an issue where it would create a new rating query every time a new combobox was selected
def update_details2(*args):
    if Dropdown_media.get() == "Movies - Most Popular":
        values = ("Movies", Movie_details,(Ratings.get()), IMDB_Movies_Content)

        def Movies_review():
            database_connect = connect('media_reviews.db')
            cursor = database_connect.cursor()
            Rating_save.config(command = cursor.execute(insert_query, values))
            database_connect.commit()
            cursor.close()
            database_connect.close()
        Rating_save.config(command= Movies_review)

    elif Dropdown_media.get() == "TV Shows - Most Popular":
        values = ("TV Shows", TV_details,(Ratings.get()), IMDB_TV_Content)
        def TV_review():
            database_connect = connect('media_reviews.db')
            cursor = database_connect.cursor()
            Rating_save.config(command = cursor.execute(insert_query, values))
            database_connect.commit()
            cursor.close()
            database_connect.close()
        Rating_save.config(command= TV_review)

    elif Dropdown_media.get() == "Music - ARIA Top 50 Singles":
        values = ("Music", Music_details,(Ratings.get()), Aria_Content)
        def music_review():
            database_connect = connect('media_reviews.db')
            cursor = database_connect.cursor()
            Rating_save.config(command = cursor.execute(insert_query, values))
            database_connect.commit()
            cursor.close()
            database_connect.close()

        Rating_save.config(command= music_review)
    
#crteates the grid for the rest of the media options box with the desired text padding
Media_type.grid(row = 0, column = 0, sticky = W, pady = 12)
Summary.grid(row = 0, column = 1, sticky = N, padx = 29)
Details.grid(row = 2, column = 1, sticky = N)
Rating_label.grid(row = 3, column = 0, sticky = W)
Rating_save.grid(row = 4, column = 0, sticky = E)


Ratings.grid(row = 4, column = 0, sticky = W)
Rating_save.config(width = 8)
Ratings.config(width = 8)

#updates all the button and combobox values when a new value is selected in either the dropdown media or ratings combobox
Dropdown_media.bind("<<ComboboxSelected>>", update_details)
Ratings.bind("<<ComboboxSelected>>", update_details2)

#closes the database when finished with the program
database_connect.commit()
cursor.close()
database_connect.close()

# Start the event loop to detect user inputs
task_2_main_window.mainloop()


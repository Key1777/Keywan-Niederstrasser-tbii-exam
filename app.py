import tkinter as tk
import pygame as pg


# create the GUI
root = tk.Tk()

root.title("Hamburg Football Buddy ⚽")

screen_width = 600
screen_height = 400

root.minsize(screen_width, screen_height)  # width, height


def clear_widgets():
    """This function will destroy any widgets you created"""
    for i in root.winfo_children():
        i.destroy()


def homepage():
    """This function carries out the steps for the new user page"""

    # call the definition that clears all the widgets
    clear_widgets()

    # create a welcome label
    welcome_label = tk.Label(root,
                               text="WELCOME ⚽🔥",
                               font=("Gill Sans MS", 28, "bold"))
    welcome_label.pack(side=tk.TOP, anchor=tk.CENTER)

    welcome1_label = tk.Label(root,
                               text="Choose below and have fun :)",
                               font=("Gill Sans MS", 20, "bold"))
    welcome1_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # Create the "homepage" button with clear visibility settings
    homepage = tk.Button(root,
                         text="Game 🎮",
                         command=game,
                         bg="lightblue",  # Set distinct background color
                         fg="black",  # Set contrasting foreground color
                         width=15, height=1  # Set appropriate size
                         )
    homepage.pack(side=tk.BOTTOM, pady=10)  # Add padding for spacing

    homepage2 = tk.Button(root,
                          text="Pitches ⚽",
                          command=pitches,
                          bg="lightblue",  # Set distinct background color
                          fg="black",  # Set contrasting foreground color
                          width=15, height=1  # Set appropriate size
                          )
    homepage2.pack(side=tk.BOTTOM, pady=10)  # Add padding for spacing

    homepage3 = tk.Button(root,
                          text="Biggest Clubs 🔷☠️",
                          command=clubs,
                          bg="lightblue",  # Set distinct background color
                          fg="black",  # Set contrasting foreground color
                          width=15, height=1  # Set appropriate size
                          )
    homepage3.pack(side=tk.BOTTOM, pady=10)  # Add padding for spacing


def pitches():
    """This function carries out the steps for the new user page"""

    # call the definition that clears all the widgets
    clear_widgets()

    # create a welcome label
    pitch1_label = tk.Label(root,
                              text="BEST LOCAL PITCHES ⚽",
                              font=("Gill Sans MS", 28, "bold"))
    pitch1_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # create a welcome label
    pitch2_label = tk.Label(root,
                              text="1️⃣ Adress: Laeiszstraße, 20357 Hamburg | Description: Tartan Ground in a cool neighborhood | Rating: ⭐⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch2_label.place(x=0, y=70)

    pitch3_label = tk.Label(root,
                              text="2️⃣ Adress: Rutschbahn, 20146 Hamburg | Description: Iconic Ground with a tree in the middle | Rating: ⭐⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch3_label.place(x=0, y=100)

    pitch4_label = tk.Label(root,
                              text="3️⃣ Adress: Kellinghusenstraße, 20249 Hamburg | Description: Completely new & very clean | Rating: ⭐⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch4_label.place(x=0, y=130)

    pitch5_label = tk.Label(root,
                              text="4️⃣ Adress: Fischers Park, 22763 Hamburg | Description: Green Tartan & always busy | Rating: ⭐⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch5_label.place(x=0, y=160)

    pitch6_label = tk.Label(root,
                              text="5️⃣ Adress: Brunnenhofstraße, 22767 Hamburg | Description: Cage Football Ground  | Rating: ⭐⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch6_label.place(x=0, y=190)

    pitch7_label = tk.Label(root,
                              text="6️⃣ Adress: Silbersackstraße, 20359 Hamburg | Description: In the Heart of St.Pauli | Rating: ⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch7_label.place(x=0, y=220)

    pitch8_label = tk.Label(root,
                              text="7️⃣ Adress: Sternschanze, 20357 Hamburg | Description: Real Grass & huge pitch | Rating: ⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch8_label.place(x=0, y=250)

    pitch9_label = tk.Label(root,
                              text="8️⃣ Adress: Am Inselpark, 21109 Hamburg | Description: In the midst of a big park | Rating: ⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch9_label.place(x=0, y=280)

    pitch10_label = tk.Label(root,
                              text="9️⃣ Adress: Festland, 22767 Hamburg | Description: Artificial Grass & renovated | Rating: ⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch10_label.place(x=0, y=310)

    pitch11_label = tk.Label(root,
                              text="🔟 Adress: Kieler Straße, 22525 Hamburg | Description: Street Football feeling | Rating: ⭐⭐⭐⭐",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    pitch11_label.place(x=0, y=340)

    # button
    pitches_button = tk.Button(root,
                                    text="🏠",
                                    font=("Comic Sans MS", 14, "bold"),
                                    command=homepage
                                    )
    pitches_button.pack(side=tk.BOTTOM, pady=10)


def clubs():
    """This function carries out the steps for the new user page"""

    # call the definition that clears all the widgets
    clear_widgets()

    # create a welcome label
    club1_label = tk.Label(root,
                              text="BIGGEST CLUBS 🔷☠️",
                              font=("Gill Sans MS", 28, "bold"))
    club1_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # create a welcome label
    club2_label = tk.Label(root,
                              text="Are you Team HSV OR Team St.Pauli? 👀",
                              font=("Gill Sans MS", 28, "bold"))
    club2_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # create button for next page
    hsv = tk.Button(root,
                         text="TEAM HSV 🔷",
                         command=hsvgame,
                         bg="white",  # Set distinct background color
                         fg="blue",  # Set contrasting foreground color
                         width=15, height=1  # Set appropriate size
                         )

    hsv.pack(side=tk.BOTTOM, pady=10)  # Add padding for spacing

    stpauli = tk.Button(root,
                    text="TEAM ST.PAULI ☠️",
                    command=stpauligame,
                    bg="white",  # Set distinct background color
                    fg="brown",  # Set contrasting foreground color
                    width=15, height=1  # Set appropriate size
                    )

    stpauli.pack(side=tk.BOTTOM, pady=10)  # Add padding for spacing


    club5_label = tk.Label(root,
                              text="Founding Year ⏳:",
                              font="Arial 12 bold",
                              fg="white",
                              bg="brown"
                              )
    club5_label.place(x=0, y=120)

    club5a_label = tk.Label(root,
                               text="HSV: 1887 | St.Pauli: 1910",
                               font="Arial 10 bold",
                               fg="black",
                               bg="white"
                               )
    club5a_label.place(x=120, y=120)



    club6_label = tk.Label(root,
                              text="Trophies 🏆:",
                              font="Arial 12 bold",
                              fg="white",
                              bg="blue"
                              )
    club6_label.place(x=0, y=150)

    club6a_label = tk.Label(root,
                               text="HSV: 20 | St.Pauli: 9",
                               font="Arial 10 bold",
                               fg="black",
                               bg="white"
                               )
    club6a_label.place(x=120, y=150)

    club7_label = tk.Label(root,
                              text="Actual Division 🇩🇪:",
                              font="Arial 12 bold",
                              fg="white",
                              bg="brown"
                              )
    club7_label.place(x=0, y=180)

    club7a_label = tk.Label(root,
                               text="HSV: second (2. Bundesliga) | St.Pauli: second (2. Bundesliga)",
                               font="Arial 10 bold",
                               fg="black",
                               bg="white"
                               )
    club7a_label.place(x=120, y=180)

    club8_label = tk.Label(root,
                              text="Stadium 🏟:",
                              font="Arial 12 bold",
                              fg="white",
                              bg="blue"
                              )
    club8_label.place(x=0, y=210)

    club8a_label = tk.Label(root,
                               text="HSV: Volksparkstadion, Capacity: 57.000 | St.Pauli: Millerntor, Capacity: 29.546",
                               font="Arial 10 bold",
                               fg="black",
                               bg="white"
                               )
    club8a_label.place(x=120, y=210)

    club9_label = tk.Label(root,
                              text="Club Members 🎉:",
                              font="Arial 12 bold",
                              fg="white",
                              bg="brown"
                              )
    club9_label.place(x=0, y=240)

    club9a_label = tk.Label(root,
                              text="HSV: 100.000 | St.Pauli: 30.000",
                              font="Arial 10 bold",
                              fg="black",
                              bg="white"
                              )
    club9a_label.place(x=120, y=240)

    club10_label = tk.Label(root,
                              text="Unique 💎:",
                              font="Arial 12 bold",
                              fg="white",
                              bg="blue"
                              )
    club10_label.place(x=0, y=270)

    club10a_label = tk.Label(root,
                               text="HSV: Long Tradition & great History. | St.Pauli: Iconic & Millerntor Stadium in the heart of the city.",
                               font="Arial 10 bold",
                               fg="black",
                               bg="white"
                               )
    club10a_label.place(x=120, y=270)

def stpauligame():
    # initialise the library
    pg.init()

    # create some variables with colour and sizes
    size = width, height = 600, 400
    colour = 0, 0, 0
    speed = [2, 2]

    # creating the display screen
    screen = pg.display.set_mode(size)
    # set the caption
    pg.display.set_caption("ST.PAULI FOREVER 🎉")


    # going back to homepage button
    stpauligame_button = tk.Button(root,
                                   text="🏠",
                                   font=("Gill Sans MS", 14, "bold"),
                                   command=homepage
                                   )
    stpauligame_button.pack(side=tk.TOP, pady=10)

    # place the image on our display
    background = pg.image.load("images/stpauli_background.png")
    ball = pg.image.load("images/stpauli.gif")

    # convert this image into a rectangular object
    ballrect = ball.get_rect()

    # goalkeeper  variable

    # load some music
    pg.mixer.music.load("music/stpauli_song.mp3")
    pg.mixer.music.play(-1)

    while True:
        for event in pg.event.get():
            # close the game if someone clicks on the exit button
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # move my ballrect
        ballrect = ballrect.move(speed)

        # if else statement to reverse the speed coordinates when it reaches the boundaries
        # we will break this out in the snake game, reference for the code:
        # Reference: https://www.pygame.org/docs/tut/PygameIntro.html
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # code to run my game
        screen.fill(colour)  # changes the background colour
        screen.blit(background, (0, 0))
        screen.blit(ball, ballrect)  # place the image on the display
        pg.display.update()

def hsvgame():
    # initialise the library
    pg.init()

    # create some variables with colour and sizes
    size = width, height = 600, 400
    colour = 0, 0, 0
    speed = [2, 2]

    # creating the display screen
    screen = pg.display.set_mode(size)
    # set the caption
    pg.display.set_caption("HSV FOREVER 🎉")

    # place the image on our display
    background = pg.image.load("images/hsv_background.png")
    ball = pg.image.load("images/hsv.gif")

    # convert this image into a rectangular object
    ballrect = ball.get_rect()

    # goalkeeper  variable

    # load some music
    pg.mixer.music.load("music/hsv_song.mp3")
    pg.mixer.music.play(-1)

    while True:
        for event in pg.event.get():
            # close the game if someone clicks on the exit button
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # move my ballrect
        ballrect = ballrect.move(speed)

        # if else statement to reverse the speed coordinates when it reaches the boundaries
        # we will break this out in the snake game, reference for the code:
        # Reference: https://www.pygame.org/docs/tut/PygameIntro.html
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # code to run my game
        screen.fill(colour)  # changes the background colour
        screen.blit(background, (0, 0))
        screen.blit(ball, ballrect)  # place the image on the display
        pg.display.update()

def game():
    # initialise the library
    pg.init()

    # create some variables with colour and sizes
    size = width, height = 600, 400
    colour = 0, 0, 0
    speed = [2, 2]

    # creating the display screen
    screen = pg.display.set_mode(size)
    # set the caption
    pg.display.set_caption("BE THE GOALIE")

    # place the image on our display
    background = pg.image.load("images/stadium.png")
    goalie = pg.image.load("images/goalie.png")
    ball = pg.image.load("images/intro_ball.gif")

    # convert this image into a rectangular object
    ballrect = ball.get_rect()

    # goalkeeper  variable

    # load some music
    pg.mixer.music.load("music/test.mp3")
    pg.mixer.music.play(-1)

    while True:
        for event in pg.event.get():
            # close the game if someone clicks on the exit button
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # move my ballrect
        ballrect = ballrect.move(speed)



        # if else statement to reverse the speed coordinates when it reaches the boundaries
        # we will break this out in the snake game, reference for the code:
        # Reference: https://www.pygame.org/docs/tut/PygameIntro.html
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # code to run my game
        screen.fill(colour)  # changes the background colour
        screen.blit(background, (0, 0))
        screen.blit(goalie, (30, 30))
        screen.blit(ball, ballrect)  # place the image on the display
        pg.display.update()
def create_homepage():
    """This function creates the homepage"""

    # clear widgets in the case widgets have been created
    clear_widgets()

    # create the home page background

    # add a welcome label
    welcome_label = tk.Label(root,
                             text="Do you Love Football?",
                             font="Arial 20 bold",
                             fg="white",
                             bg="red"
                             )
    welcome_label.place(x=180, y=100)


    # add two buttons new and returning user
    # on activation these buttons should destroy all the widgets and carry out the steps for the page
    gotohomepage_button = tk.Button(root,
                                    text="YESSSS 🔥",
                                    font=("Gill Sans MS", 14, "bold"),
                                    command=homepage
                                    )
    gotohomepage_button.pack(side=tk.BOTTOM, pady=10)


# call my homepage definition to create the home page when launching the gui
create_homepage()

# launch the gui
root.mainloop()
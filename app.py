import tkinter as tk
import pygame as pg
import random

# create the GUI
root = tk.Tk()

root.title("Hamburg Football Buddy ⚽")

# defining the size of the frame
screen_width = 600
screen_height = 400

# adjusting the screen
root.minsize(screen_width, screen_height)

# This function will destroy any widgets created
def clear_widgets():
    for i in root.winfo_children():
        i.destroy()

# This function carries out the steps for the homepage
def homepage():


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
                         bg="lightblue",  # distinct background color
                         fg="black",  # contrasting foreground color
                         width=15, height=1  # Setting appropriate size
                         )
    homepage.pack(side=tk.BOTTOM, pady=10)  # Adding padding for spacing

    homepage2 = tk.Button(root,
                          text="Local Pitches ⚽",
                          command=pitches,
                          bg="lightblue",  # distinct background color
                          fg="black",  # contrasting foreground color
                          width=15, height=1  # Setting appropriate size
                          )
    homepage2.pack(side=tk.BOTTOM, pady=10)  # Adding padding for spacing

    homepage3 = tk.Button(root,
                          text="Biggest Clubs 🔷☠️",
                          command=clubs,
                          bg="lightblue",  # distinct background color
                          fg="black",  # contrasting foreground color
                          width=15, height=1  # Setting appropriate size
                          )
    homepage3.pack(side=tk.BOTTOM, pady=10)  # Adding padding for spacing

# This function carries out the steps for the pitches page"""
def pitches():


    # call the definition that clears all the widgets
    clear_widgets()

    # create a welcome label
    pitch1_label = tk.Label(root,
                            text="BEST LOCAL PITCHES ⚽",
                            font=("Gill Sans MS", 28, "bold"))
    pitch1_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # create a welcome label
    pitch2_label = tk.Label(root,
                            text="OUR TOP 10..",
                            font=("Gill Sans MS", 18, "bold"))
    pitch2_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # create labels with information about the pitches
    pitch2_label = tk.Label(root,
                            text="1️⃣ Adress: Laeiszstraße, 20357 Hamburg | Description: Tartan Ground in a cool neighborhood | Rating: ⭐⭐⭐⭐⭐",
                            font="Arial 10 bold",
                            fg="black",
                            bg="white"
                            )
    pitch2_label.place(x=0, y=70) # defining the place of the label

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

    # button to get back to the homepage
    pitches_button = tk.Button(root,
                               text="🏠",
                               font=("Comic Sans MS", 14, "bold"),
                               command=homepage
                               )
    pitches_button.pack(side=tk.BOTTOM, pady=1)

# This function carries out the steps for the biggest clubs page
def clubs():


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
                           font=("Gill Sans MS", 18, "bold"))
    club2_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # create labels with the topics to the answers
    club5_label = tk.Label(root,
                           text="Founding Year ⏳:",
                           font="Arial 12 bold",
                           fg="white",
                           bg="brown"
                           )
    club5_label.place(x=0, y=100) # defining the place of the label

    # create labels with the answers to the topics for each club
    club5a_label = tk.Label(root,
                            text="HSV: 1887 | St.Pauli: 1910",
                            font="Arial 10 bold",
                            fg="black",
                            bg="white"
                            )
    club5a_label.place(x=120, y=100)

    club6_label = tk.Label(root,
                           text="Trophies 🏆:",
                           font="Arial 12 bold",
                           fg="white",
                           bg="blue"
                           )
    club6_label.place(x=0, y=130)

    club6a_label = tk.Label(root,
                            text="HSV: 20 | St.Pauli: 9",
                            font="Arial 10 bold",
                            fg="black",
                            bg="white"
                            )
    club6a_label.place(x=120, y=130)

    club7_label = tk.Label(root,
                           text="Actual Division 🇩🇪:",
                           font="Arial 12 bold",
                           fg="white",
                           bg="brown"
                           )
    club7_label.place(x=0, y=160)

    club7a_label = tk.Label(root,
                            text="HSV: second (2. Bundesliga) | St.Pauli: second (2. Bundesliga)",
                            font="Arial 10 bold",
                            fg="black",
                            bg="white"
                            )
    club7a_label.place(x=120, y=160)

    club8_label = tk.Label(root,
                           text="Stadium 🏟:",
                           font="Arial 12 bold",
                           fg="white",
                           bg="blue"
                           )
    club8_label.place(x=0, y=190)

    club8a_label = tk.Label(root,
                            text="HSV: Volksparkstadion, Capacity: 57.000 | St.Pauli: Millerntor, Capacity: 29.546",
                            font="Arial 10 bold",
                            fg="black",
                            bg="white"
                            )
    club8a_label.place(x=120, y=190)

    club9_label = tk.Label(root,
                           text="Club Members 🎉:",
                           font="Arial 12 bold",
                           fg="white",
                           bg="brown"
                           )
    club9_label.place(x=0, y=220)

    club9a_label = tk.Label(root,
                            text="HSV: 100.000 | St.Pauli: 30.000",
                            font="Arial 10 bold",
                            fg="black",
                            bg="white"
                            )
    club9a_label.place(x=120, y=220)

    club10_label = tk.Label(root,
                            text="Unique 💎:",
                            font="Arial 12 bold",
                            fg="white",
                            bg="blue"
                            )
    club10_label.place(x=0, y=250)

    club10a_label = tk.Label(root,
                             text="HSV: Long Tradition & great History. | St.Pauli: Iconic & Millerntor Stadium in the heart of the city.",
                             font="Arial 10 bold",
                             fg="black",
                             bg="white"
                             )
    club10a_label.place(x=120, y=250)

    # create a label to show the user what to do next
    clubchoice_label = tk.Label(root,
                                text="Choose ➡️",
                                font="Arial 14 bold",
                                fg="black",
                                bg="white"
                                )
    clubchoice_label.place(x=120, y=320)

    # create a button to return back to the homepage
    clubs_button = tk.Button(root,
                             text="🏠",
                             font=("Comic Sans MS", 14, "bold"),
                             command=homepage
                             )
    clubs_button.pack(side=tk.BOTTOM, pady=5)

    # create a button for the game page of hsv
    hsv = tk.Button(root,
                    text="TEAM HSV 🔷",
                    command=hsvgame,
                    bg="white",  # distinct background color
                    fg="blue",  # contrasting foreground color
                    width=15, height=1  # Setting appropriate size
                    )

    hsv.pack(side=tk.BOTTOM, pady=1)  # Adding padding for spacing

    # create a button for the game page of stpauli
    stpauli = tk.Button(root,
                        text="TEAM ST.PAULI ☠️",
                        command=stpauligame,
                        bg="white",  # distinct background color
                        fg="brown",  # contrasting foreground color
                        width=15, height=1  # Setting appropriate size
                        )

    stpauli.pack(side=tk.BOTTOM, pady=1)  # Adding padding for spacing

# This function carries out the steps for the stpauli game page
def stpauligame():
    # initialise the library
    pg.init()

    # create variables with colour and sizes
    size = width, height = 600, 400
    colour = 0, 0, 0
    speed = [2, 2]

    # create the display screen
    screen = pg.display.set_mode(size)
    # set the caption
    pg.display.set_caption("ST.PAULI FOREVER 🎉")

    # place images on the display
    background = pg.image.load("images/stpauli_background.png")
    ball = pg.image.load("images/stpauli.gif")

    # convert ball into a rectangular object
    ballrect = ball.get_rect()

    # load music
    pg.mixer.music.load("music/stpauli_song.mp3")
    pg.mixer.music.play(-1)

    running = True
    while running:
        for event in pg.event.get():
            # close the game if someone clicks on the exit button
            if event.type == pg.QUIT:
                running = False

        # move ballrect
        ballrect = ballrect.move(speed)

        # if else statement to reverse the speed coordinates when it reaches the boundaries
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # code to run the game
        screen.fill(colour)  # changes the background colour
        screen.blit(background, (0, 0)) # places background image on the display
        screen.blit(ball, ballrect)  # place the image on the display

        # Draw quit button
        quit_button_rect = pg.Rect(500, 350, 80, 30)
        pg.draw.rect(screen, (255, 255, 255), quit_button_rect)
        quit_font = pg.font.Font(None, 30)
        quit_text = quit_font.render("Quit", True, (0, 0, 0))
        screen.blit(quit_text, (510, 355))

        # Update the display
        pg.display.flip()

        # Check for quit button click
        mouse_pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN and quit_button_rect.collidepoint(mouse_pos):
            running = False

    # Quit Pygame
    pg.quit()

# This function carries out the steps for the hsv game page
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

    # place images on our display
    background = pg.image.load("images/hsv_background.png")
    ball = pg.image.load("images/hsv.gif")

    # convert ball image into a rectangular object
    ballrect = ball.get_rect()

    # load music
    pg.mixer.music.load("music/hsv_song.mp3")
    pg.mixer.music.play(-1)

    running = True
    while running:
        for event in pg.event.get():
            # close the game if someone clicks on the exit button
            if event.type == pg.QUIT:
                running = False

        # move ballrect
        ballrect = ballrect.move(speed)

        # if else statement to reverse the speed coordinates when it reaches the boundaries
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # code to run the game
        screen.fill(colour)  # changes the background colour
        screen.blit(background, (0, 0)) # place background on the display
        screen.blit(ball, ballrect)  # place the image on the display

        # Draw quit button
        quit_button_rect = pg.Rect(500, 350, 80, 30)
        pg.draw.rect(screen, (255, 255, 255), quit_button_rect)
        quit_font = pg.font.Font(None, 30)
        quit_text = quit_font.render("Quit", True, (0, 0, 0))
        screen.blit(quit_text, (510, 355))

        # Update the display
        pg.display.flip()

        # Check for quit button click
        mouse_pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN and quit_button_rect.collidepoint(mouse_pos):
            running = False

    # Quit Pygame
    pg.quit()

# This function carries out the steps for the game page
def game():
    # Initialize Pygame
    pg.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600

    # Defining Colors
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BROWN = (139, 69, 19)

    # Create the screen
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("Game 🎮")

    # load music
    pg.mixer.music.load("music/playing.mp3")
    pg.mixer.music.play(-1)

    # Goal image
    goal_image = pg.image.load("images/goalie.png")

    # Player (ball) radius
    ball_radius = 10

    # Player position (initially at the center of the screen)
    player_x = screen_width // 2
    player_y = screen_height // 2

    # Score
    score = 0

    # Create a clock object to control the frame rate
    clock = pg.time.Clock()

    # Create a list to hold the enemies
    enemies = []

    # Function to generate enemy positions
    def generate_enemy_positions():
        enemies.clear()
        for _ in range(10):
            enemy_x = random.randint(20, screen_width - 20)
            enemy_y = random.randint(20, screen_height - 20)
            enemies.append((enemy_x, enemy_y))

    # Function to display score
    def display_score():
        font = pg.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLUE)
        screen.blit(score_text, (10, 10))

    def play_goal_music():
        # play music
        pg.mixer.music.load("music/goalmusic.mp3")
        pg.mixer.music.play()

    # Generate initial enemy positions
    generate_enemy_positions()

    # Initial goal position and movement
    goal_x = 150
    goal_y = 10
    goal_speed = 5
    goal_direction = 1

    # Game loop
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Move the goal
        goal_x += goal_speed * goal_direction
        if goal_x >= screen_width - goal_image.get_width() or goal_x <= 0:
            goal_direction *= -1

        # Check for collisions with enemies
        for enemy_x, enemy_y in enemies:
            if (player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2 <= ball_radius ** 2:
                pg.mouse.set_pos(screen_width // 2, screen_height // 2)
                score = 0
                goal_speed = 5
                generate_enemy_positions()

        # Check for goal scoring
        if goal_x < player_x < goal_x + goal_image.get_width() and goal_y < player_y < goal_y + goal_image.get_height():
            pg.mouse.set_pos(screen_width // 2, screen_height // 2)
            score += 1
            goal_speed += 5
            generate_enemy_positions()
            # play some music
            play_goal_music()


        # Get the current mouse position
        mouse_x, mouse_y = pg.mouse.get_pos()

        # Keep the player (ball) within the field bounds
        player_x = min(max(mouse_x, ball_radius), screen_width - ball_radius)
        player_y = min(max(mouse_y, ball_radius), screen_height - ball_radius)

        # Clear the screen
        screen.fill(WHITE)

        # Draw the goal
        screen.blit(goal_image, (goal_x, goal_y))

        # Draw the player (ball)
        pg.draw.circle(screen, BLUE, (player_x, player_y), ball_radius)

        # Draw the enemies
        for enemy_x, enemy_y in enemies:
            pg.draw.rect(screen, BROWN, (enemy_x, enemy_y, 20, 20))

        # Display score
        display_score()

        # Draw quit button
        quit_button_width = 80
        quit_button_height = 30
        quit_button_rect = pg.Rect(screen_width - quit_button_width - 10, screen_height - quit_button_height - 10,
                                   quit_button_width, quit_button_height)
        pg.draw.rect(screen, (255, 255, 255), quit_button_rect)
        quit_font = pg.font.Font(None, 30)
        quit_text = quit_font.render("Quit", True, (0, 0, 0))
        quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
        screen.blit(quit_text, quit_text_rect)

        # Update the display
        pg.display.flip()

        # Check for quit button click
        mouse_pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN and quit_button_rect.collidepoint(mouse_pos):
            running = False

        # Limit frame rate
        clock.tick(60)

    # Quit Pygame
    pg.quit()


# This function creates the homepage
def create_homepage():


    # clear widgets in the case widgets have been created
    clear_widgets()

    # add a welcome label
    welcome_label = tk.Label(root,
                             text="Do you Love Football?",
                             font="Arial 20 bold",
                             fg="white",
                             bg="red"
                             )
    welcome_label.place(x=180, y=100)

    # create button to get to the homepage
    createhomepage_button = tk.Button(root,
                                      text="YESSSS 🔥",
                                      font=("Gill Sans MS", 14, "bold"),
                                      command=homepage
                                      )
    createhomepage_button.pack(side=tk.BOTTOM, pady=10)


# call my homepage definition to create the home page when launching the gui
create_homepage()

# launch the gui
root.mainloop()
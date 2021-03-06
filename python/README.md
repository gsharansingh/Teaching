## Multithreading

> There are two libraries that can be used for the purpose:

`multithreading` library actually cannot create thread, it makes threads which work simulatneously. Whereas, `multiprocessing` library creates actual threads

#### [1] `multithreading`

```
ENABLE_JOIN = True

starting = time.time()
def hello(i, name):
    print(f"Hello {name}, you are sleeping for {i} seconds")
    time.sleep(i)
    print(f"thread took {time.time() - starting}\nbye {name}")

t1 = threading.Thread(target=hello, name="tread", args=(8, 'Mr. Singh'))

t1.start()
print("Hello stupid, wait")
if ENABLE_JOIN:
    t1.join()
time.sleep(3)
print(F"You will be always stupid\nmain took {time.time() - starting}") 
```

#### [2] `multiprocessing`
## C/C++ Extensions

#### [1] Setup
To add C/C++ extension, start with including the `Python.h` library

> *Windows users get these headers as part of the package when they use the binary Python installer*
* So, open up the directory in which the Python is installed. The path looks like : `C:\Users\{user_name}\AppData\Local\Programs\Python\{Python_version}\include`
* Copy the data inside the include floder and paste it into the `gcc` compiler's `include` directory

> We also have to install `python-dev`
* To install, open the terminal and type:

`$ python3 -m pip install python-dev-tools --user --upgrade`

> I LOST

---

## Making Game

*Required Library:* pygame
*To install the library, use:* `$ pip install pygame` in the **command prompt**

> #### Simple Program, opening up a 800x600 blank window:
```
import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

In the above code, `pygame.event.get()` returns a `list` of object type `Event` and when used with `.type` which looks like: 

    [<Event(17-VideoExpose {})>, <Event(16-VideoResize {'size': (800, 600), 'w': 800, 'h': 600})>, <Event(1-ActiveEvent {'gain': 0, 'state': 1})>, <Event(4-MouseMotion {'pos': (402, 599), 'rel': (403, 600), 'buttons': (0, 0, 0), 'window': None})>]

The code: 
```
for event in pygame.event.get():
    event.type
```
gives values depending open the action taken on the pygame window. e.g. `4` when we move curser, `12` when we press the **X** on window to close it (this means `pygame.QUIT == 12`)

---

> #### Adding the color to screen with `.fill()`

But this .fill() alone will not work, we have to update the screen as well. So we made a function for this

```
def re_draw_window():
    screen.fill((255, 0, 0))
    pygame.display.update()
```

*In this above fill function we passed `(255, 0, 0)` which represent the RGB values. So, the output screen will be __red__*.

Now the whole program looks like:
<details><summary>CODE</summary>
<p>

```
import pygame

# Intialize the pygame
pygame.init()

# window size
w_width = 800
w_height = 600

# create the screen
screen = pygame.display.set_mode((w_width, w_height))

# Redrawing the window
def re_draw_window():
    screen.fill((255, 0, 0))
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        re_draw_window()
        if event.type == pygame.QUIT:
            running = False
```
</p>
</details>

---

> #### Making a movable rectangle

We had made a class named *Player*, which can be used to create an object of rectangular player. The created class:
```
class Player():
    def __init__(self, x=0, y=0, width=100, height=100, color=(0, 0, 0)):
        '''
        A rectangular moved around using keys

        `x`: default 'x-axis' postion of rectangle
        `y`: default 'y-axis' postion of rectangle
        `width`: width of rectangle
        `height`: height of rectangle
        `color`: color of rectangle
        '''

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.displace = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.displace
        if keys[pygame.K_RIGHT]:
            self.x += self.displace
        if keys[pygame.K_UP]:
            self.y -= self.displace
        if keys[pygame.K_DOWN]:
            self.y += self.displace
        
        # Updating the rectangle's position
        self.rect = (self.x, self.y, self.width, self.height) 
```
After creating the object, we have to constantly monitor the keys pressed, which we did in `move` function of class. Finally, we draw the rectangle on the screen using `draw` function

<details><summary>CODE</summary>
<p>

```
import pygame

# Intialize the pygame
pygame.init()

# window size
w_width = 800
w_height = 600

# create the screen
screen = pygame.display.set_mode((w_width, w_height))

# Redrawing the window
def re_draw_window():
    screen.fill((255, 0, 0))
    p.move()
    p.draw(screen)
    pygame.display.update()

class Player():
    def __init__(self, x=0, y=0, width=100, height=100, color=(0, 0, 0)):
        '''
        A rectangular moved around using keys

        `x`: default 'x-axis' postion of rectangle
        `y`: default 'y-axis' postion of rectangle
        `width`: width of rectangle
        `height`: height of rectangle
        `color`: color of rectangle
        '''

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.displace = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.displace

        if keys[pygame.K_RIGHT]:
            self.x += self.displace

        if keys[pygame.K_UP]:
            self.y -= self.displace

        if keys[pygame.K_DOWN]:
            self.y += self.displace
        
        # Updating the rectangle's position
        self.rect = (self.x, self.y, self.width, self.height)


running = True
p = Player(300, 300, 100, 100, (255, 255, 255))

while running:

    for event in pygame.event.get():
        re_draw_window()
        if event.type == pygame.QUIT:
            running = False
```

</p>
</details>





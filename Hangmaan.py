import pygame
import sys
import random

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock()

WHITE = (127,255,212)
BLACK = (0, 0, 0)

title_font = pygame.font.Font(None, 50)
text_font = pygame.font.Font(None, 30)
button_font = pygame.font.Font(None, 40)

hangman_images = [pygame.image.load(f"img_{i}.png") for i in range(21, 27)]


words = ['PYGAME', 'PYTHON','PROJECTS']
score = 0

def draw_buttons(buttons):
    for box, letter, visible in buttons:
        if visible:
            pygame.draw.rect(screen, BLACK, box, 2)
            btn_text = button_font.render(letter, True, BLACK)
            btn_rect = btn_text.get_rect(center=box.center)
            screen.blit(btn_text, btn_rect)

def display_word(word, guessed):
    display_text = ''
    for letter in word:
        if letter in guessed:
            display_text += f"{letter} "
        else:
            display_text += '_ '
    text = text_font.render(display_text, True, BLACK)
    screen.blit(text, (300, 250))

def display_score(score):
    score_text = text_font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def main():
    global score
    hangman_status = 0
    guessed = []
    word = random.choice(words)
    buttons = []
    button_width = 50
    button_height = 50
    button_margin = 10
    num_buttons_per_row = 10

    # calculate the total width used by buttons
    total_buttons_width = (button_width + button_margin) * num_buttons_per_row
    start_x = (width - total_buttons_width) // 2

    for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        row = i // num_buttons_per_row
        col = i % num_buttons_per_row
        x = start_x + col * (button_width + button_margin)
        y = 400 + row * (button_height + button_margin)
        button_rect = pygame.Rect(x, y, button_width, button_height)
        buttons.append((button_rect, letter, True))

    while True:
        screen.fill(WHITE)
        screen.blit(hangman_images[hangman_status], (150, 100))
    # title
        title_text = title_font.render("Hangman", True, BLACK)
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 20))
        #  score
        display_score(score)
        #  word
        display_word(word, guessed)
        # buttons
        draw_buttons(buttons)
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button_rect, letter, visible in buttons:
                    if button_rect.collidepoint(mouse_pos) and visible:
                        guessed.append(letter)
                        buttons.remove((button_rect, letter, visible))
                        if letter not in word:
                            hangman_status += 1
                            if hangman_status == 6:
                                return False
                        if all(letter in guessed for letter in word):
                            score += 1
                            return True
        pygame.display.flip()
        clock.tick(20)

while True:
    if main():
        score +1

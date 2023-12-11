import pygame
import random
import time

pygame.init()

screen_size = (800, 900)
screen = pygame.display.set_mode(screen_size)

custom_font_path = "assets/font.ttf"
custom_font = pygame.font.Font(custom_font_path, 36)
bg_image = pygame.image.load("assets/space_bg.png")
title_font = pygame.font.Font(custom_font_path, 48)
text_font = pygame.font.Font(custom_font_path, 32)

correct_sound = pygame.mixer.Sound("assets/correct.wav")
incorrect_sound = pygame.mixer.Sound("assets/incorrect.wav")

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in range(pygame.K_a, pygame.K_z + 1):
                return chr(event.key)
    return None

def render_word(target_word, guesses):
    current_guess = "".join([char if char in guesses else "_" for char in target_word])
    return text_font.render(current_guess, True, (255, 255, 255))

def play_game():
    words = ["planet", "rocket", "alien", "jupiter", "galaxy"]
    target_word = random.choice(words)

    guesses = []
    score = 0
    correct_guesses = 0
    incorrect_guesses = 0

    start_ticks = pygame.time.get_ticks()
    end_ticks = start_ticks + 30 * 1000

    title_text = title_font.render("WordWarptoSpace", True, (255, 255, 255))

    while True:
        screen.blit(bg_image, (0, 0))
        screen.blit(title_text, (20, 20))
        screen.blit(render_word(target_word, guesses), (20, 120))

        guessed_letter = handle_input()
        if guessed_letter:
            if guessed_letter not in guesses:
                guesses.append(guessed_letter)
                if guessed_letter in target_word:
                    screen.blit(text_font.render(guessed_letter, True, (255, 255, 255)), (20, 200))
                    correct_sound.play()
                    correct_guesses += 1
                    score += 10
                else:
                    incorrect_sound.play()
                    incorrect_guesses += 1
                    score -= 5

        curr_time = pygame.time.get_ticks()
        time_left = max(0, end_ticks - curr_time)
        screen.blit(text_font.render(f"Time Left: {time_left//1000} seconds", True, (255, 255, 255)), (20, 60))

        if time_left == 0:
            break

        pygame.display.update()

    game_over_text = title_font.render("Game Over", True, (255, 255, 255))
    score_text = text_font.render(f"Your score: {score}", True, (255, 255, 255))
    screen.blit(game_over_text, (screen_size[0] // 2 - 100, screen_size[1] // 2 - 50))
    screen.blit(score_text, (screen_size[0] // 2 - 80, screen_size[1] // 2 + 20))
    pygame.display.update()

    pygame.time.delay(5000)

while True:
    play_game()

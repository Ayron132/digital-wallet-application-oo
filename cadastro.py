import pygame
import sys
import pygame_gui

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cadastro")

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

text_entry_positions = {
    "name": (100, 100),
    "cpf": (100, 160),
    "senha": (100, 220),
    "saldo": (100, 280),
}

name_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(((150, 100), (550, 50))),
    manager=MANAGER,
    object_id="#text_name"
)

cpf_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(((150, 160), (550, 50))),
    manager=MANAGER,
    object_id="#text_cpf"
)

password_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(( (150, 220), (550, 50))),
    manager=MANAGER,
    object_id="#text_password"
)

balance_input = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(((150, 280), (550, 50))),
    manager=MANAGER,
    object_id="#text_balance"
)

def get_user():
    while True:
        UI_REFRESH_RATE = CLOCK.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            MANAGER.process_events(event)

        MANAGER.update(UI_REFRESH_RATE)

        SCREEN.fill("white")

        font = pygame.font.Font(None, 36)
        for field, position in text_entry_positions.items():
            label = font.render(field.capitalize() + ":", True, (0, 0, 0))
            SCREEN.blit(label, (position[0] - 80, position[1] + 15))

        MANAGER.draw_ui(SCREEN)

        pygame.display.update()

get_user()
from os import environ


try:
    previous_support_prompt_setting = environ["PYGAME_HIDE_SUPPORT_PROMPT"]
except KeyError:
    previous_support_prompt_setting = "0"
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = previous_support_prompt_setting
del previous_support_prompt_setting

from screeninfo import get_monitors
from typing import NoReturn
from sys import exit

for monitor in get_monitors():
    if monitor.is_primary:
        SCREEN_WIDTH, SCREEN_HEIGHT = monitor.width, monitor.height
        break

pygame.init()
pygame.display.set_caption("Alien Sex Simulator")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("arial", round(SCREEN_WIDTH / 38.4))


class ReproduceAlienButton(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("resources/ufo.png")
        self.image = pygame.transform.scale(
            self.image, ((SCREEN_WIDTH / 5), (SCREEN_WIDTH / 4) / 3.50)
        )
        self.grey_image = pygame.image.load("resources/ufo_grey.png")
        self.grey_image = pygame.transform.scale(
            self.grey_image, ((SCREEN_WIDTH / 5), (SCREEN_WIDTH / 4) / 3.50)
        )
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT - 15
        self.rect.left = 15


class KillCowButton(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("resources/knife.png")
        self.image = pygame.transform.scale(
            self.image, ((SCREEN_WIDTH / 3) / 2.75, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.grey_image = pygame.image.load("resources/knife_grey.png")
        self.grey_image = pygame.transform.scale(
            self.grey_image, ((SCREEN_WIDTH / 3) / 2.75, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT - 15
        self.rect.left = (SCREEN_WIDTH / 5) + 50


class BuyCowButton(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("resources/cow.png")
        self.image = pygame.transform.scale(
            self.image, ((SCREEN_WIDTH / 3) / 2.75, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.grey_image = pygame.image.load("resources/cow_grey.png")
        self.grey_image = pygame.transform.scale(
            self.grey_image, ((SCREEN_WIDTH / 3) / 2.75, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT - 15
        self.rect.left = (SCREEN_WIDTH / 5) + ((SCREEN_WIDTH / 3) / 2.75) + 50


class UpgradeGainsButton(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("resources/upgrade_gains.png")
        self.image = pygame.transform.scale(
            self.image, ((SCREEN_WIDTH / 3) / 3.50, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.grey_image = pygame.image.load("resources/upgrade_gains_grey.png")
        self.grey_image = pygame.transform.scale(
            self.grey_image, ((SCREEN_WIDTH / 3) / 3.50, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.dead_image = pygame.image.load("resources/upgrade_gains_dead.png")
        self.dead_image = pygame.transform.scale(
            self.dead_image, ((SCREEN_WIDTH / 3) / 3.50, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT - 15
        self.rect.left = (SCREEN_WIDTH - self.rect.width) - 15


class UpgradePriceButton(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("resources/upgrade_price.png")
        self.image = pygame.transform.scale(
            self.image, ((SCREEN_WIDTH / 3) / 2.75, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.grey_image = pygame.image.load("resources/upgrade_price_grey.png")
        self.grey_image = pygame.transform.scale(
            self.grey_image, ((SCREEN_WIDTH / 3) / 2.75, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.dead_image = pygame.image.load("resources/upgrade_price_dead.png")
        self.dead_image = pygame.transform.scale(
            self.dead_image, ((SCREEN_WIDTH / 3) / 2.75, (SCREEN_WIDTH / 3) / 3.50)
        )
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT - 15
        self.rect.right = SCREEN_WIDTH - self.rect.width


def quit_all() -> NoReturn:
    pygame.quit()
    exit()


def render_text(text: str, color: tuple[int, int, int], placement: tuple[int, int]):
    rendered_text = FONT.render(text, True, color)
    screen.blit(rendered_text, placement)


def soft_round(number: float | int) -> float | int:
    if round(number) == number:
        return round(number)
    else:
        return number


def main() -> None:
    reproduction_button = ReproduceAlienButton()
    kill_cow_button = KillCowButton()
    buy_cow_button = BuyCowButton()
    upgrade_gains_button = UpgradeGainsButton()
    upgrade_price_button = UpgradePriceButton()
    background_image = pygame.image.load("resources/background.png")
    alive_cow_count = 5
    meat_count = 0
    alien_count = 2
    frame_count = 0
    mars_soil = 0
    gain_divider = 50
    price_divider = 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_all()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if reproduction_button.rect.collidepoint(*pygame.mouse.get_pos()):
                        if meat_count >= 0.5 and alien_count >= 2:
                            alien_count += 1
                            meat_count -= 0.5
                        elif alive_cow_count < 0.5:
                            print("Du har ikke nok køer!")
                    elif kill_cow_button.rect.collidepoint(*pygame.mouse.get_pos()):
                        if alive_cow_count >= 1:
                            alive_cow_count -= 1
                            meat_count += 2
                        else:
                            print("Du har ikke nok køer!")
                    elif buy_cow_button.rect.collidepoint(*pygame.mouse.get_pos()):
                        if mars_soil >= 150 / price_divider:
                            mars_soil -= 150 / price_divider
                            alive_cow_count += 1
                        else:
                            print("Du har ikke nok mars jord!")
                    elif upgrade_gains_button.rect.collidepoint(
                        *pygame.mouse.get_pos()
                    ):
                        if mars_soil >= 200 - (gain_divider * 2):
                            mars_soil -= 200 - (gain_divider * 2)
                            match gain_divider:
                                case 50:
                                    gain_divider = 40
                                case 40:
                                    gain_divider = 30
                                case 30:
                                    gain_divider = 20
                                case 20:
                                    print("Du kan ikke opgradere den her mere!")
                    elif upgrade_price_button.rect.collidepoint(
                        *pygame.mouse.get_pos()
                    ):
                        if mars_soil >= 200 - (price_divider * 2):
                            mars_soil -= 200 - (price_divider * 2)
                            match price_divider:
                                case 50:
                                    price_divider = 40
                                case 40:
                                    price_divider = 30
                                case 30:
                                    price_divider = 20
                                case 20:
                                    print("Du kan ikke opgradere den her mere!")

        frame_count += 1
        if frame_count % 30 == 0:
            mars_soil += alien_count / gain_divider

        screen.blit(background_image, (0, 0))

        if meat_count < 1:
            screen.blit(reproduction_button.grey_image, reproduction_button.rect)
        else:
            screen.blit(reproduction_button.image, reproduction_button.rect)

        if alive_cow_count < 1:
            screen.blit(kill_cow_button.grey_image, kill_cow_button.rect)
        else:
            screen.blit(kill_cow_button.image, kill_cow_button.rect)

        if mars_soil < 3:
            screen.blit(buy_cow_button.grey_image, buy_cow_button.rect)
        else:
            screen.blit(buy_cow_button.image, buy_cow_button.rect)

        if gain_divider == 15:
            screen.blit(upgrade_gains_button.dead_image, upgrade_gains_button.rect)
        elif mars_soil < 200 - (gain_divider * 2):
            screen.blit(upgrade_gains_button.grey_image, upgrade_gains_button.rect)
        else:
            screen.blit(upgrade_gains_button.image, upgrade_gains_button.rect)

        if price_divider == 15:
            screen.blit(upgrade_price_button.dead_image, upgrade_price_button.rect)
        elif mars_soil < 200 - (gain_divider * 2):
            screen.blit(upgrade_price_button.grey_image, upgrade_price_button.rect)
        else:
            screen.blit(upgrade_price_button.image, upgrade_price_button.rect)

        render_text(f"Cows: {alive_cow_count}", (255, 255, 255), (0, 0))
        render_text(f"Meat: {soft_round(meat_count)}", (255, 255, 255), (0, 50))
        render_text(f"Aliens: {alien_count}", (255, 255, 255), (0, 100))
        render_text(f"Mars Jord: {round(mars_soil, 3)}", (255, 255, 255), (0, 150))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

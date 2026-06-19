import game
import random
import math

pygame.init()

W, H = 300, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Bee Game")
clock = pygame.time.Clock()

# Bee
bee_x = 60
bee_y = H // 2
bee_vy = 0

GRAVITY = 0.7
BUZZ = -7

# Thorns: [x, y, radius, speed_x, drift_y]
thorns = []

# Flowers: [x, y, collected]
flowers = []

score = 0
game_over = False
started = False
frames = 0


def spawn_thorn():
    r = random.randint(14, 32)
    y = random.randint(r + 40, H - r - 40)
    sx = random.uniform(2.0, 3.5)
    dy = random.uniform(-0.5, 0.5)
    thorns.append([float(W + r), float(y), r, sx, dy])


def spawn_flower():
    y = random.randint(50, H - 70)
    flowers.append([float(W), float(y), False])


def draw_bg():
    for y in range(H - 60):
        ratio = y / (H - 60)
        r = int(135 + (100 - 135) * ratio)
        g = int(206 + (180 - 206) * ratio)
        b = int(235 + (140 - 235) * ratio)
        pygame.draw.line(screen, (r, g, b), (0, y), (W, y))

    pygame.draw.rect(screen, (90, 160, 60), (0, H - 60, W, 60))
    pygame.draw.rect(screen, (110, 180, 70), (0, H - 62, W, 4))


def draw_bee(y):
    iy = int(y)

    wing_up = frames % 6 < 3
    wy = iy - 16 if wing_up else iy - 11

    pygame.draw.ellipse(screen, (220, 230, 255),
                        (bee_x - 8, wy, 18, 13))
    pygame.draw.ellipse(screen, (220, 230, 255),
                        (bee_x + 3, wy, 18, 13))

    pygame.draw.ellipse(screen, (255, 200, 40),
                        (bee_x - 15, iy - 10, 30, 20))

    for sx in range(-6, 12, 6):
        pygame.draw.line(screen, (50, 40, 10),
                         (bee_x + sx, iy - 9),
                         (bee_x + sx, iy + 9), 3)

    pygame.draw.circle(screen, (255, 255, 255),
                       (bee_x + 11, iy - 3), 5)
    pygame.draw.circle(screen, (30, 30, 30),
                       (bee_x + 12, iy - 3), 3)

    pygame.draw.polygon(screen, (80, 60, 30), [
        (bee_x - 15, iy - 3),
        (bee_x - 15, iy + 3),
        (bee_x - 22, iy)
    ])


def draw_thorn(x, y, r):
    ix, iy = int(x), int(y)

    pts = []
    n = 10

    for i in range(n * 2):
        a = math.radians(i * 180 / n - 90)
        cr = r + 7 if i % 2 == 0 else r * 0.55

        pts.append((
            ix + int(cr * math.cos(a)),
            iy + int(cr * math.sin(a))
        ))

    pygame.draw.polygon(screen, (45, 100, 35), pts)
    pygame.draw.circle(screen, (65, 140, 50),
                       (ix, iy), int(r * 0.6))


def draw_flower(x, y):
    ix, iy = int(x), int(y)

    for i in range(5):
        angle = i * 72
        px = ix + int(8 * math.cos(math.radians(angle)))
        py = iy + int(8 * math.sin(math.radians(angle)))

        pygame.draw.circle(screen,
                           (255, 255, 100),
                           (px, py), 5)

    pygame.draw.circle(screen,
                       (255, 180, 50),
                       (ix, iy), 5)


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if game_over:
                bee_y = H // 2
                bee_vy = 0
                thorns.clear()
                flowers.clear()
                score = 0
                frames = 0
                game_over = False
                started = True

            else:
                started = True
                bee_vy = BUZZ

    if started and not game_over:

        bee_vy += GRAVITY
        bee_y += bee_vy
        frames += 1

        if frames % 15 == 0:
            score += 1

        rate = min(0.10, 0.04 + frames * 0.00004)

        if random.random() < rate:
            spawn_thorn()

        if random.random() < 0.008:
            spawn_flower()

        for t in thorns:
            t[0] -= t[3]
            t[1] += t[4]

            if t[1] - t[2] < 30 or t[1] + t[2] > H - 70:
                t[4] = -t[4]

        thorns[:] = [t for t in thorns if t[0] + t[2] > -10]

        for f in flowers:
            f[0] -= 2.5

        flowers[:] = [f for f in flowers
                      if f[0] > -15 and not f[2]]

        for t in thorns:
            dx = bee_x - t[0]
            dy = bee_y - t[1]

            dist = math.sqrt(dx * dx + dy * dy)

            if dist < t[2] + 13:
                game_over = True

        for f in flowers:

            if not f[2]:

                dx = bee_x - f[0]
                dy = bee_y - f[1]

                dist = math.sqrt(dx * dx + dy * dy)

                if dist < 18:
                    f[2] = True
                    score += 3

        if bee_y > H - 70 or bee_y < 10:
            game_over = True

    draw_bg()

    for f in flowers:
        if not f[2]:
            draw_flower(f[0], f[1])

    for t in thorns:
        draw_thorn(t[0], t[1], t[2])

    draw_bee(bee_y)

    font = pygame.font.Font(None, 36)

    screen.blit(
        font.render(str(score), True, (255, 255, 255)),
        (W // 2 - 10, 12)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame

pygame.init()

pygame.display.set_caption('Audio_Player')
screen = pygame.display.set_mode((500, 200))
type_shrift = pygame.font.Font('freesansbold.ttf', 16)
musics = ['/Users/sulejmenovtamerlan/Desktop/PP2/lab7/music/Lil Durk feat. Nicki Minaj - Extravagant.mp3', '/Users/sulejmenovtamerlan/Desktop/PP2/lab7/music/Post Malone & Swae Lee - Sunflower (OST Человек-паук Через Вселенные).mp3', '/Users/sulejmenovtamerlan/Desktop/PP2/lab7/music/Post Malone feat. Young Thug - Goodbyes.mp3']
a = 0

def guide(x, y):
    text = ("|<s> start| |<space> pause| |<c> continue| |-> next| |<- prev|")

    guide_text = type_shrift.render(text, True, (0, 0, 0))

    screen.blit(guide_text, (x, y))


done = False
while not done:
    screen.fill((255, 255, 255))
    screen.blit(screen, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer.music.load(musics[a])
                pygame.mixer.music.play()
                pygame.mixer.music.queue(musics[a + 1])
                pygame.mixer.music.queue(musics[a + 2])

            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()

            if event.key == pygame.K_c:
                pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                if a < len(musics) - 1:
                    pygame.mixer.music.load(musics[a + 1])
                    pygame.mixer.music.play()
                    a += 1
                else:
                    a = 0

                    pygame.mixer.music.load(musics[a])
                    pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                if a > 0:
                    pygame.mixer.music.load(musics[a - 1])
                    pygame.mixer.music.play()
                    a -= 1
                elif a == 0:
                    pygame.mixer.music.load(musics[len(musics) - 1])
                    pygame.mixer.music.play()
                    a = len(musics) - 1

    guide(30, 100)
    pygame.display.flip()
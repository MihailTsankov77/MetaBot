
class MonsterBase:
    def __init__(self, damage, player, hitbox):
        self.damage = damage
        self.player = player
        self.hitbox = hitbox
        self.has_taken_damage = False

    def update(self):
        if not self.has_taken_damage and self.hitbox.colliderect(self.player.rect):
            self.player.health -= self.damage
            self.has_taken_damage = True

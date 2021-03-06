import pygame

UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1
NEUTRAL = 0

class Ball:
   def __init__(self, x, y, radius, color, dx, dy):
      self.x = x
      self.y = y
      self.radius = radius
      self.color = color
      self.dx = dx
      self.dy = dy
      

   def draw_ball(self, screen):
      pygame.draw.ellipse(screen, self.color,
         pygame.Rect(self.x - self.radius, self.y - self.radius,
            self.radius * 2, self.radius * 2) )

   def horizontal_movement(self, width):
      return ( (self.dx > 0 and self.x + self.radius + self.dx < width) or
               (self.dx < 0 and self.x - self.radius + self.dx >= 0) )

   def vertical_movement(self, height):
      return ( (self.dy > 0 and self.y + self.radius + self.dy < height) or
               (self.dy < 0 and self.y - self.radius + self.dy >= 0) )

   def ball_movement(self, width, height, balls):
      if not self.horizontal_movement(width):
         self.dx *= -1
      if not self.vertical_movement(height):
         self.dy *= -1
      self.x += self.dx
      self.y += self.dy


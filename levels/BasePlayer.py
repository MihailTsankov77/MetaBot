
class BasePlayer:
    def __init__(self, x, health, robot):
        self.x = x
        self.__x = x
        
        self.health = health
        self.__health = health

        self.__robot = robot
    
    def _set_on_action_finished(self, on_action_finished):
        self.__robot.on_action_finished = on_action_finished
    
    def _set_delay(self, delay_timer):
        self.__robot.delay(delay_timer)

    def _update(self):
        moved_this_turn = self.x - self.__x
        self.__x = self.x
        self.robot_in_action = False

        if moved_this_turn:
            self.robot_in_action = True
            self.__robot.move_tile(moved_this_turn)

        damage_taken_this_turn = self.__health - self.health
        self.__health = self.health
        if damage_taken_this_turn:
            self.robot_in_action = True
            self.__robot.take_damage(damage_taken_this_turn)

        self.__robot.set_in_action(self.robot_in_action)
        self.__robot.update()

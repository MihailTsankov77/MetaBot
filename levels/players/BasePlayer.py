
class BasePlayer:
    def __init__(self, x, health, robot):
        self._base_x = x
        self.__base_original_x = x

        self._base_health = health
        self.__base_original_health = health

        self.__robot = robot
        self._trigger_action = False

    def _set_on_action_finished(self, on_action_finished):
        self.__robot.on_action_finished = on_action_finished

    def _set_delay(self, delay_timer):
        self.__robot.delay(delay_timer)

    def _sync(self):
        ...

    def _update(self):
        self._sync()

        moved_this_turn = self._base_x - self.__base_original_x
        self.__base_original_x = self._base_x
        self.robot_in_action = False

        if moved_this_turn:
            self.robot_in_action = True
            self.__robot.move_tile(moved_this_turn)

        damage_taken_this_turn = self.__base_original_health - self._base_health
        self.__base_original_health = self._base_health
        if damage_taken_this_turn:
            self.robot_in_action = True
            self.__robot.take_damage(damage_taken_this_turn)

        self.__robot.set_in_action(
            self.robot_in_action or self._trigger_action)
        self._trigger_action = False
        self.__robot.update()

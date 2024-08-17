import time


class Timer:
    def __init__(self, check_store_seconds, end_timer_seconds):
        self.check_store_seconds = check_store_seconds
        self.start_time = None
        self.end_timer_seconds = end_timer_seconds
        self.game_start_time = time.time()

    def counting_down(self):
        if self.start_time is None:
            self.start_time = time.time()
        return time.time() - self.start_time

    def is_countdown_zero(self):
        running_time = self.counting_down()
        return running_time >= self.check_store_seconds
        # if the running time equal to the seconds countdown

    def reset_timer(self):
        self.start_time = None

    def is_game_on(self):
        running_time = time.time() - self.game_start_time
        return running_time < self.end_timer_seconds

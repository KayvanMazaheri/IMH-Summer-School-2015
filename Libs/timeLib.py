from datetime import datetime

__start_time__ = datetime.now()
__end_time__ = 0
__last_lap__ = 0
__lap_list__ = []

def __get_micro_seconds__(datetime_obj):
  total_microseconds = datetime_obj.microseconds + datetime_obj.seconds * (10 ** 6)
  return total_microseconds

def initialize():
  global __lap_list__
  __lap_list__ = []
  return

def start():
  global __start_time__
  __start_time__ = datetime.now()
  return

def lap():
  global __end_time__ 
  global __last_lap__ 
  global __start_time__

  __end_time__= datetime.now()
  __last_lap__ = __end_time__ - __start_time__
  
  total_microseconds = __get_micro_seconds__(__last_lap__)

  __start_time__ = __end_time__
  __lap_list__.append(__last_lap__)
  return total_microseconds

def end():
  return lap()

def get_last_lap():
  return __get_micro_seconds__(__lap_list__[-1])

def print_formatted(total_microseconds):
  print("-- executed in {} microseconds. ".format(total_microseconds))
  return

def print_lap():
  lap_microseconds = lap()
  print_formatted(lap_microseconds)
  return

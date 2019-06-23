# coding: utf-8

__author__ = '代码会说话'

"""
假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。由于道路的限制，车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。

这儿有一份行程计划表 trips[][]，其中 trips[i] = [num_passengers, start_location, end_location] 包含了你的第 i 次行程信息：

必须接送的乘客数量；
乘客的上车地点；
以及乘客的下车地点。
这些给出的地点位置是从你的 初始 出发位置向前行驶到这些地点所需的距离（它们一定在你的行驶方向上）。

请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所用乘客的任务（当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false）。

 

示例 1：

输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false
示例 2：

输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true
示例 3：

输入：trips = [[2,1,5],[3,5,7]], capacity = 3
输出：true
示例 4：

输入：trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
输出：true
 

提示：

你可以假设乘客会自觉遵守 “先下后上” 的良好素质
trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
"""

from collections import defaultdict
from typing import List, NamedTuple

class Trip(NamedTuple):
  num_passengers:int
  start_location:int
  end_location:int

class Car:
  def __init__(self,*,capacity:int):
    self.capacity = capacity
    self.empty_seats = capacity
    self.location = 0
    self.end_location_map = defaultdict(list)

  def can_take(self,trip:Trip):
    return self.empty_seats >= trip.num_passengers

  def take(self,trip:Trip):
    self.empty_seats -= trip.num_passengers
    self.end_location_map[trip.end_location].append(trip)

  def get_off_from(self,location):
    trips = self.end_location_map[location]
    if trips:
      del self.end_location_map[location]
    for trip in trips:
      self.empty_seats += trip.num_passengers

  def move_to(self,location:int):
    for loc in range(self.location,location):
      self.get_off_from(loc)
    self.location = location
    self.get_off_from(location)



class Solution:
  def carPooling(self, trips: List[List], capacity: int) -> bool:
    car = Car(capacity=capacity)
    trips_t = [Trip(*trip) for trip in trips]
    start_location_to_trips = defaultdict(list)
    for trip in trips_t:
      start_location_to_trips[trip.start_location].append(trip)

    start_locations = list(start_location_to_trips.keys())
    start_locations.sort()
    for start_location in start_locations:
      cur_trips = start_location_to_trips[start_location]
      car.move_to(start_location)
      for trip in cur_trips:
        if car.can_take(trip):
          car.take(trip)
        else:
          return False
    return True


def test():
  s = Solution()
  assert s.carPooling([[3,2,8],[4,4,6],[10,8,9]], 11) == True

  assert s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4) == False
  assert s.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5) == True

  assert s.carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3) == True
  assert s.carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11) == True

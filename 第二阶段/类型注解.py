# 非强制，仅作为标识

from typing import Union

def play_game(name: str, players: Union[int, str]):
    print(f'游戏名{name}, 玩家{players}人')


play_game("王者荣耀", 10)
play_game("王者荣耀", "十")



name = "" # type: str
dict1: dict[str, int] = {"a":1}
tuple1: tuple = (1, 2)


# 定义返回值类型
def get_user_info() -> str:
    return input('输入个人信息')

a = get_user_info()
print(a, type(a))
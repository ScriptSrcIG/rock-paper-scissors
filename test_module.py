from RPS import player
from RPS_game import play, quincy, abbey, kris, mrugesh

def test():
    print("Testing against Quincy...")
    assert play(player, quincy, 1000) >= 60

    print("Testing against Abbey...")
    assert play(player, abbey, 1000) >= 60

    print("Testing against Kris...")
    assert play(player, kris, 1000) >= 60

    print("Testing against Mrugesh...")
    assert play(player, mrugesh, 1000) >= 60

    print("All tests passed!")
  

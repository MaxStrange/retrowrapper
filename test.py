import retrowrapper

if __name__ == "__main__":
    game = "SonicTheHedgehog-Genesis"
    state = "GreenHillZone.Act1"
    env1 = retrowrapper.RetroWrapper(game, state=state)
    env2 = retrowrapper.RetroWrapper(game, state=state)
    _obs = env1.reset()
    _obs = env2.reset()

    done = False
    while not done:
        action = env1.action_space.sample()
        _obs, _rew, done, _info = env1.step(action)
        env1.render()

        action = env2.action_space.sample()
        _obs, _rew, done, _info = env2.step(action)
        _obs, _rew, done, _info = env2.step(action)
        env2.render()
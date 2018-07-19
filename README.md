# retrowrapper

Wrapper for OpenAI Retro envs for parallel execution

OpenAI's [Retro](https://github.com/openai/retro) exposes an OpenAI [gym](https://gym.openai.com/) interface for Deep Reinforcement Learning, but
unfortunately, their back-end only allows one emulator instance per process. To get around this, I wrote this class.

## To Use

To use it, just instantiate it like you would a normal retro environment, and then treat it exactly the same, but now you can have multiples in a single python process. Magic!

```python
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
        env2.render()
```

## Using a custom make function

Sometimes you will need a custom make function, for example the `retro_contest`
repository requires you to use their make function rather than `retro.make`.

In these cases you can use the `retrowrapper.set_retro_make()` to set a new
make function.

Example usage:

```python
import retrowrapper
from retro_contest.local import make

retrowrapper.set_retro_make( make )

env1 = retrowrapper.RetroWrapper(
    game='SonicTheHedgehog2-Genesis', 
    state='MetropolisZone.Act1'
)
env2 = retrowrapper.RetroWrapper(
    game='SonicTheHedgehog2-Genesis', 
    state='MetropolisZone.Act2'
)
```
